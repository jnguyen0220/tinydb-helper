import pytest
from tinydb_helper.helper import Table
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

TABLE = "project"
ID = "1"


@pytest.fixture
def table():
    db = TinyDB(storage=MemoryStorage)
    return Table(db=db, table=TABLE)


def test_all(table):
    table.insert(item=dict(), id=id)
    assert len(table.all()) == 1


def test_insert(table):
    created_id = table.insert(item=dict(), id=ID)
    assert ID == created_id


def test_update(table):
    table.insert(item=dict(), id=ID)
    update_id = table.update(id=ID, item=dict())
    assert ID == update_id


def test_delete(table):
    table.insert(item=dict(), id=ID)
    delete_id = table.delete(id=ID)
    assert ID == delete_id


def test_find(table):
    table.insert(item=dict(), id=ID)
    found = table.find(id=ID)
    assert found is not None
