from database.config import get_db_cursor
from classes.plan import Plan

def getPlansList():
  cur = get_db_cursor()
  cur.execute('SELECT * FROM Plans ORDER BY duration')
  plans = cur.fetchall()
  cur.close()

  return plans

def validatePlan(plan):
  cur = get_db_cursor()
  cur.execute('SELECT id FROM Plans WHERE title = ?', (plan['title'], ))
  res = cur.fetchone()
  cur.close()

  if res:
    raise Exception('Plano já cadastrado!')
  
  try:
    price = float(plan['price'].replace('R$ ', '').replace('.', '').replace(',', '.'))
    duration = float(plan['duration'])
  except:
    raise Exception('Valores inválidos!')

  return Plan(plan['title'], duration, price)

def insertPlan(plan):
  cur = get_db_cursor()
  cur.execute('INSERT INTO Plans (title, duration, price) VALUES (?, ?, ?)',
              (plan.title, plan.duration, plan.price))
  cur.close()

def getPlan(plan_id):
  cur = get_db_cursor()
  cur.execute('SELECT * FROM Plans WHERE id = ?', (plan_id, ))
  res = cur.fetchone()
  cur.close()

  if res:
    return Plan(res['title'], res['duration'], res['price'], res['id'])
  else:
    return False

def removePlan(plan_id):
  cur = get_db_cursor()
  cur.execute('DELETE FROM Plans WHERE id = ?', (plan_id, ))
  cur.close()