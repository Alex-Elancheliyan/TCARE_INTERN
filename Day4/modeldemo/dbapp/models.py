from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_rollno = models.IntegerField()
    student_total = models.IntegerField(max_length=10)

    #To Set Custom Table Name in the Database
    class Meta:
        db_table = "student_table"

def __str__(self):
    return "Student Details Added"

