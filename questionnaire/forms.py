from django.forms import ModelForm
from django import forms
from questionnaire.models import Candidate

class CandidateForm(ModelForm):
	class Meta:
		model = Candidate
		fields = ['name', 'email', 'html', 'css', 'javascript', 'python', 'django', 'ios', 'android']
	html = forms.IntegerField(min_value=0, max_value=10, required=False)
	css = forms.IntegerField(min_value=0, max_value=10, required=False)
	javascript = forms.IntegerField(min_value=0, max_value=10, required=False)
	python = forms.IntegerField(min_value=0, max_value=10, required=False)
	django = forms.IntegerField(min_value=0, max_value=10, required=False)
	ios = forms.IntegerField(min_value=0, max_value=10, required=False)
	android = forms.IntegerField(min_value=0, max_value=10, required=False)