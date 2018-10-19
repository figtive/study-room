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

class LoginUser(forms.Form):
    username_attrs = {
        'id': 'username_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Username',
    }

    password_attrs = {
        'id': 'password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Password',
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
    }
    
    username_attrs = {
        'id': 'username_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Username',
    }
    
    student_id_attrs = {
        'id': 'student_id_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Student ID',
        'data-parsley-type': 'digits',
        'data-parsley-length': '[10, 10]',
    }
    
    faculty_attrs = {
        'id': 'faculty_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Faculty',
    }
    
    password_attrs = {
        'id': 'password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Password',
    }

    ver_password_attrs = {
        'id': 'ver_password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Verify Password',
        'data-parsley-equalto': '#password_field',
    }

    name = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=name_attrs))
    email = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=email_attrs))
    username = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=username_attrs))
    student_id = forms.CharField(label='', required=True, widget=forms.TextInput(attrs=student_id_attrs))
    faculty = forms.CharField(label='', max_length=10, required=True, widget=forms.Select(choices=FACULTIES, attrs=faculty_attrs))
    password = forms.CharField(label='', max_length=50, required=True, widget=forms.PasswordInput(attrs=password_attrs))
    ver_password = forms.CharField(label='', max_length=50, required=True, widget=forms.PasswordInput(attrs=ver_password_attrs))
    
    def clean(self):
        cleaned_data = super(RegisterUser, self).clean()
        password = cleaned_data.get("password")
        ver_password = cleaned_data.get("ver_password")
        student_id = cleaned_data.get("student_id")

        if password != ver_password:
            raise forms.ValidationError("Passwords do not match.")
        
        if (len(str(student_id)) != 10):
            raise forms.ValidationError("Student ID is invalid.")

