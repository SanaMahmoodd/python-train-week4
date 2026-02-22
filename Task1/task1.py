from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Iterator


@dataclass
class Student:
    student_id: str
    name: str
    grades: Dict[str, float] = field(default_factory=dict)  # {"Math": 88, "AI": 93}

    @staticmethod
    def is_valid_id(student_id: str) -> bool:
        """Static helper: no self/cls needed."""
        return isinstance(student_id, str) and student_id.strip() != ""

    @classmethod
    def from_csv(cls, line: str) -> "Student":
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            raise ValueError("CSV must have at least: id,name")

        student_id, name = parts[0], parts[1]
        grades: Dict[str, float] = {}

        if len(parts) >= 3 and parts[2]:
            items = parts[2].split(";")
            for item in items:
                if "=" in item:
                    course, grade = item.split("=")
                    grades[course.strip()] = float(grade.strip())

        return cls(student_id=student_id, name=name, grades=grades)

    def add_grade(self, course_name: str, grade: float) -> None:
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self.grades[course_name] = grade

    @property
    def gpa(self) -> float:
    #Auto-calculated GPA from grades, Simple mapping: 0-100 -> 0-4 scale.
        if not self.grades:
            return 0.0

        avg = sum(self.grades.values()) / len(self.grades)
        # Convert average percentage to 4.0 scale
        gpa = (avg / 100) * 4
        return round(gpa, 2)

    def __eq__(self, other: object) -> bool:
        #Equality based on ID.
        if not isinstance(other, Student):
            return NotImplemented
        return self.student_id == other.student_id


class Course:
    def __init__(self, course_name: str) -> None:
        self.course_name = course_name
        self._students: List[Student] = []

    def add_student(self, student: Student) -> None:
        # prevent duplicates by ID
        if student in self._students:
            raise ValueError(f"Student with id {student.student_id} already in course.")
        self._students.append(student)

    def __len__(self) -> int:
        #Allows len(course).
        return len(self._students)

    def __iter__(self) -> Iterator[Student]:
        #Allows: for student in course:
        return iter(self._students)

    def __repr__(self) -> str:
        return f"Course(name={self.course_name!r}, students={len(self)})"


if __name__ == "__main__":
    # Demo
    s1 = Student("S1001", "Ahmad")
    s1.add_grade("Math", 90)
    s1.add_grade("AI", 80)

    s2 = Student.from_csv("S1002, Sara, Math=95;AI=90")
    s3 = Student("S1001", "SomeoneElse")  # same ID as s1

    print("s1 GPA:", s1.gpa)
    print("s2 GPA:", s2.gpa)
    print("s1 == s3 ?", s1 == s3)

    course = Course("AI-101")
    course.add_student(s1)
    course.add_student(s2)

    print(course)
    print("len(course):", len(course))

    for st in course:
        print(st.student_id, st.name, st.gpa)
