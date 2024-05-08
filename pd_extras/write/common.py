"""Common variables for dataframe to database module"""

from pd_extras.write.driver import SQLDatabaseType

META_INFO_QUERIES = {
    SQLDatabaseType.SQLSERVER.value: {
        "dialect": "mssql",
        "driver": "+pymssql",
        "query": {
            "db_list": "SELECT name FROM master.sys.databases;",
            "table_list": """SELECT TABLE_NAME FROM
                INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND
                TABLE_CATALOG=%s;""",
            "column_info": """SELECT * FROM
                information_schema.columns WHERE TABLE_CATALOG='%s' AND
                TABLE_SCHEMA = 'dbo' AND TABLE_NAME = '%s';""",
        },
    },
    SQLDatabaseType.MYSQL.value: {
        "dialect": "mysql",
        "driver": "+mysqldb",
        "query": {
            "db_list": "SHOW DATABASES;",
            "table_list": """SHOW TABLES FROM %s""",
            "column_info": """SELECT *
                from information_schema.columns
                WHERE table_schema='%s' and table_name='%s';""",
        },
    },
    SQLDatabaseType.POSTGRES.value: {
        "dialect": "postgresql",
        "driver": "+psycopg2",
        "query": {
            "db_list": "select datname from pg_database;",
            "table_list": "select * from pg_catalog.pg_tables where schemaname=%s;",
            "column_info": """select * from information_schema.columns WHERE
                table_catalog='%s' and table_name='%s';""",
        },
    },
}
nosql_dbtypes = ["mongo"]
