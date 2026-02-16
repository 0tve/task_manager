# REST API для управления задачами и клиентами.
# Порядок запуска:
1. Создать базу данных и настроить переменные окружения в `settings.env`
2. Выполнить команды: `pip install -r requirements.txt` и `alembic upgrade head`
3. Запустить приложение: `python.exe -m src.main`
4. Открыть в браузере: `http://127.0.0.1:8000/`
# Функционал:
- CRUD для задач и клиентов
- статус задачи - в работе / завершено
- статистика по задачам (общая и по клиентам): сколько всего, сколько выполнено и процент выполненных

***Акцент сделан на архитектуру приложения***. Реализована слоистая архитектура вместе с паттернами *Repository* и *Unit of Work*.

Стек: FastAPI, SQLAlchemy, Pydantic, Pydantic Settings, uvicorn. В качестве СУБД использовал PostgreSQL.
# Примеры запросов:

Попытка добавить задачу несуществующему клиенту:

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/b78b282d-32e4-4bb7-8f06-d81dd5dc954b" />

Создание клиента:

<img width="600" height="470" alt="image" src="https://github.com/user-attachments/assets/268a4f4f-f742-4044-b446-09360a561956" />

Успешное создание задачи:

<img width="600" height="490" alt="image" src="https://github.com/user-attachments/assets/2d08773a-e3a6-4621-8ad8-6c7bbe432354" />

Изменение статуса задачи (завершена):

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/2ffa6de6-8386-4090-8dd3-9f79635481f1" />

Получение списка задач:

<img width="600" height="570" alt="image" src="https://github.com/user-attachments/assets/c0104c1f-b438-4a16-b781-94b2d7e2e4b0" />

Получение конкретной задачи:

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/4b71b50f-2d45-4215-b5ca-ca337c1934e1" />

Получение общей статистики по задачам:

<img width="600" height="330" alt="image" src="https://github.com/user-attachments/assets/3cf97047-6eba-48ae-ae67-683f37859fc1" />

Удаление задачи (ответ 204):

<img width="600" height="265" alt="image" src="https://github.com/user-attachments/assets/cb2fbc7b-00b8-471c-8dd5-76169da55c43" />

Списки задач, закрепленные за клиентами:

<img width="600" height="930" alt="image" src="https://github.com/user-attachments/assets/c975ccd9-c476-43ed-9554-b003c1954a07" />

Статистика по задачам конкретного клиента:

<img width="600" height="430" alt="image" src="https://github.com/user-attachments/assets/500794a2-2c84-42d2-8966-cc14da74761c" />
