import fastapi
from fastapi import status

from src.components import dependencies as deps
from src.entities.schemas import clients

router = fastapi.APIRouter(prefix='/clients', tags=['clients'])


@router.post('', response_model=clients.Client, summary='Создать клиента', status_code=status.HTTP_201_CREATED)
async def create_client(
    service: deps.ClientServiceDep,
    data: clients.ClientCreate
):
    return await service.create(data)


@router.get('', response_model=list[clients.Client], summary='Получить всех клиентов')
async def get_clients(
    service: deps.ClientServiceDep,
    offset: int = fastapi.Query(default=0, ge=0),
    limit: int = fastapi.Query(default=100, ge=0)
):
    return await service.get_clients(offset, limit)


@router.get('/tasks', response_model=list[clients.ClientTasks], summary='Получить задачи клиентов')
async def get_client_tasks(
    service: deps.ClientServiceDep,
    offset: int = fastapi.Query(default=0, ge=0),
    limit: int = fastapi.Query(default=100, ge=0)
):
    return await service.get_client_tasks(offset, limit)


@router.get('/{id}/stats', response_model=clients.ClientTaskStats, summary='Статистика по задачам клиента')
async def get_client_task_stats(
    id: int,
    service: deps.ClientServiceDep
):
    return await service.get_client_task_stats(id)


@router.get('/{id}', response_model=clients.Client, summary='Получить одного клиента по ID')
async def get_client(
    id: int,
    service: deps.ClientServiceDep
):
    return await service.get_client(id)


@router.patch('/{id}', response_model=clients.Client, summary='Обновить клиента')
async def update_client(
    id: int,
    service: deps.ClientServiceDep,
    data: clients.ClientUpdate
):
    return await service.update_client(id, data)


@router.delete('/{id}', summary='Удалить клиента', status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(
    id: int,
    service: deps.ClientServiceDep
) -> None:
    await service.delete_client(id)
