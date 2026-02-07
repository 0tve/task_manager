import fastapi
from fastapi import status

from src.components import dependencies as deps
from src.entities.schemas import tasks

router = fastapi.APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('', response_model=tasks.Task, summary='Создать задачу', status_code=status.HTTP_201_CREATED)
async def create_task(
    service: deps.TaskServiceDep,
    data: tasks.TaskCreate
):
    return await service.create(data)


@router.get('/stats', response_model=tasks.TaskStats, summary='Получить статистику по задачам')
async def get_task_stats(
    service: deps.TaskServiceDep
):
    return await service.get_task_stats()


@router.get('', response_model=list[tasks.Task], summary='Получить все задачи')
async def get_tasks(
    service: deps.TaskServiceDep,
    offset: int = fastapi.Query(default=0, ge=0),
    limit: int = fastapi.Query(default=100, ge=0)
):
    return await service.get_tasks(offset, limit)


@router.get('/{id}', response_model=tasks.Task, summary='Получить одну задачу по ID')
async def get_task(
    id: int,
    service: deps.TaskServiceDep
):
    return await service.get_task(id)


@router.patch('/{id}', response_model=tasks.Task, summary='Обновить задачу')
async def update_task(
    id: int,
    service: deps.TaskServiceDep,
    data: tasks.TaskUpdate
):
    return await service.update_task(id, data)


@router.delete('/{id}', summary='Удалить задачу', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    id: int,
    service: deps.TaskServiceDep
) -> None:
    await service.delete_task(id)
