"""Module services excel files, generates report dependent on set parameters"""
import sqlite3
from pythonlangutil.overload import Overload, signature

import pandas as pd


class ReportGenerator:
	def start(self, db, cursor, time: int = None, supervisor: str = None, level: str = None, days: int=None):
		"""
		Class generates report based on given informations
		:param db:
		:param alarm_type:
		:param time:
		:param supervisor:
		:param level:
		"""
		rows = self.get_proper_rows(db, cursor, time, supervisor, level, days)
		id = [row[0] for row in rows]
		types = [row[1] for row in rows]
		ranges = [row[2] for row in rows]
		time = [str(row[3]) for row in rows]
		supervisor_names = [row[4] for row in rows]

		self.generate(id, types, ranges, time, supervisor_names)

	def get_proper_rows(self, db, cursor, time_range, supervisor=None, level=None, days=None):
		query = db.prepare_query(time_range, supervisor, level, days)
		try:
			cursor.execute(query)
			rows = cursor.fetchall()
			print(query)
			return [row for row in rows]
		except sqlite3.OperationalError as ex:
			raise RuntimeError(ex)

	def generate(self, id, types, ranges, time, supervisor_names):
		df =pd.DataFrame({'Id': id, 'Rodzaj alarmu': types, "Priorytet": ranges,
						  "Czas zdarzenia": time, "Kierownik": supervisor_names})
		writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
		df.to_excel(writer, sheet_name="Alarmy1", index=False)
		worksheet = writer.sheets['Alarmy1']
		worksheet.conditional_format('B2:B100', {'type': '2_color_scale'})
		writer.close()
