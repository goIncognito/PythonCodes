import pytest
from db.db_client import DatabaseClient

@pytest.fixture
def db_client():
    db = DatabaseClient(
        host="localhost",
        user="root",
        password="password",
        db="testdb"
    )
    yield db
    db.close()
