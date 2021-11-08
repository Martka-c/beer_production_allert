import sqlite3

import mysql.connector


class InputDatabase:

    def __init__(self, login: str, password: str):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user=login,
            password=password,
        )
        self.cursor = self.db.cursor(buffered=True)

    def drop_db(self):
        query = "DROP DATABASE main_database"
        self.cursor.execute(query)

    def start(self):
        self.start_creating_dbs_if_not_exist()
        self.fill_priority_table_if_not_filled()

    def start_creating_dbs_if_not_exist(self):
        self.create_db_if_not_exist()
        self.select_db()
        self.drop_constant_tables()
        self.create_tables()

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
            query = """CREATE TABLE IF NOT EXISTS alarms(id INTEGER(6), alert_type TEXT, alert_range 
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

    def fill_alarm_types_table_if_not_filled(self):
        """
        Method checks if alarm types table contains any rows and if not - fill it.
        :return: Doesn't return anything
        """
#        if self.check_if_table_is_empty("alarm_types"):
        self.fill_alarm_types_table()

    def fill_alarm_types_table(self):
        try:
            query = """INSERT INTO alarm_types(id_type, type) VALUES (1, 'Brak jęczmienia w maszynie do zacierania'), (2,'Usterka w młynie'),
             (3, 'Usterka miksera do zacieru'), 
             (4, 'Brak cieczy w kadzi do gotowania'), 
             (5, 'Zbyt wysoka temperatura w zbiorniku do gotowania'), 
             (6, 'Pęknięta kadź do gotowania'), 
             (7, 'Uszkodzona uszczelka w chłodnicy (uszkodzona chłodnica)'),
             (8, 'Nieszczelny zamknięty fermentator stożkowy'),
             (9, 'W fermentatorze stożkowym znajduje się ciecz o zbyt wysokiej temperaturze (usterka chłodnicy)'),
             (10, 'Uszkodzony zbiornik pośredni'),
             (11, 'Pęknięta baryłka'),
             (12, 'Uszkodzony filtr do oczyszczania piwa'),
             (13, 'Zatkany filtr do oczyszczania piwa'),
             (14, 'Pęknięty zbiornik oczyszczonego piwa'),
             (15, 'Usterka pasteryzatora'),
             (16, 'Zbyt wysoka temperatura podczas pasteryzacji'),
             (17, 'Usterka maszyny pakującej'),
             (18, 'Elementy szkła na taśmie produkcyjnej'),
             """
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during filling alarm types table: {ex}")

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

    def fill_priority_table_if_not_filled(self):
        self.fill_priority_table()

    def fill_priority_table(self):
        try:
            query = "INSERT INTO priority_table(id_priority, priority) VALUES (1, 'Normal'), (2,'Urgent'), (3, 'Critical')"
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error during filling priority_table: {ex}")

    def select_db(self):
        try:
            query = "USE main_database"
            self.cursor.execute(query)
        except sqlite3.OperationalError as ex:
            raise RuntimeError(f"Error: cannot use main_database\n{ex}")

    def test_db(self):
        query = "SELECT * FROM priority_table"
        rows = self.cursor.execute(query).fetchall()
        print([row[0] for row in rows])

    def drop_constant_tables(self):
        query = "DROP TABLE priority_table"
        self.cursor.execute(query)
        self.db.commit()


if __name__ == '__main__':
    db = InputDatabase("root", "")
    db.start()
    #db.drop_db()