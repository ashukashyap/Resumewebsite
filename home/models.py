from django.db import models


# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    content = models.TextField(max_length=300)
    timestamp = models.DateField()


    def __str__(self):
        return self.name
    
    



