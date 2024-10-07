from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# User = get_user_model()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name


class Ice_recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    ice_name = models.CharField(max_length=100)
    ice_discription = models.TextField()
    ice_image = models.ImageField(upload_to="ice_cream_pictures")


# Different model example

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    # This is basically for sorting the department name in order.
    class Meta:
        ordering = ['department']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
    class Meta:
        ordering = ['student_id']


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class Student(models.Model):
    department = models.ForeignKey(
        Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(
        StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        # verbose_name = "student"


class Subject_marks(models.Model):
    student = models.ForeignKey(
        Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
        unique_together = ['student', 'subject']


# class CustomUser(AbstractUser):
#     username = None
#     phone_number = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     user_bio = models.CharField(max_length=50)
#     user_profile_img = models.ImageField(upload_to="profile")

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = [] 