from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit

from .models import Project, TimeBlock


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'baseline', 'bonus', 'rows']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'blocks:project_add'
        self.helper.layout = Layout(
            Div('name', css_class='col-8'),
            Div(
                Div('baseline', css_class='col-2'),
                Div('bonus', css_class='col-2'),
                Div('rows', css_class='col-2'),
                css_class='row'
            ),
            Submit('submit', 'Add project', css_class='mt-4')
        )


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'baseline', 'bonus', 'rows', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div('name', css_class='col-8'),
            Div(
                Div('baseline', css_class='col-2'),
                Div('bonus', css_class='col-2'),
                Div('rows', css_class='col-2'),
                css_class='row'
            ),
            Div(
                Div('active', css_class='col-2'),
                css_class='row'
            ),
            Submit('submit', 'Update project', css_class='mt-4')
        )


class TimeBlockUpdateForm(ModelForm):
    class Meta:
        model = TimeBlock
        fields = ['start', 'note']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div('start', css_class='col-6'),
            Div('note', css_class='col-6'),
            Submit('submit', 'Update block', css_class='mt-4'),
        )


        