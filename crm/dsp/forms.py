from dsp.models import SessionReport
from django.forms import ModelForm
class SessionForm(ModelForm):
    class Meta:
        model=SessionReport
        fields='__all__'
