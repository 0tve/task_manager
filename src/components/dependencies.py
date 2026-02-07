import typing as t
from collections import abc as c

import fastapi

from src.components import db, unit_of_work
from src.components.services import clients, tasks


async def get_uow() -> c.AsyncGenerator[unit_of_work.BaseUnitOfWork, None]:
    async with unit_of_work.SQLAlchemyUnitOfWork(db.async_sessionmaker) as uow:
        yield uow


def get_task_service(uow: t.Annotated[unit_of_work.BaseUnitOfWork, fastapi.Depends(get_uow)]) -> tasks.TaskService:
    return tasks.TaskService(uow)


def get_client_service(uow: t.Annotated[unit_of_work.BaseUnitOfWork, fastapi.Depends(get_uow)]) -> clients.ClientService:
    return clients.ClientService(uow)


TaskServiceDep = t.Annotated[tasks.TaskService,
                             fastapi.Depends(get_task_service)]
ClientServiceDep = t.Annotated[clients.ClientService,
                               fastapi.Depends(get_client_service)]
