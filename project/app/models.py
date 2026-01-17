from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100,default='N/A')
    email = models.EmailField(unique=True)
    contact = models.CharField()
    qualification = models.CharField(max_length=200,default='N/A')
    gender = models.CharField(max_length=10,default='N/A')
    state = models.CharField(max_length=50,default='N/A')
    image = models.ImageField(upload_to='images/',default='N/A')
    audio = models.FileField(upload_to='audios/',default='N/A',null=True)
    video = models.FileField(upload_to='videos/',default='N/A')
    document = models.FileField(upload_to='documents/',default='N/A',null=True)
    password = models.CharField(max_length=20,null=True)  # null = true we write because already there is data if we don`t write it will show empty or error

    # def __str__(self):
    #     # return str(self.contact)
    #     # return self.name
    #     # return f"{self.name} - {self.email}"
    #     # return f"{self.name}"

def Emp1_contact(contact):
    if not len(str(contact))==10:
        raise ValidationError("Contact must be in 10 digits only")
    if not contact.isdigit():
        raise ValidationError("Contact must be only in number")

        

class Employee1(models.Model):
    name = models.CharField(max_length=100,validators=[MaxLengthValidator(10),MinLengthValidator(3)],   error_messages={
        'blank': 'Enter a valid name',
        'min_length': 'Name must be at least 3 characters',
        'max_length': 'Name must not exceed 10 characters',
    })
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15,validators=[Emp1_contact])
    image = models.ImageField(upload_to='employee_profiles/', null=True, blank=True)
    password = models.CharField(max_length=128,default='N/A')
    department=models.CharField(max_length=50,null=True)
    d_code = models.CharField(max_length=20,null=True)
    d_des = models.CharField(max_length=50,null=True)

    def clean(self):
        if not len(str(self.password))==4:
            raise ValidationError("Password must be 4 length")

    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    


class Department(models.Model):
    department = models.CharField(max_length=100)
    dept_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.department

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,default='panding')
    solution=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

