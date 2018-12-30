from crispy_forms.layout import *
from .models import conference_form
from django.utils.translation import gettext_lazy as _
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from markdownx.fields import MarkdownxFormField


class confForm(forms.ModelForm):
    helper = FormHelper()

    helper.layout = Layout(
        Fieldset(

            'Name and acronym',
            HTML('<i>Enter the conference full name</i>'),
            'conference_name',
            HTML('<p><i>Enter the conference acronym</i></p>'),
            'conference_acronym',

        ),
        HTML('<hr>'),

        Fieldset(
            'Conference information',
            HTML('<p><i></i></p>'),
            'conference_webpage',
            HTML('<p><i></i></p>'),
            'conference_venue',
            HTML('<p><i></i></p>'),
            'conference_country',
            HTML('<p><i></i></p>'),
            'conference_city',
        ),
        HTML('<hr>'),

        Fieldset(
            'Date',
            HTML('<p><i></i></p>'),
            'conference_start',
            HTML('<p><i></i></p>'),
            'conference_end',
        ),
        HTML('<hr>'),

        Fieldset(
            'Research Area',
            HTML('<p><i></i></p>'),
            'conference_research_area',
            HTML('<p><i></i></p>'),
            'conference_area_notes',
        ),
        HTML('<hr>'),

        Fieldset(
            'Organizer',
            HTML('<p><i></i></p>'),
            'conference_organizer',
            HTML('<p><i></i></p>'),
            'conference_organizer_webpage',
            HTML('<p><i></i></p>'),
            'conference_organizer_contact',
        ),
        HTML('<hr>'),

        Fieldset(
            'Other information',
            HTML('<p><i></i></p>'),
            'conference_other_info',

        ),
        FormActions(
            Submit('send_installation', 'Send Installation'),

        )

    )
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'

    class Meta:
        model = conference_form
        fields = [
            'conference_name',
            'conference_acronym',
            'conference_webpage',
            'conference_venue',
            'conference_country',
            'conference_city',
            'conference_start',
            'conference_end',
            'conference_organizer',
            'conference_organizer_contact',
            'conference_organizer_webpage',
            'conference_area_notes',
            'conference_other_info',
            'conference_research_area',


        ]


class markdownForm(forms.Form):
    content = MarkdownxFormField();
