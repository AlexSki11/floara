from django import forms
from froala_editor.widgets import FroalaEditor
from models import Page

class PageForm(forms.ModelForm):
  content = forms.CharField(widget=FroalaEditor)
  
  class Meta:
    model = Page
    fields = "__all__"