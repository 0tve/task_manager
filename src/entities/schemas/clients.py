import datetime

import pydantic

from src.entities.schemas import shared, tasks


class Client(pydantic.BaseModel):
    id: int
    name: shared.str100
    surname: shared.str100
    patronymic: shared.str100 | None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ClientCreate(pydantic.BaseModel):
    name: shared.str100
    surname: shared.str100
    patronymic: shared.str100 | None = None


class ClientUpdate(pydantic.BaseModel):
    name: shared.str100 | None = None
    surname: shared.str100 | None = None
    patronymic: shared.str100 | None = None


class ClientTasks(pydantic.BaseModel):
    id: int
    name: shared.str100
    surname: shared.str100
    patronymic: shared.str100 | None
    tasks: list[tasks.Task]


class ClientTaskStats(pydantic.BaseModel):
    id: int
    name: shared.str100
    surname: shared.str100
    patronymic: shared.str100 | None
    task_stats: tasks.TaskStats
