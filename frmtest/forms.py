# make sure this is at the top if it isn't already
from django import forms
from frmtest.models import contactdb

# our new form
class ContactForm(forms.ModelForm):
    class Meta:
        model=contactdb
        fields = '__all__' # Or a list of the fields that you want to include in your form
