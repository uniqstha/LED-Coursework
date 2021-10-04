import pytest


@pytest.mark.parametrize("username, password", [("admin", "admin"), ("admin", "Ram")])
def test_admin(username, password):
    assert username == password


@pytest.mark.parametrize("username, password", [("employee", "employee"), ("employee", "sita")])
def test_employe(username, password):
    assert username == password


@pytest.fixture()
def tester():
    FullName = "Unknown"
    Department = "Manager"
    Age = 10
    Gender = "Male"
    Contact = 9864239908
    Address = "Kathmandu"

    return [FullName, Department, Age, Gender, Contact, Address]


def testing_1(tester):
    first_name = "Unknown"
    assert tester[0] == first_name


def testing_2(tester):
    Depart = "Manager"
    assert tester[1] == Depart


def testing_3(tester):
    old = 21
    assert tester[2] == old


def testing_4(tester):
    sex = "Male"
    assert tester[3] == sex


def testing_5(tester):
    phone_no = 9864239908
    assert tester[4] == phone_no


def testing_6(tester):
    place = "Kathmandu"
    assert tester[5] == place