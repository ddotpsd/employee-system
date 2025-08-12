from add_employee import add_employee
from remove_employee import remove_employee
from search_employee import search_employee

employee = []
employee = add_employee(employee, "Alice")
employee = add_employee(employee, "Bob")
employee = remove_employee(employee, "Alice")

print(search_employee(employee, "Bob"))
print(search_employee(employee, "Alice"))