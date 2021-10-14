import sqlite3

import mysql.connector


class InputDatabase:

    def __init__(self, login: str, password: str):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user=login,
            password=password,
        )
        self.cursor = self.db.cursor()
        self.start_creating_dbs_if_not_exist()
        self.fill_tables()

    def start_creating_dbs_if_not_exist(self):
        self.create_db_if_not_exist()
        self.select_db()
        self.create_tables()
        self.db.commit()

    def create_db_if_not_exist(self):
        try:
            query = "CREATE DATABASE IF NOT EXISTS main_database;"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating database: {ex}")

    def create_tables(self):
        self.create_all_alarms_table()
        self.create_alarm_types_table()
        self.create_alarms_priority_table()
        self.create_users_table()

    def create_all_alarms_table(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS alarms(id INTEGER(6), alert_name TEXT, alert_type TEXT, alert_range 
            TEXT, time DATETIME, supervisor_name TEXT);"""
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating alarms table: {ex}")

    def create_alarm_types_table(self):
        """
        Alarm ma obejmować wydarzenia, dzięki którym coś może sie zdupcyć
        - przekroczenie temperatury przy ważeniu
        - stłuczenie butelki (elementy szkła w urządzeniu
        - nadmierne spienienie się płynu
        - brak butelki pod podajnikiem
        - brak cieczy w zbiorniku
        - zapłon elementu
        - odpadnięcie jakiegoś urządzenia
        - przepalenie się żarówki alarmowej
        """
        try:
            query = "CREATE TABLE IF NOT EXISTS alarm_types(id_type TEXT, type TEXT );"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating alarms_type table: {ex}")

    def create_alarms_priority_table(self):
        """
        Priorytety alarmów powinny obejmować:
        - alarm krytyczny
        - alarm o zagrożeniu
        - alarm ostrzegawczy
        """
        try:
            query = "CREATE TABLE IF NOT EXISTS priority_table(id_priority INTEGER(6), priority TEXT)"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating priority table: {ex}")

    def create_users_table(self):
        """
        Creates table that contains registered users
        """
        try:
            query = "Create TABLE IF NOT EXISTS users(login TEXT, password TEXT)"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during creating table users: {ex}")

    def fill_tables(self):
        try:
            query = "INSERT INTO priority_table(id_priority, priority) VALUES (1, 'Normal'), (2,'Urgent'), " \
                    "(3, 'Critical')"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during filling priority_table: {ex}")

    def select_db(self):
        try:
            query = "USE main_database"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error: cannot use main_database\n{ex}")
