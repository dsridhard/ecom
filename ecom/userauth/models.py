from django.db import models

class Userauth(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  useremail =models.EmailField(max_length=255,null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)


  def __str__(self):
    return f"{self.firstname} {self.lastname}"