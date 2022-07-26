import locale

class Plan():
  def __init__(self, title, duration, price, plan_id=None):
    if duration == 0 or price == 0:
      raise Exception('Valores inválidos!')

    self.title = title
    self.duration = duration
    self.price = price
    self.id = plan_id

  @staticmethod
  def formatPrice(price):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    return locale.currency(price).replace('$', '$ ')