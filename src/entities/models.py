import datetime

import sqlalchemy as sa
from sqlalchemy import orm


class Base(orm.DeclarativeBase):
    pass


class BaseWithId(Base):
    __abstract__ = True

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)


class Task(BaseWithId):
    __tablename__ = 'tasks'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    client_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('clients.id'), nullable=False)
    title: orm.Mapped[str] = orm.mapped_column(sa.String(100), nullable=False)
    description: orm.Mapped[str | None] = orm.mapped_column(sa.Text)
    is_completed: orm.Mapped[bool] = orm.mapped_column(
        nullable=False, default=False)
    created_at: orm.Mapped[datetime.datetime] = orm.mapped_column(
        nullable=False, server_default=sa.func.now())
    updated_at: orm.Mapped[datetime.datetime] = orm.mapped_column(
        nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    
    client: orm.Mapped[Client] = orm.relationship(back_populates='tasks')


class Client(BaseWithId):
    __tablename__ = 'clients'
    
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(100), nullable=False)
    surname: orm.Mapped[str] = orm.mapped_column(sa.String(100), nullable=False)
    patronymic: orm.Mapped[str | None] = orm.mapped_column(sa.String(100))
    created_at: orm.Mapped[datetime.datetime] = orm.mapped_column(
        nullable=False, server_default=sa.func.now())
    updated_at: orm.Mapped[datetime.datetime] = orm.mapped_column(
        nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    
    tasks: orm.Mapped[list[Task]] = orm.relationship(back_populates='client')