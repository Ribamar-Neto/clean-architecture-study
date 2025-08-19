import pytest
from src.settings.db import DBConnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handler = DBConnectionHandler()

    engine = db_connection_handler.create_database_engine()

    assert engine is not None
