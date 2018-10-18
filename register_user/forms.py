from django import forms

FACULTIES = [
    ('FK', 'FK'),
    ('FKG', 'FKG'),
    ('FKM', 'FKM'),
    ('FIK', 'FIK'),
    ('FF', 'FF'),
    ('FMIPA', 'FMIPA'),
    ('FT', 'FT'),
    ('FASILKOM', 'FASILKOM'),
    ('FH', 'FH'),
    ('FEB', 'FEB'),
    ('FIB', 'FIB'),
    ('FPsi', 'FPsi'),
    ('FISIP', 'FISIP'),
    ('FIA', 'FIA'),
    ('VOKASI', 'VOKASI'),
]

class RegisterUser(forms.Form):

    name_attrs = {
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Name',
    }
    
    email_attrs = {
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Email',
    }
    
    username_attrs = {
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Username',
    }
    
    student_id_attrs = {
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Student ID',
    }
    
    faculty_attrs = {
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Faculty',
    }
    
    password_attrs = {
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'verify-pass',
    }

    name = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=name_attrs))
    email = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=email_attrs))
    username = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=username_attrs))
    student_id = forms.CharField(label='', required=True, widget=forms.TextInput(attrs=student_id_attrs))
    faculty = forms.CharField(label='', max_length=10, required=True, widget=forms.Select(choices=FACULTIES, attrs=faculty_attrs))
    password = forms.CharField(label='', max_length=50, required=True, widget=forms.PasswordInput(attrs=password_attrs))
