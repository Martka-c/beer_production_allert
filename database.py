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
        self.db.commit()

        #query = "DROP DATABASE IF EXISTS bazka"
        #self.cursor.execute(query)

        #query = "CREATE DATABASE bazka"
        #self.cursor.execute(query)

        #query = 'USE bazka'
        #self.cursor.execute(query)

        #query = """CREATE TABLE ok(id INT(6), firstname VARCHAR(30) NOT NULL, lastname VARCHAR(30) NOT NULL,
        #email VARCHAR(50)) """
        #self.cursor.execute(query)

        #query = "INSERT INTO ok(id, firstname, lastname, email) VALUES (1, 'HEJKA', 'sdfxf', 'ok')"
        #self.cursor.execute(query)

        #query = "SELECT firstname FROM ok WHERE id=1"
        #self.cursor.execute(query)
        #row = self.cursor.fetchone()
        #print(row[0])

        #query = "SELECT * FROM ok"
        #self.cursor.execute(query)
        #row = self.cursor.fetchone()
        #print(row)

        #self.db.commit()

        #self.create_db_if_not_exist()

    def start_creating_dbs_if_not_exist(self):
        self.create_db_if_not_exist()
        self.select_db()
        self.create_tables()

    def create_db_if_not_exist(self):
        query = "CREATE DATABASE IF NOT EXISTS main_database;"
        self.cursor.execute(query)

    def create_tables(self):
        self.create_all_alarms_table()
        self.create_alarm_types_table()
        self.create_alarms_priority_table()
        self.create_users_table()

    def create_all_alarms_table(self):
        query = "CREATE TABLE IF NOT EXISTS alarms(id INTEGER(6), alert_name TEXT, alert_type TEXT, alert_range_TEXT, time TIMESTAMP, supervisor_name TEXT);"
        self.cursor.execute(query)

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
        query = "CREATE TABLE IF NOT EXISTS alarm_types(id_type TEXT, type TEXT );"
        self.cursor.execute(query)

    def create_alarms_priority_table(self):
        """
        Priorytety alarmów powinny obejmować:
        - alarm krytyczny
        - alarm o zagrożeniu
        - alarm ostrzegawczy
        """
        query = "CREATE TABLE IF NOT EXISTS priority_table(id_priority, priority TEXT)"
        self.cursor.execute(query)

    def create_users_table(self):
        """
        Creates table that contains registered users
        """
        query = "Create TABLE IF NOT EXISTS users(login TEXT, password TEXT)"
        self.cursor.execute(query)

    def fill_tables(self):
        query = "INSERT INTO priority_table(id_priority, priority) VALUES (1, 'Normal'), (2,'Urgent'), (3, 'Critical')"
        self.cursor.execute(query)

    def select_db(self):
        query = "USE main_database"
        self.cursor.execute(query)
