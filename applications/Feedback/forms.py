from pyexpat import model
from django import forms
from .models import Feedback




class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['Username','first_name','last_name','subject','msg']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Username'].widget.attrs.update({'class': 'input__field cf-validate','placeholder':"Enter Your Username"})
        self.fields['first_name'].widget.attrs.update({'class': 'input__field cf-validate','placeholder':"Enter Your First Name"})
        self.fields['last_name'].widget.attrs.update({'class': 'input__field cf-validate','placeholder':"Enter Your Last Name"})
        self.fields['subject'].widget.attrs.update({'class': 'input__field cf-validate','placeholder':"Enter Your Subject"})
        self.fields['msg'].widget.attrs.update({'class': 'input__field cf-validate','placeholder':"Enter Your Message"})

        


