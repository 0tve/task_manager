import fastapi
from fastapi import responses

router = fastapi.APIRouter(tags=['index'])


@router.get('/')
async def index():
    return responses.FileResponse('src/templates/index.html')
