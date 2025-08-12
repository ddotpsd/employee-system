def remove_employee(employee, name):
    if name in employee:
        employee.remove(name)
    return employee