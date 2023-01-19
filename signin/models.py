from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=60)
    username=models.CharField(max_length=100)
    emailid=models.CharField(primary_key=True,max_length=150)
    dob=models.DateField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username