import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')



class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Customer/',null=True,blank=True)
    mail= models.EmailField(max_length=30,null=False)
    address = models.CharField(max_length=40)
    mobile = models.PositiveIntegerField(max_length=15,null=False)
    gender = models.CharField(max_length=15,null=False)
    birthday = models.DateField(datetime.date)
    pid = models.CharField(max_length=3,null=False,validators=[alphanumeric])
    nid = models.PositiveIntegerField(max_length=15,null=False)

#
#    def clean_mail(self):
    #   print (type(self.cleaned_data))
    #   mail = self.cleaned_data.get('mail')
    #
    #   with open("customer/disposable-email-provider-domains.txt",'r') as f:
    #       blacklist = f.read().splitlines()

    #   for disposable_email in blacklist:
    #       if disposable_email in mail:
    #           raise models.validationError("spam %s" % disposable_email)
    #   return mail


    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name