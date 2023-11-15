# 11-3 Employee
import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    return Employee('John', 'Doe', 50_000)

def test_give_default_raise(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 55_000

def test_give_custom_raise(employee_instance):
    employee_instance.give_raise(7_000)
    assert employee_instance.annual_salary == 57_000