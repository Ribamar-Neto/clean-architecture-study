from src.schemas import UsersInputSchema
from src.settings.db.connection import DBConnectionHandler


class UsersRepository:
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as db:
            try:
                new_register = UsersInputSchema(first_name=first_name, last_name=last_name, age=age)
                db.session.add(new_register)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str, last_name: str, age: int) -> any:
        with DBConnectionHandler() as db:
            try:
                users = (
                    db.session.query(UsersInputSchema)
                    .filter(UsersInputSchema.first_name == first_name)
                    .filter(UsersInputSchema.last_name == last_name)
                    .filter(UsersInputSchema.age == age)
                    .all()
                )

                return users
            except Exception as exception:
                db.session.rollback()
                raise exception
