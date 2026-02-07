import abc
import types

from sqlalchemy.ext import asyncio as sa_asyncio

from src.components import repository as repo


class BaseUnitOfWork(abc.ABC):
    tasks: repo.BaseTaskRepository
    clients: repo.BaseClientRepository

    @abc.abstractmethod
    def __init__(self, async_sessionmaker: sa_asyncio.async_sessionmaker[sa_asyncio.AsyncSession]) -> None:
        ...

    @abc.abstractmethod
    async def __aenter__(self) -> 'BaseUnitOfWork':
        ...

    @abc.abstractmethod
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None
    ) -> None:
        ...

    @abc.abstractmethod
    async def commit(self) -> None:
        ...

    @abc.abstractmethod
    async def rollback(self) -> None:
        ...


class SQLAlchemyUnitOfWork(BaseUnitOfWork):
    def __init__(self, async_sessionmaker: sa_asyncio.async_sessionmaker[sa_asyncio.AsyncSession]) -> None:
        self.async_sessionmaker = async_sessionmaker

    async def __aenter__(self) -> 'BaseUnitOfWork':
        self._session = self.async_sessionmaker()
        self.tasks = repo.TaskRepository(self._session)
        self.clients = repo.ClientRepository(self._session)
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
