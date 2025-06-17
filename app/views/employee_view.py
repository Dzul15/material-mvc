from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.employee_controller import (
    list_employees,
    show_employee,
    create_employee,
    edit_employee,
    remove_employee,
)

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/')
def index():
    employees = list_employees()
    return render_template('index.html', employees=employees)

@employee_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        create_employee(name, department)
        return redirect(url_for('employee.index'))
    return render_template('add.html')

@employee_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    employee = show_employee(id)
    if not employee:
        return redirect(url_for('employee.index'))
    
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        edit_employee(id, name, department)
        return redirect(url_for('employee.index'))

    return render_template('edit.html', employee=employee)

@employee_bp.route('/delete/<int:id>')
def delete(id):
    remove_employee(id)
    return redirect(url_for('employee.index'))
