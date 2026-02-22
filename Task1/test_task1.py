from task1 import Student, Course

def test_student_equality_by_id():
    a = Student("S1", "A")
    b = Student("S1", "B")
    assert a == b

def test_course_iterable_and_len():
    c = Course("X")
    c.add_student(Student("S1", "A"))
    c.add_student(Student("S2", "B"))
    assert len(c) == 2
    ids = [s.student_id for s in c]
    assert ids == ["S1", "S2"]

def test_gpa_auto_calculated():
    s = Student("S9", "Test")
    s.add_grade("Math", 100)
    s.add_grade("AI", 50)
    assert s.gpa == 3.0  # avg=75 => 3.0
