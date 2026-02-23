from __future__ import annotations
from typing import Dict, List, Optional
from .student import Student


class SchoolManager:
    def __init__(self) -> None:
        self._students: Dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        if student.student_id in self._students:
            raise ValueError("Student already exists.")
        self._students[student.student_id] = student

    def get_student(self, student_id: str) -> Optional[Student]:
        return self._students.get(student_id)

    def list_students(self) -> List[Student]:
        return list(self._students.values())
