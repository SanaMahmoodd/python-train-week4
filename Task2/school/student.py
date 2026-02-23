from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Student:
    student_id: str
    name: str
    grades: Dict[str, float] = field(default_factory=dict)

    @staticmethod
    def is_valid_id(student_id: str) -> bool:
        return isinstance(student_id, str) and student_id.strip() != ""

    def add_grade(self, course_name: str, grade: float) -> None:
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self.grades[course_name] = grade

    @property
    def gpa(self) -> float:
        if not self.grades:
            return 0.0
        avg = sum(self.grades.values()) / len(self.grades)
        return round((avg / 100) * 4, 2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.student_id == other.student_id
