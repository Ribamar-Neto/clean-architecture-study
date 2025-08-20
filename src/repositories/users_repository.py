from src.settings.db.connection import DBConnectionHandler
from src.schemas import UsersInputSchema

class UsersRepository:
    
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age:int) -> None:
        with DBConnectionHandler() as db:
            try:
                new_register = UsersInputSchema(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                db.session.add(new_register)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
