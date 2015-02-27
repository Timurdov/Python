# -*- coding: utf-8 -*-
from django.forms import ModelForm
from person.models import Person, Previous, Education

# class AllForm(ModelForm):
#     class Meta:
#         model = {Person, Previous, Education}
#         fields = [ 'person_last_name','person_name','person_father_name','person_birthday', 'person_region','person_city',
#                'person_position','person_phone_number','person_email','person_skills','education_name','education_speciality',
#                'previous_place','previous_position']

class ResumeForm(ModelForm):
    class Meta:
        model = Person
        fields = ['person_last_name','person_name','person_father_name','person_birthday', 'person_region','person_city',
               'person_position','person_phone_number','person_email','person_skills','person_username','person_profession','person_branch']

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['education_name','education_speciality']

class PreviousForm(ModelForm):
    class Meta:
        model = Previous
        fields = ['previous_place','previous_position']