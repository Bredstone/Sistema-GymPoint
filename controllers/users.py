from database.config import get_db_cursor

def validateUser(user):
  cur = get_db_cursor()

  cur.execute('SELECT id FROM Users WHERE cpf = ?', (user['cpf'], ))
  cpfRes = cur.fetchone()
  cur.execute('SELECT id FROM Users WHERE email = ?', (user['email'], ))
  emailRes = cur.fetchone()

  cur.close()

  if cpfRes:
    raise Exception('CPF já cadastrado!')
  if emailRes:
    raise Exception('Email já cadastrado!')
  if user['password'] != user['confirm-password']:
    raise Exception('As senhas informadas não são iguais!')