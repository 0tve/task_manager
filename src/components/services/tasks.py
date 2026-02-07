from src.components.services import base
from src.entities import models
from src.entities.schemas import tasks


class TaskService(base.BaseService):
    entity_name = 'Задача'

    async def create(self, data: tasks.TaskCreate) -> models.Task:
        await self.uow.clients.get_by_id(data.client_id)
        task = await self.uow.tasks.create(data.model_dump())
        await self.uow.commit()
        return task

    async def get_task_stats(self) -> tasks.TaskStats:
        return await self.uow.tasks.get_task_stats()

    async def get_task(self, id: int) -> models.Task:
        return await self.uow.tasks.get_by_id(id)

    async def get_tasks(self, offset: int, limit: int) -> list[models.Task]:
        return list(await self.uow.tasks.get_all(offset, limit))

    async def update_task(self, id: int, data: tasks.TaskUpdate) -> models.Task:
        if data.client_id is not None:
            await self.uow.clients.get_by_id(data.client_id)
        task = await self.uow.tasks.update_by_id(id, data.model_dump(exclude_none=True))
        await self.uow.commit()
        return task

    async def delete_task(self, id: int) -> None:
        await self.uow.tasks.delete_by_id(id)
        await self.uow.commit()
