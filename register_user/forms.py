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
        'name': 'username_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Username',
    }

    password_attrs = {
        'name': 'password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Password',
    }

    username = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='', max_length=50, required=True, widget=forms.PasswordInput(attrs=password_attrs))

class RegisterUser(forms.Form):

    name_attrs = {
        'name': 'name_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Name',
    }
    
    email_attrs = {
        'name': 'email_field',
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Email',
    }
    
    username_attrs = {
        'name': 'username_field',
        'type': 'text',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Username',
    }
    
    student_id_attrs = {
        'name': 'student_id_field',
        'id': 'student-id',
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
        'name': 'password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Password',
    }

    ver_password_attrs = {
        'name': 'ver_password_field',
        'type': 'password',
        'maxlength': 50,
        'class': 'form-control',
        'placeholder': 'Verify Password',
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

