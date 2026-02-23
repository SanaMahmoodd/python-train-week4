from school import Student
from school.management import SchoolManager


def test_add_and_get_student():
    mgr = SchoolManager()
    s = Student("S1", "Sana")
    mgr.add_student(s)

    got = mgr.get_student("S1")
    assert got is not None
    assert got.name == "Sana"


def test_gpa_property():
    s = Student("S2", "Ahmad")
    s.add_grade("Math", 100)
    s.add_grade("AI", 50)
    assert s.gpa == 3.0
