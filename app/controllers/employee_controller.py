from app.models.employee_model import (
    get_all_employees,
    get_employee,
    add_employee,
    update_employee,
    delete_employee,
)

def list_employees():
    return get_all_employees()

def show_employee(id):
    return get_employee(id)

def create_employee(name, department):
    return add_employee(name, department)

def edit_employee(id, name, department):
    return update_employee(id, name, department)

def remove_employee(id):
    return delete_employee(id)
