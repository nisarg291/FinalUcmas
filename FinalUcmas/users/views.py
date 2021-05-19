import json
from ast import literal_eval
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from webapp.models import Student
from .models import Profile
def register(request):
    if request.method == 'POST':
        
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            email=str(form.cleaned_data.get('email'))
            password1=str(form.cleaned_data.get('password1'))
            password2=str(form.cleaned_data.get('password2'))
            username = str(form.cleaned_data.get('username'))
            print(username)
            first_name = str(form.cleaned_data.get('first_name'))
            print(first_name)
            last_name = str(form.cleaned_data.get('last_name'))
            print(last_name)
            print(email)
            print(request.POST)
            print(form)
        # user=User(username=username,first_name=first_name,last_name=last_name,email=email,password1=password1,password2=password2)
            filter_Student=Student.objects.filter(StudentUserName=username,StudentFirstName=first_name,StudentLastName=last_name,StudentEmail=email)
            # print(filter_Student[0])
            if len(filter_Student)==1:
                filter_Student=filter_Student[0]
                form.save()
                userObj=User.objects.filter(username=username)
                print(filter_Student.BirthDate)
                profile=Profile(user=userObj[0],StudentUserName=username,StudentFirstName=filter_Student.StudentFirstName,StudentMiddleName=filter_Student.StudentMiddleName,StudentLastName=filter_Student.StudentLastName,StudentEmail=filter_Student.StudentEmail,BirthDate=filter_Student.BirthDate,Gender=filter_Student.Gender,std=filter_Student.std,ucmaslevel=filter_Student.ucmaslevel,Enroll=filter_Student.Enroll,SchoolName=filter_Student.SchoolName,Hobbies=filter_Student.Hobbies,Refference=filter_Student.Refference,Ressidence=filter_Student.Ressidence)
                print(profile)
                profile.save()
                messages.success(request, f'Account created for {username}!')
                return redirect('home')
            
            else:
                messages.warning(request,'You are not a Student of ucmas you cannot register')
                messages.warning(request,'contact us to join in ucmas')
                return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        #which is uploaded bu user from his/her p.c.'s location
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        Cuser=request.user;

        context = {
        'u_form': u_form,
        'p_form': p_form,
        }
        return render(request, 'profile.html', context)

@login_required
def edit(request):
    Cuser=request.user;
    return HttpResponse("hello edit")
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
    #     #which is uploaded bu user from his/her p.c.'s location
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)
    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form,
    # }
    # return render(request, 'users/edit.html', context)
