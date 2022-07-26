import sqlite3

def get_db_cursor():
  connection = sqlite3.connect('database.db', isolation_level=None)
  connection.row_factory = sqlite3.Row

  return connection.cursor()