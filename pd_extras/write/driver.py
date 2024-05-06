from enum import Enum, auto


class SQLDatabases(Enum):
    MYSQL = auto()
    POSTGRES = auto()
    SQLSERVER = auto()


class NoSQLDatabases(Enum):
    MONGO = auto()
