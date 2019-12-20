import json
import pyodbc


class AccessDB:
    """docstring for AccessDB"""
    def __init__(self, file):
        self.config = self.__read_config('../conf/config.cfg')
        self.conn = self.__open(file)

    def __read_config(self, file):
        fh = open(file)
        return(json.load(fh)['database'])

    def __open(self, file):
        return pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % file)

    def get_rows_from_date(self, date):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM %s' % self.config['table'])
        return cursor.fetchall()
