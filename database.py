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
        self.create_default_user()

    def drop_db(self):
        query = "DROP DATABASE main_database"
        self.cursor.execute(query)

    def create_default_user(self):
        query = "INSERT INTO users(login, password) VALUES ('login', 'haslo'), ('default', 'default')"
        self.cursor.execute(query)
        self.db.commit()

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

    def get_all_from_db(self):
        try:
            query = "SELECT * FROM alarms"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [row for row in rows]
        except sqlite3.OperationalError as ex:
            raise RuntimeError(ex)

    def prepare_query(self, time_range, supervisor, priority, days: int = None):

        query = "SELECT * FROM alarms A"

        if time_range == 1:
            query += " WHERE time > DATE_SUB(CURDATE(), INTERVAL 1 DAY)"
        elif time_range == 2:
            query += " WHERE time > DATE_SUB(CURDATE(), INTERVAL 7 DAY)"
        elif time_range == 3:
            query += " WHERE time > DATE_SUB(CURDATE(), INTERVAL 30 DAY)"
        else:
            query += f" WHERE time > DATE_SUB(CURDATE(), INTERVAL {days} DAY)"

        if supervisor:
            query += f" AND  supervisor_name = '{supervisor}'"
        if priority:
            query += f" AND alert_range = '{priority}'"

        return query

    def get_users_list(self):
        try:
            query = "SELECT DISTINCT(login) FROM users"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [row[0] for row in rows]
        except sqlite3.OperationalError as ex:
            raise RuntimeError(ex)
