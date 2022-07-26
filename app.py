from controllers.students import getStudentsList, validateStudent, insertStudent, getStudent, removeStudent
from classes.student import Student
from controllers.plans import getPlansList, validatePlan, insertPlan, getPlan, removePlan
from classes.plan import Plan
from controllers.trainers import getTrainersList
from classes.trainer import Trainer
from controllers.receptionists import getReceptionistsList
from classes.receptionist import Receptionist

from flask import Flask, render_template, request, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'O rato roeu a roupa do rei de Roma'

@app.route('/sign', methods=['GET', 'POST'])
def sign():
  return render_template('sign.html')

@app.route('/students')
def students():
  return render_template('Students/students.html', students=getStudentsList(), getAge=Student.getAge)

@app.route('/create-student', methods=['GET', 'POST'])
def createStudent():
  if request.method == 'POST':
    try:
      student = validateStudent(request.form)

      insertStudent(student)
      flash('Aluno cadastrado com sucesso!', 'success')
      return redirect('/students')
    except Exception as e:
      flash(e, 'error')

  return render_template('Students/create-student.html')

@app.route('/delete-student/<int:student_id>', methods=['GET', 'POST'])
def deleteStudent(student_id):
  student = getStudent(student_id)

  if not student:
    abort(404)
  else:
    removeStudent(student_id)
    flash('{} foi excluído com sucesso!'.format(student.name), 'success')
    return redirect('/students')

@app.route('/plans')
def plans():
  return render_template('Plans/plans.html', plans=getPlansList(), formatPrice=Plan.formatPrice)

@app.route('/create-plan', methods=['GET', 'POST'])
def createPlan():
  if request.method == 'POST':
    try:
      plan = validatePlan(request.form)

      insertPlan(plan)
      flash('Plano cadastrado com sucesso!', 'success')
      return redirect('/plans')
    except Exception as e:
      flash(e, 'error')

  return render_template('Plans/create-plan.html')

@app.route('/delete-plan/<int:plan_id>', methods=['GET', 'POST'])
def deletePlan(plan_id):
  plan = getPlan(plan_id)

  if not plan:
    abort(404)
  else:
    removePlan(plan_id)
    flash('{} foi excluído com sucesso!'.format(plan.title), 'success')
    return redirect('/plans')

@app.route('/registrations')
def registrations():
  return render_template('Registrations/registrations.html')

@app.route('/create-registration')
def createRegistration():
  return render_template('Registrations/create-registration.html')

@app.route('/trainers')
def trainers():
  return render_template('Trainers/trainers.html', trainers=getTrainersList(), formatHours=Trainer.formatHours)

@app.route('/create-trainer')
def createTrainer():
  return render_template('Trainers/create-trainer.html')

@app.route('/receptionists')
def receptionists():
  return render_template('Receptionists/receptionists.html', receptionists=getReceptionistsList(), formatHours=Receptionist.formatHours)

@app.route('/receptionist-profile')
def recepcionistProfile():
  return render_template('Receptionists/profile.html')

@app.route('/create-receptionist')
def createReceptionist():
  return render_template('Receptionists/create-receptionist.html')

@app.route('/student-profile')
def StudentProfile():
  return render_template('Students/profile.html')
