from enum import Enum


class SQLDatabaseType(str, Enum):
    MYSQL = "mysql"
    POSTGRES = "postgresql"
    SQLSERVER = "sqlserver"


class NoSQLDatabaseType(str, Enum):
    MONGO = "mongo"
