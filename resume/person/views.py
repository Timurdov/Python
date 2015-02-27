# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from person.models import Person, Previous, Education, Branch, Profession, Region
from person.form import ResumeForm, PreviousForm, EducationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def mainpage(request, page_number=1):
    resumes = Person.objects.all().order_by('-person_timestamp')
    region = Region.objects.all()
    branch = Branch.objects.all()
    profession = Profession.objects.all()
    username = auth.get_user(request).username
    if request.GET:
        if request.GET["person_region"] != "0":
            resumes = Person.objects.filter(person_region = request.GET["person_region"])
        if request.GET["person_branch"] != "0":
            resumes = resumes.filter(person_branch = request.GET["person_branch"])
        if request.GET["person_profession"] != "0":
            resumes = resumes.filter(person_profession = request.GET["person_profession"])
        return render_to_response('allresumes.html', {'resumes':resumes, 'username':username,
                                                  'regions':region, 'branches':branch, 'professions':profession})

    resumes_paginator  = Paginator(resumes, 3)
    return render_to_response('allresumes.html', {'resumes':resumes_paginator.page(page_number), 'username':username,
                                                  'regions':region, 'branches':branch, 'professions':profession})

def personpage(request, person_id=1):
    args={}
    args.update(csrf(request))
    args['person'] = Person.objects.get(id=person_id)
    args['person'].person_views += 1
    args['person'].save()
    args['education'] = Education.objects.filter(education_person_id=person_id)
    args['previous'] = Previous.objects.filter(previous_person_id=person_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('personresume.html', args)

def owncabinet(request, username):
    our_user = request.session['someuser']
    print "our_user is: " + our_user
    if auth.get_user(request).username and ("someuser" in request.session) and (our_user == username):
        education_form = EducationForm
        previous_form = PreviousForm
        args={}
        args.update(csrf(request))
        args['person'] = Person.objects.get(person_username = username)
        num_id = args['person'].id
        args['username'] = username
        args['education'] = Education.objects.filter(education_person=num_id)
        args['education_form'] = education_form
        args['job'] = Previous.objects.filter(previous_person=num_id)
        args['job_form'] = previous_form
        return render_to_response('owncabinet.html',args)
    else:
        args={}
        args.update(csrf(request))
        args['username'] = username
        args['person'] = "Вы можете зайти только зарегистрировавшись и только в свой личный кабинет"
    return render_to_response('shouldregister.html',args)

def saveowncabinet(request, username):
    if request.POST:
        form = ResumeForm(request.POST, instance = Person.objects.get(person_username=username))
        if form.is_valid():
            dataForm = form.save(commit=False)
            form.save()
    return redirect('/cabinet/get/%s' %username)


def cabineteducation(request, username):
    if request.POST:
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.education_person = Person.objects.get(person_username=username)
            form.save()
    return redirect('/cabinet/get/%s' %username)



def cabinetjob(request, username):
    if request.POST:
        form = PreviousForm(request.POST)
        if form.is_valid():
            previous = form.save(commit=False)
            previous.previous_person = Person.objects.get(person_username=username)
            form.save()
    return redirect('/cabinet/get/%s' %username)

def ownblank(request, username):
    args={}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['person'] = Person.objects.all()
    args['regions'] = Region.objects.all()
    args['branches'] = Branch.objects.all()
    args['professions'] = Profession.objects.all()
    return render_to_response('ownblank.html', args)


def saveownblank(request, username):
    if request.POST:
        form = ResumeForm(request.POST)
        if form.is_valid():
            dataForm = form.save(commit=False)
            form.save()
    return redirect('/blank/second/get/%s' %username)


def ownblanksecond(request, username):
    education_form = EducationForm
    previous_form = PreviousForm
    args={}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['person'] = Person.objects.get(person_username=username)
    num_id = args['person'].id
    args['education_form'] = education_form
    args['education'] = Education.objects.filter(education_person=num_id)
    args['job_form'] = previous_form
    args['job'] = Previous.objects.filter(previous_person=num_id)
    return render_to_response('blanksecond.html', args)


def addeducation(request, username):
    if request.POST:
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.education_person = Person.objects.get(person_username=username)
            form.save()
    return redirect('/blank/second/get/%s' %username)



def addjob(request, username):
    if request.POST:
        form = PreviousForm(request.POST)
        if form.is_valid():
            previous = form.save(commit=False)
            previous.previous_person = Person.objects.get(person_username=username)
            form.save()
    return redirect('/blank/second/get/%s' %username)

# def getquery(request, page_number=1):
#     resumes = Person.objects.all().order_by('-person_timestamp')
#     if request.GET:
#
#         if request.GET["person_region"] != "0":
#             resumes = Person.objects.filter(person_region = request.GET["person_region"])
#
#         if request.GET["person_branch"] != "0":
#             resumes = resumes.filter(person_branch = request.GET["person_branch"])
#
#         if request.GET["person_profession"] != "0":
#             resumes = resumes.filter(person_profession = request.GET["person_profession"])
#
#         region = Region.objects.all()
#         branch = Branch.objects.all()
#         profession = Profession.objects.all()
#         resumes_paginator  = Paginator(resumes, 3)
#         username = auth.get_user(request).username
#         return render_to_response('allresumes.html', {'resumes':resumes_paginator.page(page_number), 'username':username,
#                                                   'regions':region, 'branches':branch, 'professions':profession})




def changeeducation(request, edu_id):
    username = auth.get_user(request).username
    if request.POST:
        form = EducationForm(request.POST, instance = Education.objects.get(id=edu_id))
        if form.is_valid():
            dataForm = form.save(commit=False)
            form.save()
    return redirect('/cabinet/get/%s' %username)


def changejob(request, j_id):
    username = auth.get_user(request).username
    if request.POST:
        form = PreviousForm(request.POST, instance = Previous.objects.get(id=j_id))
        if form.is_valid():
            dataForm = form.save(commit=False)
            form.save()
    return redirect('/cabinet/get/%s' %username)












