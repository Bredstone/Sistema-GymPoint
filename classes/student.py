from classes.user import User
from datetime import datetime, date

class Student(User):
  def __init__(self, name, cpf, email, 
               password, phone, cep, 
               number, birth_date, blood_type,
               weight, height, gender, objective,
               user_id=None, emergency_phone=None, user_type='Student',
               body_fat=None, observations=None):
    super().__init__(name, cpf, email, password, phone, cep, number, user_id, emergency_phone, user_type)

    if birth_date == '' or blood_type == '' or weight == '' or height == '' or gender == '' or objective == '':
      raise Exception('Valores vazios não são permitidos!')

    try:
      datetime.strptime(birth_date, '%d/%m/%Y').date()
    except:
      raise Exception('Data de nascimento inválida!')

    if blood_type not in ['A +', 'A -', 'B +', 'B -', 'AB +', 'AB -', 'O +', 'O -']:
      raise Exception('Tipo sanguíneo inválido!')

    try:
      self.weight = float(str(weight).replace(',', '.'))
      if self.weight == 0:
        raise Exception()
    except:
      raise Exception('Peso inválido!')
    
    try:
      self.height = float(str(height).replace(',', '.'))
      if self.height == 0:
        raise Exception()
    except:
      raise Exception('Altura inválida!')

    if gender != 'Masculino' and gender != 'Feminino':
      raise Exception('Sexo inválido!')

    if body_fat:
      try:
        self.body_fat = float(str(body_fat).replace('%', '').replace(',', '.'))
        if self.body_fat == 0:
          raise Exception()
      except:
        raise Exception('Body Fat inválido!')
    else:
      self.body_fat = body_fat

    self.birth_date = birth_date
    self.blood_type = blood_type
    self.gender = gender
    self.objective = objective
    self.observations = observations

  @staticmethod
  def getAge(birth_date):
    today = date.today()
    born = datetime.strptime(birth_date, '%d/%m/%Y').date()
    
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))