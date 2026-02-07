from src.components import unit_of_work


class BaseService:
    def __init__(self, uow: unit_of_work.BaseUnitOfWork) -> None:
        self.uow = uow
