from database.config import get_db_cursor

def getReceptionistsList():
  cur = get_db_cursor()
  cur.execute('SELECT Users.id, name, email, hour_start, hour_end, service_days FROM Users INNER JOIN Receptionists ON Users.id = Receptionists.id')
  receptionists = cur.fetchall()
  cur.close()

  return receptionists