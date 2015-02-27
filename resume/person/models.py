# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    class Meta():
        db_table = 'resume'
    person_last_name = models.CharField(max_length=50)
    person_name = models.CharField(max_length=50)
    person_father_name = models.CharField(max_length=50)
    person_birthday = models.DateField(null=True, blank=True)
    person_region = models.CharField(max_length=50)
    person_city = models.CharField(max_length=100)
    person_phone_number = models.IntegerField()
    person_email = models.EmailField()
    person_branch = models.CharField(max_length=100)
    person_profession = models.CharField(max_length=100)
    person_position = models.CharField(max_length=100)
    person_skills = models.TextField()
    person_views = models.IntegerField(default=0)
    person_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    person_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    person_username = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return "%s" %(self.person_username)

class Education(models.Model):
    class Meta():
        db_table = 'education'
    education_name = models.CharField(max_length=200, null=True, blank=True)
    education_speciality = models.CharField(max_length=200, null=True, blank=True)
    education_person = models.ForeignKey(Person)

class Previous(models.Model):
    class Meta():
        db_table = 'previous_job'
    previous_place = models.CharField(max_length=200, null=True, blank=True)
    previous_position = models.CharField(max_length=200, null=True, blank=True)
    previous_person = models.ForeignKey(Person)

class Region(models.Model):
    class Meta():
        db_table = 'region'
    region = models.CharField(max_length=50)
    # previous_person = models.ForeignKey(Person)
    def __unicode__(self):
        return  "%s" %(self.region)

class Branch(models.Model):
    class Meta():
        db_table = 'branch'
    branch = models.CharField(max_length=100)
    # previous_person = models.ForeignKey(Person)
    def __unicode__(self):
        return  "%s" %(self.branch)


class Profession(models.Model):
    class Meta():
        db_table = 'profession'
    profession = models.CharField(max_length=100)
    profession_branch = models.ForeignKey(Branch)
    def __unicode__(self):
        return "%s" %(self.profession)








