from django import forms

FACULTIES = [
    ('', 'Faculty'),
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

class LoginUser(forms.Form):
    username_attrs = {
        'id': 'username_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Username',
        'data-parsley-pattern': '/^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]+$/',
        'data-parsley-pattern-message': 'Please enter a valid username!',
        'data-parsley-required-message': 'Please enter your username!',
    }

    password_attrs = {
        'id': 'password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Password',
        'data-parsley-required-message': 'Please enter your password!',
    }

    username = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='', max_length=50, required=True, widget=forms.PasswordInput(attrs=password_attrs))

class RegisterUser(forms.Form):

    name_attrs = {
        'id': 'name_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Name',
        'data-parsley-required-message': 'Please enter your name!',
    }
    
    email_attrs = {
        'id': 'email_field',
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Email',
        'data-parsley-type': 'email',
        'data-parsley-remote': '/user/register/email_check/',
        'data-parsley-required-message': 'Please enter your email!',
        'data-parsley-remote-message': 'This email is already used!',
    }
    
    username_attrs = {
        'id': 'username_field',
        'type': 'text',
        'minlength': 4,
        'maxlength': 12,
        'class': 'form-control',
        'placeholder': 'Username',
        'data-parsley-length': '[4,12]',
        'data-parsley-length-message': 'Username has to be between 4 and 12 characters!',
        'data-parsley-pattern': '/^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]+$/',
        'data-parsley-remote': '/user/register/username_check/',
        'data-parsley-pattern-message': 'Please enter a valid username!',
        'data-parsley-required-message': 'Please enter a username!',
        'data-parsley-remote-message': 'This username is already used!',
    }
    
    student_id_attrs = {
        'id': 'student_id_field',
        'type': 'text',
        'maxlength': 10,
        'class': 'form-control',
        'placeholder': 'Student ID',
        'data-parsley-type': 'digits',
        'data-parsley-rangelength': '[10,10]',
        'data-parsley-studentid': '',
        'data-parsley-required-message': 'Please enter your Student ID!',
        'data-parsley-rangelength-message': 'Student ID should be exactly 10 digits long',
    }
    
    faculty_attrs = {
        'id': 'faculty_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Faculty',
        'value': '',
        'data-parsley-required-message': 'Please choose a faculty!',
    }
    
    password_attrs = {
        'id': 'password_field',
        'type': 'password',
        'minlength': 8,
        'class': 'form-control',
        'placeholder': 'Password',
        'data-parsley-required-message': 'Please enter your password!',
    }

    ver_password_attrs = {
        'id': 'ver_password_field',
        'type': 'password',
        'minlength': 8,
        'class': 'form-control',
        'placeholder': 'Verify Password',
        'data-parsley-equalto': '#password_field',
        'data-parsley-required-message': 'Please enter your password!',
    }

    name = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=name_attrs))
    email = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=email_attrs))
    username = forms.CharField(label='', min_length=4, max_length=12, required=True, widget=forms.TextInput(attrs=username_attrs))
    student_id = forms.CharField(label='', required=True, widget=forms.TextInput(attrs=student_id_attrs))
    faculty = forms.CharField(label='', max_length=10, required=True, widget=forms.Select(choices=FACULTIES, attrs=faculty_attrs))
    password = forms.CharField(label='', min_length=8, required=True, widget=forms.PasswordInput(attrs=password_attrs))
    ver_password = forms.CharField(label='', min_length=8, required=True, widget=forms.PasswordInput(attrs=ver_password_attrs))

