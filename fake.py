from faker import Faker
import random
from home.models import *

fake = Faker()

def fake_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                Subject_marks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0, 100),
                )
    except Exception as e:
        print(e)

def fake_data(n=10) -> None:
    try:
        for i in range(n):
            departments_objs = Department.objects.all()
            random_index = random.randint(0, len(departments_objs)-1)

            department = departments_objs[random_index]
            student_id = f'STD-0{random.randint(100, 900)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 40)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )
    except Exception as a:
        print(a)