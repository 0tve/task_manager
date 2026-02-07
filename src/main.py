import fastapi
import uvicorn
from fastapi import status
from sqlalchemy import exc

from src.api import clients, index, tasks

app = fastapi.FastAPI()
app.include_router(tasks.router)
app.include_router(index.router)
app.include_router(clients.router)


@app.exception_handler(exc.NoResultFound)
async def no_result_found_handler(request: fastapi.Request, exc: exc.NoResultFound):
    return fastapi.responses.JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'detail': 'Сущность с указанным ID не существует'}
    )

if __name__ == '__main__':
    uvicorn.run(app='src.main:app', reload=True)
