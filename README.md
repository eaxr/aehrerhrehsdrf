angular + fastapi + sqlalchemy

```
Используемые пакеты:
asyncio==3.4.3
asyncpg==0.23.0
sqlalchemy==1.4.36
pydantic-sqlalchemy==0.0.9
psycopg2==2.8.4
alembic==1.7.7
fastapi==0.68.0
uvicorn==0.14.0
```

Создание контейнеров web приложения из docker-compose файла. Создание frontend контейнера с angular, создание контейнера с postgresql и backend контейнера с fastapi,sqlalchemy:
![alt text](https://github.com/eaxr/aehrerhrehsdrf/blob/main/images/fa1.gif?raw=true)

Создание пары заметок, которые сохраняются в базе данных и создание множества заметок, которые отображаются в таблице. Таблица имеет воможность пролистать созданные заметки:
![alt text](https://github.com/eaxr/aehrerhrehsdrf/blob/main/images/fa2.gif?raw=true)

Общий вид:
![alt text](https://github.com/eaxr/aehrerhrehsdrf/blob/main/images/image.png?raw=true)
