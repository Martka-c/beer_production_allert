from datetime import datetime
import sqlite3

import mysql.connector

from dictionary import RANGES, MESSAGES


class InputDatabase:

    def __init__(self, login: str, password: str):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user=login,
            password=password,
        )
        self.cursor = self.db.cursor(buffered=True)
        self.start_creating_dbs_if_not_exist()

    def drop_db(self):
        query = "DROP DATABASE main_database"
        self.cursor.execute(query)

    def start_creating_dbs_if_not_exist(self):
        self.create_db_if_not_exist()
        self.select_db()
        self.create_tables()

    def create_db_if_not_exist(self):
        try:
            query = "CREATE DATABASE IF NOT EXISTS main_database;"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating database: {ex}")

    def create_tables(self):
        self.create_all_alarms_table()
        self.create_users_table()

    def create_all_alarms_table(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS alarms(id int NOT NULL AUTO_INCREMENT, alert_type TEXT, alert_range 
            TEXT, time DATETIME, supervisor_name TEXT, PRIMARY KEY (id));"""
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating alarms table: {ex}")

    def create_users_table(self):
        """
        Creates table that contains registered users
        """
        try:
            query = "Create TABLE IF NOT EXISTS users(login TEXT, password TEXT)"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating table users: {ex}")

    def select_db(self):
        try:
            query = "USE main_database"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error: cannot use main_database\n{ex}")

    def raise_allert(self, allert_content: str, user: str):
        try:
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(date_time)
            # datatime field format YYYY-MM-DD hh:mm:ss
            query = f"INSERT INTO alarms(alert_type, alert_range, time, supervisor_name) " \
                    f"VALUES ('{allert_content}', '{RANGES[MESSAGES[allert_content]]}', '{date_time}', '{user}')"
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.OperationalError as ex:
            raise RuntimeError(ex)

    def check_user(self, userek: str, passwordek: str):
        try:
            self.cursor.execute(f"SELECT password FROM users WHERE login='{userek}'")
            row = self.cursor.fetchone()
            return True if row and row[0] == passwordek else False
        except sqlite3.OperationalError as ex:
            raise RuntimeError(ex)

if __name__ == '__main__':
    db = InputDatabase("root", "")