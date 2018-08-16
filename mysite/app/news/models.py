
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from django.db import models

class Hello(CMSPlugin):
   title = models.CharField(max_length=255)
   message = HTMLField(blank=True)