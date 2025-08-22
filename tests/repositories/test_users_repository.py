import pytest
from sqlalchemy import text

from src.repositories import UsersRepository
from src.settings.db import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 18

    users_repository = UsersRepository()
    users_repository.insert_user(
        first_name=mocked_first_name, last_name=mocked_last_name, age=mocked_age
    )

    sql = """
        SELECT * FROM users
        WHERE first_name = :first_name
        AND last_name = :last_name
        AND age = :age
    """
    response = connection.execute(
        text(sql), first_name=mocked_first_name, last_name=mocked_last_name, age=mocked_age
    )
    register = response.fetchall()[0]

    assert register.first_name == mocked_first_name
    assert register.last_name == mocked_last_name
    assert register.age == mocked_age

    connection.execute(
        text("""
        DELETE FROM users
        WHERE id = :id
    """),
        id=register.id,
    )

    connection.commit()
    connection.close()


def test_select_user():
    mocked_first_name = "first_2"
    mocked_last_name = "last_2"
    mocked_age = 20

    users_repository = UsersRepository()

    sql = """
        INSERT INTO users (first_name, last_name, age)
        VALUES (:first_name, :last_name, :age)
    """

    connection.execute(
        text(sql), first_name=mocked_first_name, last_name=mocked_last_name, age=mocked_age
    )
    connection.commit()

    result = users_repository.select_user(
        first_name=mocked_first_name, last_name=mocked_last_name, age=mocked_age
    )

    assert result[0].first_name == mocked_first_name
    assert result[0].last_name == mocked_last_name
    assert result[0].age == mocked_age

    connection.execute(
        text("""
        DELETE FROM users
        WHERE id = :id
    """),
        id=result[0].id,
    )
    connection.commit()
    connection.close()
