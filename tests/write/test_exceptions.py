import os

import pytest

from pd_extras.write.nosql_writer import NoSQLDatabaseWriter


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
