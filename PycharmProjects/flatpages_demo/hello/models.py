from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):

    class Meta:
        app_label="hello"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return ' '.join([self.first_name,self.last_name])


    def __init__(self,*args,**kwargs):
        super(Contact,self).__init__(*args,**kwargs)