import os
import sqlite3 as sl


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = self._create_db()
        self.tables = []

    def _create_db(self):
        connection = sl.connect(self.name)
        return connection

    def query(self, query):
        with self.connection as con:
            return con.execute(query)

    def create_table(self, table):
        self._drop_table_if_exists(table)
        query = f"""
                CREATE TABLE {table} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT
                );
                """
        self.query(query)
        self.tables.append(table)

    def _drop_table_if_exists(self, table):
        query = f'DROP TABLE IF EXISTS {table};'
        self.query(query)

    def read_all_entries_from_table(self, table):
        if len(self.tables) == 0:
            print('There are no tables to read from at this time.')
            return
        if table not in self.tables:
            print(f'Table {table} was not found in the list of existing db tables: {self.tables}')
            return
        with self.connection as con:
            data = con.execute(f'SELECT * FROM {table};')
        return data

    def list_all_tables(self):
        with self.connection as con:
            return con.execute(f'SELECT * FROM sqlite_master WHERE type="table";')

    def insert_into_table(self, table, identifier, username, password):
        if table not in self.tables:
            print(f'Table {table} was not found in the list of existing db tables: {self.tables}')
            return
        with self.connection as con:
            con.execute(f'INSERT INTO {table} (id, username, password) VALUES ({identifier}, "{username}", "{password}");')
        # print(?)

    def list_table_columns(self, table):
        with self.connection as con:
            table_columns = con.execute(f'PRAGMA table_info([{table}]);')
            for column in table_columns:
                print(column)

    def delete_table(self, table):
        table = table
        with self.connection as con:
            con.execute(f'DROP TABLE {table};')
        # if above is successful
        self.tables.remove(table)
        print(f'Removed {table} from db {self.name}. Remaining tables: {self.tables}')

    def delete_db(self, db):
        if self.connection:
            self.connection.close()  # Otherwise os system call will fail as file is in use.
        os.remove(db)
        remaining_dbs = [file for file in os.listdir() if '.db' in file]
        if remaining_dbs:
            print(f'Databases remaining: {remaining_dbs}')
