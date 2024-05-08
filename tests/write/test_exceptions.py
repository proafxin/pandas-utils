import os

import pytest

from pd_extras.write.driver import SQLDatabaseType
from pd_extras.write.nosql_writer import NoSQLDatabaseWriter
from pd_extras.write.sql_writer import SQLDatabaseWriter


def test_wrong_dbtype() -> None:
    with pytest.raises(KeyError):
        _ = NoSQLDatabaseWriter(
            dbtype="notmongo",
            host=os.environ["MONGO_HOST"],
            dbname="test",
            user=os.environ["MONGO_USER"],
            password=os.environ["MONGO_PASSWORD"],
            port=int(os.environ["MONGO_PORT"]),
        )


def test_db_create() -> None:
    with pytest.raises(ValueError):
        SQLDatabaseWriter(
            dbtype=SQLDatabaseType.MYSQL,
            host=os.environ["MYSQL_HOST"],
            dbname="",
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            port=os.environ["MYSQL_PORT"],
        )
