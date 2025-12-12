from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone} | {self.address}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.email}"

    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Register"
