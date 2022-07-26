from database.config import get_db_cursor
from classes.student import Student
from controllers.users import validateUser

def getStudentsList():
  cur = get_db_cursor()
  cur.execute('SELECT Users.id, name, email, CPF, birth_date FROM Users INNER JOIN Students ON Users.id = Students.id')
  students = cur.fetchall()
  cur.close()

  return students

def validateStudent(student):
  validateUser(student)
  
  return Student(
    name=student['name'], 
    cpf=student['cpf'], 
    email=student['email'], 
    password=student['password'],
    phone=student['phone'],
    cep=student['cep'],
    number=student['number'],
    birth_date=student['birth-date'],
    blood_type=student['blood-type'],
    weight=student['weight'],
    height=student['height'],
    gender=student['gender'],
    objective=student['objective'],
    emergency_phone=student['emergency-phone'], 
    body_fat=student['body-fat'],
    observations=student['obs'])

def insertStudent(student):
  cur = get_db_cursor()
  cur.execute('INSERT INTO Users (name, CPF, email, password, phone, phone_alt, cep, street_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
              (student.name, student.cpf, student.email, student.password, student.phone, student.phone_alt, student.cep, student.street_number))
  cur.execute('INSERT INTO Students (id, birth_date, blood_type, weight, height, gender, objective, body_fat) VALUES ((SELECT id from Users WHERE email = ?), ?, ?, ?, ?, ?, ?, ?)',
              (student.email, student.birth_date, student.blood_type, student.weight, student.height, student.gender, student.objective, student.body_fat))
  cur.close()

def getStudent(student_id):
  cur = get_db_cursor()

  cur.execute('SELECT * FROM Users WHERE id = ?', (student_id, ))
  user = cur.fetchone()
  cur.execute('SELECT * FROM Students WHERE id = ?', (student_id, ))
  student = cur.fetchone()

  cur.close()

  if user and student:
    return Student(
      name=user['name'], 
      cpf=user['cpf'], 
      email=user['email'], 
      password=user['password'],
      phone=user['phone'],
      cep=user['cep'],
      number=user['street_number'],
      birth_date=student['birth_date'],
      blood_type=student['blood_type'],
      weight=student['weight'],
      height=student['height'],
      gender=student['gender'],
      objective=student['objective'],
      emergency_phone=user['phone_alt'], 
      body_fat=student['body_fat'],
      observations=student['observations'])
  else:
    return False

def removeStudent(student_id):
  cur = get_db_cursor()
  cur.execute('DELETE FROM Students WHERE id = ?', (student_id, ))
  cur.execute('DELETE FROM Users WHERE id = ?', (student_id, ))
  cur.close()