import abc
import typing as t
from collections import abc as c

import sqlalchemy as sa
from sqlalchemy import exc, orm
from sqlalchemy.ext import asyncio as sa_asyncio

from src.entities import models
from src.entities.schemas import tasks


class BaseRepository[ModelT: models.BaseWithId](abc.ABC):
    @abc.abstractmethod
    async def get_by_id(self, id: int) -> ModelT:
        ...

    @abc.abstractmethod
    async def get_all(self, offset: int,
                      limit: int) -> c.Sequence[ModelT]:
        ...

    @abc.abstractmethod
    async def create(self, data: dict[str, t.Any]) -> ModelT:
        ...

    @abc.abstractmethod
    async def update_by_id(
            self, id: int, data: dict[str, t.Any]) -> ModelT:
        ...

    @abc.abstractmethod
    async def delete_by_id(self, id: int) -> None:
        ...


class SQLAlchemyRepository[ModelT: models.BaseWithId](BaseRepository[ModelT]):
    model: type[ModelT]

    def __init__(self, session: sa_asyncio.AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, id: int) -> ModelT:
        result = await self._session.get(self.model, id)
        if result is None:
            raise exc.NoResultFound
        return result

    async def get_all(self, offset: int, limit: int) -> c.Sequence[ModelT]:
        stmt = sa.select(self.model).offset(offset).limit(limit)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def create(self, data: dict[str, t.Any]) -> ModelT:
        instance = self.model(**data)
        self._session.add(instance)
        await self._session.flush()
        return instance

    async def update_by_id(self, id: int, data: dict[str, t.Any]) -> ModelT:
        stmt = (
            sa.update(self.model)
            .where(self.model.id == id)
            .values(**data)
            .returning(self.model)
        )
        result = await self._session.execute(stmt)
        try:
            return result.scalar_one()
        except exc.NoResultFound:
            raise

    async def delete_by_id(self, id: int) -> None:
        stmt = sa.delete(self.model).where(self.model.id == id)
        result = await self._session.execute(stmt)
        if result.rowcount == 0:  # type: ignore
            raise exc.NoResultFound


class BaseTaskRepository(BaseRepository[models.Task]):
    @abc.abstractmethod
    async def get_task_stats(self, client_id: int | None = None) -> tasks.TaskStats:
        ...


class TaskRepository(SQLAlchemyRepository[models.Task], BaseTaskRepository):
    model = models.Task

    async def get_task_stats(self, client_id: int | None = None) -> tasks.TaskStats:
        stmt = sa.select(
            sa.func.count().label('total'),
            sa.func.count()
            .filter(models.Task.is_completed == True)
            .label('completed'),
        )

        if client_id is not None:
            stmt = stmt.where(models.Task.client_id == client_id)

        result = await self._session.execute(stmt)
        row = result.one()
        total = row.total
        completed = row.completed
        completion_rate = (completed / total * 100) if total > 0 else 0.0
        return tasks.TaskStats(
            total=total,
            completed=completed,
            completion_rate=round(completion_rate, 2),
        )


class BaseClientRepository(BaseRepository[models.Client]):
    @abc.abstractmethod
    async def get_all_with_tasks(self, offset: int, limit: int) -> c.Sequence[models.Client]:
        ...


class ClientRepository(SQLAlchemyRepository[models.Client], BaseClientRepository):
    model = models.Client

    async def get_all_with_tasks(self, offset: int, limit: int) -> c.Sequence[models.Client]:
        stmt = (
            sa.select(self.model)
            .options(orm.selectinload(self.model.tasks))
            .offset(offset)
            .limit(limit)
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()
