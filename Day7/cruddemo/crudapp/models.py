from django.db import models

class Student(models.Model):
    stud_no = models.IntegerField()
    stud_name = models.CharField(max_length=30)
    stud_class = models.IntegerField()
    stud_address = models.CharField(max_length=100)
    stud_gender = models.CharField(max_length=10,default='Unknown')

