from django import forms


class aboutForm(forms.Form):
    about_attrs = {
        'id': 'about_field',
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Testimony',
        'data-parsley-required-message': 'Please enter your testimony!',

    }

    about_post = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs=about_attrs))
