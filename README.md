# Тестовое задание на вакансию Python разработчика в Didenok Team

## Менеджер паролей
### Описание:
API с базовым функционалом менеджера паролей.


### Запуск:
#### 1. Скопировать проект на компьютер, перейти в папку didenok_test.

- Создать файл ```.env``` и добавить в него следующие строки:
```
SECRET_KEY="django-insecure-+bg%+#=t@*v72q!j3k8bw^4-g(m79e_55ko5n%)yqu7xc(0j0^"
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
- Выполнить команду для сборки:\
```docker-compose up -d```

#### 2. После сборки проекта перейти в контейнеры и выполнить миграции:

- ```docker-compose exec api python manage.py migrate```

#### 3. Доступные эндпоинты и примеры запросов:
В заголовках необходимо передать JWT токен в виде пары ключ-значение ```Autorization : Bearer <token>```  
- ```http://0.0.0.0:80/users/``` - POST, регистрация
    Запрос:  
    ```
    {
        "username": "username",
        "password": "password"
    }
    ```
- ```http://0.0.0.0:80/api/users/me/``` - GET, информация о текущем пользователе
- ```http://0.0.0.0:80/api/auth/jwt/create/``` - POST, получение JWT токена  
    Запрос:  
    ```
    {
        "username": "username",
        "password": "password"
    }
    ```
    Ответ:  
    ```
    {
        "refresh": <token>,
        "access": <token>
    }
    ```
- ```http://0.0.0.0:80/password/yundex``` - POST, создание новой пары сервис-пароль, редактирование пароля  
    Запрос:  
    ```
    {
        "password": "very_secret_pass"
    }
    ```
    Ответ:  
    ```
    {
        "password": "very_secret_pass",
        "service_name": "yundex"
    }
    ```
- ```http://0.0.0.0:80/password/yundex``` - GET, получение пароля по имени сервиса   
   
    Ответ:  
    ```
    {
        "password": "very_secret_pass",
        "service_name": "yundex"
    }
    ```
- ```http://0.0.0.0:80/password/?service_name=yun``` - GET, получение пароля по части имени сервиса  

    Ответ:  
    ```
    [
        {
            "password": "very_secret_pass",
            "service_name": "yundex"
        }
    ]
    ```
