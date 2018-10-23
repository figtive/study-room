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

class RegisterEvent(forms.Form):

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
        'data-parsley-required-message': 'Please enter your email!',
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

    name = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=name_attrs))
    email = forms.CharField(label='', max_length=50, required=True, widget=forms.TextInput(attrs=email_attrs))
    student_id = forms.CharField(label='', required=True, widget=forms.TextInput(attrs=student_id_attrs))
    faculty = forms.CharField(label='', max_length=10, required=True, widget=forms.Select(choices=FACULTIES, attrs=faculty_attrs))

