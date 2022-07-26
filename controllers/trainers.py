from database.config import get_db_cursor

def getTrainersList():
  cur = get_db_cursor()
  cur.execute('SELECT Users.id, name, email, hour_start, hour_end, service_days FROM Users INNER JOIN Trainers ON Users.id = Trainers.id')
  trainers = cur.fetchall()
  cur.close()

  return trainers