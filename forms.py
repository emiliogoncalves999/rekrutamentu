from django import forms
from rekrutamentu.models import UserApplication, UserAttachment
from django.forms import inlineformset_factory




from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button, Div, Field
from rekrutamentu.models import *


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserAttachment
        fields = ['upload_file']




class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'  # You can specify the fields you want to include if needed

    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='col-md-12'),
         
            ),
            Row(

                Column('requirements', css_class='col-md-12'),
            ),


            Row(
                Column('description', css_class='col-md-12'),
            ),
            
            Row(
                Column('publish_status', css_class='col-md-6'),
                Column('deadline', css_class='col-md-6'),
            ),
            Field('attachments'),
            Field('image'),

            Div(
                    Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['requirements'].widget.attrs['class'] = 'form-control'
        self.fields['attachments'].widget.attrs['class'] = 'form-control-file'
        self.fields['image'].widget.attrs['class'] = 'form-control-file'
        self.fields['publish_status'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.input_type = 'date'