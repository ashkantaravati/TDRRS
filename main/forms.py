from django import forms

class myForm(forms.Form):
    firstName=forms.CharField()
    def __init__(self,*args, **kwargs):
        super(myForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].label = 'نام'