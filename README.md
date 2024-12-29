# Ore Concentrate Test

Система позволяет сохранять данные (содержание различных элементов) в железнорудном концентрате и просматривать
сводный отчет за месяц о всех концентратах

У системы доступен сваггер по адресу `/docs` или `/redoc`

### .env
```dotenv
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=host
POSTGRES_PORT=5432
POSTGRES_NAME=db
SECRET_KEY=random_string
```

## Запуск

### Docker
1. Заполнить .env файл
2. Команда `docker-compose up --build`
3. Приложение будет доступно по адресу localhost:8000
