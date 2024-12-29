from datetime import date
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, extract
from sqlalchemy.orm import Session
from models import User, Concentrate
from schemas import Token, DatabaseUser, Concentrate as ConcentrateSchema, BulkConcentrate, Report
from database import get_session
from utils.user import get_current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/token', response_model=Token)
async def sign_in(form_data: OAuth2PasswordRequestForm, session = Depends(get_session)):
    user = session.scalars(select(User).where(User.username == form_data.username)).one()
    if not user or not user.validate_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    access_token = user.create_access_token()
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.post('/sign_up')
async def sign_up(data: DatabaseUser, session = Depends(get_session)):
    user = User(
        username=data.username,
        password=User.hash_password(data.password)
    )
    session.add(user)
    session.commit()

@app.post('/concentrate', dependencies=[Depends(get_current_user)], status_code=201)
async def create_concentrate(data: ConcentrateSchema, session: Session = Depends(get_session)):
    concentrate = Concentrate(**data.model_dump())
    session.add(concentrate)
    session.commit()

    return "Ok"

@app.post('/concentrate/bulk', dependencies=[Depends(get_current_user)], status_code=201)
async def bulk_create_concentrate(bulk_data: BulkConcentrate, session: Session = Depends(get_session)):
    session.add_all(Concentrate(**model_data.model_dumb()) for model_data in bulk_data.data)
    session.commit()

    return "Ok"

@app.get('/concentrate/report/{report_date}', dependencies=[Depends(get_current_user)], response_model=Report)
async def get_report(report_date: date, session: Session = Depends(get_session)):
    request = select(Concentrate).where(
        extract('month', Concentrate.date) == report_date.month,
        extract('year', Concentrate.date) == report_date.year
    )
    result = session.scalars(request).all()

    report = {
        'iron_content': {'minimum': result[0].iron_content, 'maximum': 0, 'average': 0},
        'silicon_content': {'minimum': result[0].silicon_content, 'maximum': 0, 'average': 0},
        'aluminium_content': {'minimum': result[0].aluminium_content, 'maximum': 0, 'average': 0},
        'calcium_content': {'minimum': result[0].calcium_content, 'maximum': 0, 'average': 0},
        'sulfur_content': {'minimum': result[0].sulfur_content, 'maximum': 0, 'average': 0},
    }

    for concentrate in result:
        for key in report:
            value = concentrate.__getattribute__(key)
            report[key]['minimum'] = min(report[key]['minimum'], value)
            report[key]['maximum'] = max(report[key]['maximum'], value)
            report[key]['average'] += value / len(result)

    return report
