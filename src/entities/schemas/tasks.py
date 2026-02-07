import datetime

import pydantic

from src.entities.schemas import shared


class Task(pydantic.BaseModel):
    id: int
    client_id: int
    title: shared.str100
    description: str | None
    is_completed: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class TaskCreate(pydantic.BaseModel):
    title: shared.str100
    description: str | None = None
    client_id: int


class TaskUpdate(pydantic.BaseModel):
    client_id: int | None = None
    title: shared.str100 | None = None
    description: str | None = None
    is_completed: bool | None = None


class TaskStats(pydantic.BaseModel):
    total: int
    completed: int
    completion_rate: float
