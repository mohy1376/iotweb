# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class comment(models.Model):
    text= models.CharField(max_length=480)
    name= models.CharField(max_length =120)
    email= models.EmailField()