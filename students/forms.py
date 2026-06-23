from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only letters."
            )
        return name

    def clean_roll_number(self):
        roll_number = self.cleaned_data.get('roll_number')

        if roll_number is not None and roll_number <= 0:
            raise forms.ValidationError(
                "Roll number must be greater than 0."
            )
        return roll_number

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age is not None and (age < 1 or age > 100):
            raise forms.ValidationError(
                "Age must be between 1 and 100."
            )
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone:
            if not phone.isdigit() or len(phone) != 10:
                raise forms.ValidationError(
                    "Phone number must contain exactly 10 digits."
                )
        return phone

    def clean_register_number(self):
        register_number = self.cleaned_data.get('register_number')

        if register_number and len(register_number) < 3:
            raise forms.ValidationError(
                "Register number must contain at least 3 characters."
            )
        return register_number

    def clean_address(self):
        address = self.cleaned_data.get('address')

        if address and len(address.strip()) < 5:
            raise forms.ValidationError(
                "Address must contain at least 5 characters."
            )
        return address