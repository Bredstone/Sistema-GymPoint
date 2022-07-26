from classes.user import User

class Receptionist(User):
  def __init__(self, name, cpf, email, 
               password, phone, cep, 
               street_number, hour_start, hour_end,
               service_days,
               user_id=None, phone_alt=None, user_type='Receptionist'):
    super().__init__(name, cpf, email, password, phone, cep, street_number, user_id, phone_alt, user_type)
    self.hour_start = hour_start
    self.hour_end = hour_end
    self.service_days = service_days

  @staticmethod
  def formatHours(hour_start, hour_end):
    return str(hour_start)[0 : 5] + ' - ' + str(hour_end)[0 : 5]