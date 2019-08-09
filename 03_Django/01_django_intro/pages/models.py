from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id} - 이름: {self.name}, 이메일: {self.email}, 생일: {self.birthday}, 나이: {self.age}'