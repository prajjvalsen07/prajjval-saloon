from django.db import models
from django.db import models
# Create your models here.
class Service (models.Model):
    service_title=models.CharField( max_length=150)
    service_desc=models.TextField()
    service_img = models.FileField(upload_to='service', max_length=250, null=True, default=None)
# aboutus clas
from django.db import models

class AboutUs(models.Model):
    about_title = models.CharField(max_length=100)
    about_description = models.TextField()
    about_img = models.FileField(upload_to='About', max_length=250, null=True, default=None)
    about_feature1 = models.CharField(max_length=100, blank=True, null=True)
    about_feature2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.about_title
#class for review
class review(models.Model):
    review_proffession=models.CharField(max_length=100)
    review_description = models.TextField()
    review_img = models.FileField(upload_to='review', max_length=250, null=True, default=None)
    review_name=models.CharField(max_length=100)

# contact form
from django.db import models
# Create your models here.
class Contactform (models.Model):
    fullname=models.CharField( max_length=150)
    email=models.CharField( max_length=150)
    phone=models.CharField( max_length=150)
    message=models.CharField( max_length=250)


  