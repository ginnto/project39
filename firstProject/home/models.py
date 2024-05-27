from django.db import models

#  Create your models here.


class register(models.Model):
    name=models.CharField(max_length=200,unique=True)
    address = models.TextField()
    age=models.IntegerField()
    img=models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name

class subject(models.Model):
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.subject


class mark(models.Model):
    stu_id = models.ForeignKey(register,on_delete=models.CASCADE)
    mark = models.IntegerField()
    sub_id = models.ForeignKey(subject,on_delete=models.CASCADE)

