from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.

class Page(models.Model):
  content = FroalaField()
