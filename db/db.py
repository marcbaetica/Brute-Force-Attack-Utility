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

    def create_table(self, table):
        with self.connection as con:
            con.execute(f"""
                CREATE TABLE {table.upper()} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                );
            """)
        self.tables.append(table.upper())

    def read_all_entries_from_table(self, table):
        if len(self.tables) == 0:
            print('There are no tables to read from at this time.')
            return
        if table.upper() not in self.tables:
            print(f'Table {table.upper()} was not found in the list of existing db tables: {self.tables}')
            return
        with self.connection as con:
            data = con.execute(f"""
                SELECT * FROM {table};
            """)
        return data

    def list_all_tables(self):
        with self.connection as con:
            return con.execute(f"""
                SELECT * FROM sqlite_master WHERE type='table';
            """)

    def insert_into_table(self, table, identifier, name, age):
        if table.upper() not in self.tables:
            print(f'Table {table.upper()} was not found in the list of existing db tables: {self.tables}')
            return
        with self.connection as con:
            con.execute(f"""
                INSERT INTO {table} (id, name, age) VALUES ({identifier}, '{name}', {age});
            """)
        # print(?)

    def delete_table(self, table):
        table = table.upper()
        with self.connection as con:
            con.execute(f"""
                DROP TABLE {table};
            """)
        # if above is successful
        self.tables.remove(table)
        print(f'Removed {table} from db {self.name}. Remaining tables: {self.tables}')

    def delete_db(self, db):
        if self.connection:
            self.connection.close()  # Otherwise os system call will fail
        os.remove(db)
        remaining_dbs = [file for file in os.listdir() if '.db' in file]
        if remaining_dbs:
            print(f'Databases remaining: {remaining_dbs}')
