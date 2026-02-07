from src.components.services import base
from src.entities import models
from src.entities.schemas import clients


class ClientService(base.BaseService):
    entity_name = 'Клиент'

    async def create(self, data: clients.ClientCreate) -> models.Client:
        client = await self.uow.clients.create(data.model_dump())
        await self.uow.commit()
        return client

    async def get_client(self, id: int) -> models.Client:
        return await self.uow.clients.get_by_id(id)

    async def get_clients(self, offset: int, limit: int) -> list[models.Client]:
        return list(await self.uow.clients.get_all(offset, limit))

    async def update_client(self, id: int, data: clients.ClientUpdate) -> models.Client:
        client = await self.uow.clients.update_by_id(id, data.model_dump(exclude_none=True))
        await self.uow.commit()
        return client

    async def delete_client(self, id: int) -> None:
        await self.uow.clients.delete_by_id(id)
        await self.uow.commit()

    async def get_client_tasks(self, offset: int, limit: int) -> list[models.Client]:
        return list(await self.uow.clients.get_all_with_tasks(offset, limit))

    async def get_client_task_stats(self, client_id: int) -> clients.ClientTaskStats:
        client = await self.uow.clients.get_by_id(client_id)
        stats = await self.uow.tasks.get_task_stats(client_id)
        return clients.ClientTaskStats.model_validate({
            'id': client.id,
            'name': client.name,
            'surname': client.surname,
            'patronymic': client.patronymic,
            'task_stats': stats
        })
