from validate_docbr import CPF
from email_validator import validate_email
import pycep_correios

class User():
  def __init__(self, name, cpf, email, 
               password, phone, cep, 
               street_number, 
               user_id=None, phone_alt=None, user_type='Student'):
    if name == '' or cpf == '' or email == '' or phone == '' or cep == '' or street_number == '':
      raise Exception('Valores vazios não são permitidos!')

    cpfCheck = CPF()
    if not cpfCheck.validate(cpf):
      raise Exception('CPF inválido!')
    
    try:
      validate_email(email)
    except:
      raise Exception('Email inválido!')

    try:
      pycep_correios.get_address_from_cep(cep)
    except:
      raise Exception('CEP inválido!')

    try:
      self.street_number = int(street_number)
    except:
      raise Exception('Número da rua inválido!')

    self.id = user_id
    self.name = name
    self.cpf = cpf
    self.email = email
    self.password = password
    self.phone = phone
    self.phone_alt = phone_alt
    self.cep = cep
    self.user_type = user_type