# Python Training - Week 4

## Task 1: Advanced Python OOP Features

### Objective

Implement advanced Python class features including: 
- Static Methods 
- Class Methods 
- Properties 
- Special (Dunder) Methods

------------------------------------------------------------------------

## Implemented Features

### 1️⃣ Student Class

**Includes:**

-   `@staticmethod`
    -   `is_valid_id()` → Validates student ID format.
-   `@classmethod`
    -   `from_csv()` → Alternative constructor to create a Student from
        CSV string.
-   `@property`
    -   `gpa` → Automatically calculated from student grades (0--4
        scale).
-   `__eq__`
    -   Students are considered equal if their `student_id` is the same.

------------------------------------------------------------------------

### 2️⃣ Course Class

**Includes:**

-   `__len__`
    -   Enables: `len(course)`
-   `__iter__`
    -   Enables:

        ``` python
        for student in course:
            print(student.name)
        ```
-   Prevents duplicate students based on ID.

------------------------------------------------------------------------

## Example Usage

``` python
s1 = Student("S1001", "Ahmad")
s1.add_grade("Math", 90)
print(s1.gpa)

course = Course("AI-101")
course.add_student(s1)

for student in course:
    print(student.name)
```

------------------------------------------------------------------------

## How to Run

``` bash
python task1.py
```

------------------------------------------------------------------------

## Learning Outcomes

✔ Understanding difference between static & class methods\
✔ Using @property for computed attributes\
✔ Implementing iterable objects\
✔ Overriding equality comparison

------------------------------------------------------------------------

**Status:** Completed ✅
