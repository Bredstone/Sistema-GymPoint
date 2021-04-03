from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
  return render_template('Users/users.html')

@app.route('/create-user')
def createUser():
  return render_template('Users/create-user.html')

@app.route('/plans')
def plans():
  return render_template('Plans/plans.html')

@app.route('/create-plan')
def createPlan():
  return render_template('Plans/create-plan.html')

@app.route('/registrations')
def registrations():
  return render_template('Registrations/registrations.html')

@app.route('/create-registration')
def createRegistration():
  return render_template('Registrations/create-registration.html')

@app.route('/trainers')
def trainers():
  return render_template('Trainers/trainers.html')

@app.route('/create-trainer')
def createTrainer():
  return render_template('Trainers/create-trainer.html')

@app.route('/receptionists')
def receptionists():
  return render_template('Receptionists/receptionists.html')

@app.route('/create-receptionist')
def createReceptionist():
  return render_template('Receptionists/create-receptionist.html')

@app.route('/sign')
def sign():
  return render_template('sign.html')
