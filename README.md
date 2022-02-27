# Table of items
Тестовое задание для компании WelbeX.

## Используемые технологии
Web-сервис написан на **Python 3.8** с использованием фреймворка **Flask**, 
база данных - **PostgreSQL**, frontend - **Vue.js**. 

## Запуск проекта
### .env файл
В директории проекта необходимо создать файл `.env` с переменными окружения
```text
SECRET_KEY=secret_key
FLASK_APP=app
FLASK_ENV=production
SQLALCHEMY_DATABASE_URI=postgresql://db_user:db_pass@db:5432/table
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_pass
POSTGRES_DB=table
```

### Запуск сервисов
Для запуска сервисов необходимо ввести команду
```shell
docker-compose up --build -d
```
После запуска сервисов сайт будет доступен по адресу http://localhost:80

### Заполнение базы данных
Для заполнения базы данных используется SQL скрипт `backend/data.sql`
```shell
docker-compose exec web flask fill-db
```

### Завершение работы
Для завершения работы сервисов необходимо выполнить команду
```shell
docker-compose down
```
