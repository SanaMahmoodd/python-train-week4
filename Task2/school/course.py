from __future__ import annotations
from typing import Iterator, List
from .student import Student


class Course:
    def __init__(self, course_name: str) -> None:
        self.course_name = course_name
        self._students: List[Student] = []

    def add_student(self, student: Student) -> None:
        if student in self._students:
            raise ValueError(f"Student with id {student.student_id} already in course.")
        self._students.append(student)

    def __len__(self) -> int:
        return len(self._students)

    def __iter__(self) -> Iterator[Student]:
        return iter(self._students)

    def __repr__(self) -> str:
        return f"Course(name={self.course_name!r}, students={len(self)})"
