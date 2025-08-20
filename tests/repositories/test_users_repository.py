from src.repositories import UsersRepository

def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 18

    users_repository = UsersRepository()
    users_repository.insert_user(
        first_name=mocked_first_name,
        last_name=mocked_last_name,
        age=mocked_age
    )
