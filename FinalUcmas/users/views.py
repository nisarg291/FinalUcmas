import json
from ast import literal_eval
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from webapp.models import Student
from django.conf import settings
from .models import Profile, UserOTP,Notification
from django.core.mail import send_mail
from verify_email.email_handler import send_verification_email
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import random

def register(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')  # 213243 #None
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                messages.success(request, f'Account is Created For {usr.username}')
                return redirect('login')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'signup.html', {'otp': True, 'usr': usr})

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = str(form.cleaned_data.get('email'))
            password1 = str(form.cleaned_data.get('password1'))
            password2 = str(form.cleaned_data.get('password2'))
            username = str(form.cleaned_data.get('username'))
            print(username)
            first_name = str(form.cleaned_data.get('first_name'))
            print(first_name)
            last_name = str(form.cleaned_data.get('last_name'))
            print(last_name)
            print(email)
            
            # user=User(username=username,first_name=first_name,last_name=last_name,email=email,password1=password1,password2=password2)
            filter_Student = Student.objects.filter(StudentUserName=username, StudentFirstName=first_name, StudentLastName=last_name, StudentEmail=email)
            print(filter_Student)
            if len(filter_Student)==1:
                filter_Student=filter_Student[0]
                form.save()
                userObj = User.objects.filter(username=username)
                print(userObj)
                profile=Profile.objects.get(user=userObj[0])
                profile.StudentUserName=filter_Student.StudentUserName
                profile.StudentFirstName=filter_Student.StudentFirstName
                profile.StudentMiddleName=filter_Student.StudentMiddleName
                profile.StudentLastName=filter_Student.StudentLastName
                profile.StudentEmail=filter_Student.StudentEmail
                profile.BirthDate=filter_Student.BirthDate
                profile.std=int(filter_Student.std)
                profile.Gender=filter_Student.Gender
                profile.ucmaslevel=int(filter_Student.ucmaslevel)
                profile.Enroll=int(filter_Student.Enroll)
                profile.SchoolName=filter_Student.SchoolName
                profile.Hobbies=filter_Student.Hobbies
                profile.Refference=filter_Student.Refference
                profile.Ressidence=filter_Student.Ressidence
                profile.save()
                usr = User.objects.get(username=username)
                print(usr)
                # messages.success(request, f'Account created for {username}!')
                usr_otp = random.randint(100000, 999999)
                UserOTP.objects.create(user=usr, otp=usr_otp)
                mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"
                send_mail(
                    "Welcome to Nisarg - Verify Your Email",
                    mess,
                    settings.EMAIL_HOST_USER,
                    [usr.email],
                    fail_silently=False
                )
                
                return render(request, 'signup.html', {'otp': True, 'usr': usr})
            else:
                messages.warning(request, 'You are not a Student of ucmas you cannot register')
                messages.warning(request, 'contact us to join in ucmas')
                form = UserRegisterForm()
                return render(request, 'signup.html', {'form':form})

    else:
        form = UserRegisterForm()
        return render(request, 'signup.html', {'form': form})

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		get_otp = request.POST.get('otp') #213243 #None

		if get_otp:
			get_usr = request.POST.get('usr')
			usr = User.objects.get(username=get_usr)
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				login(request, usr)
				return redirect('home')
			else:
				messages.warning(request, f'You Entered a Wrong OTP')
				return render(request, 'user/login.html', {'otp': True, 'usr': usr})


		usrname = request.POST['username']
		passwd = request.POST['password']

		user = authenticate(request, username = usrname, password = passwd) #None
		if user is not None:
			login(request, user)
			return redirect('home')
		elif not User.objects.filter(username = usrname).exists():
			messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
			return redirect('login')
		elif not User.objects.get(username=usrname).is_active:
			usr = User.objects.get(username=usrname)
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to ITScorer - Verify Your Email",
				mess,
				settings.EMAIL_HOST_USER,
				[usr.email],
				fail_silently = False
				)
			return render(request, 'login.html', {'otp': True, 'usr': usr})
		else:
			messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
			return redirect('login')

	form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})

def resend_otp(request):
    if request.method == "GET":
        get_usr = request.GET['usr']
        if User.objects.filter(email=get_usr).exists() and not User.objects.get(email=get_usr).is_active:
            usr = User.objects.get(email=get_usr)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to ITScorer - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return HttpResponse("Resend")

    return HttpResponse("Can't Send ")


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        # which is uploaded bu user from his/her p.c.'s location
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        Cuser = request.user
        print(p_form)
        print(u_form)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'profile.html', context)


@login_required
def edit(request):
    Cuser = request.user
    return HttpResponse("hello edit")

@login_required
def notifications(request):
	noti = Notification.objects.filter(user=request.user, seen = False)
	noti = serializers.serialize('json', noti)
	return JsonResponse({'data':noti})

@login_required
def notifications_seen(request):
	Notification.objects.filter(user=request.user, seen = False).update(seen = True)
	return HttpResponse(True)

@csrf_exempt
@login_required
def clear_notifications(request):
	if request.method == "POST":
		Notification.objects.filter(user=request.user).delete()
		return HttpResponse(True)
	return HttpResponse(False)

def islogin(request):
	return JsonResponse({'is_login':request.user.is_authenticated})
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
