from app import engine
from sqlalchemy import text

def row_to_dict(row):
    return dict(row._mapping) if row else None

def get_all_employees():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM employee"))
        return [row_to_dict(row) for row in result]

def get_employee(id):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM employee WHERE id = :id"), {"id": id})
        return row_to_dict(result.fetchone())

def add_employee(name, department):
    with engine.connect() as connection:
        connection.execute(
            text("INSERT INTO employee (name, department) VALUES (:name, :department)"),
            {"name": name, "department": department}
        )
        connection.commit()

def update_employee(id, name, department):
    with engine.connect() as connection:
        connection.execute(
            text("UPDATE employee SET name = :name, department = :department WHERE id = :id"),
            {"id": id, "name": name, "department": department}
        )
        connection.commit()

def delete_employee(id):
    with engine.connect() as connection:
        connection.execute(
            text("DELETE FROM employee WHERE id = :id"),
            {"id": id}
        )
        connection.commit()
