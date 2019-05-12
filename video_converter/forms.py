from django import forms

from .models import QueryHistory


class DownloadForm(forms.ModelForm):
    url = forms.RegexField(
        regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',
        widget=forms.TextInput(attrs={
            'placeholder': 'paste or input video link'}),
        label=False, required=True, max_length=500)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': 'input your email'}),
        label=False)

    class Meta:
        model = QueryHistory
        fields = ('url', 'email')
