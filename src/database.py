from server import FTPServer
import json
import pyodbc


class AccessDB:
	"""docstring for AccessDB"""
	def __init__(self, file):
		self.conn = self.__open(file)

	def __open(self, file):
		return pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % file)
		