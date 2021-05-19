from django.shortcuts import render,HttpResponse,redirect
# import pyttsx3 #pip install pyttsx3
# import speech_recognition as sr #pip install speechRecognition
from django.contrib import messages
import datetime
# from bs4 import BeautifulSoup
import requests
# import webbrowser
from django.contrib.auth.decorators import login_required
import os
# import smtplib
import time
import random

# from gtts import gTTS
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 200)
# def speak(text):
#     tts=gTTS(text=text,lang="en")
#     fileName="voice.mp3"
#     tts.save(fileName)
#     playsound.playsound(fileName)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# # Create your views here.

# for listening and flash menu page
@login_required
def listening_flash_menu(request):
    return render(request,'listening_flash_menu.html')

# for competitions page
def competitions(request):
    return render(request,'competitions.html')

# for gallary page
def gallary(request):
    return render(request,'gallary.html')

# for levels page
def levels(request):
    return render(request,'levels.html')

@login_required
def info(request):
    return render(request,'info.html')

def profile(request):
    return render(request, 'profile.html')
# for aboutus page
def aboutus(request):
    return render(request,'aboutus.html')

# for main home page
def home(request):
    return render(request,'home.html')

#for login page
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        request.session['email']=email;
        request.session['password']=password;
        if email=="student@ucmas.com":
            if password=="123456":
                context={
                    'email':email,
                    'password':password,
                }
                return render(request,'index.html',context)
            else:
                messages.warning(request,'Password Do not Match')
                return render(request,'login.html')
                return HttpResponse('Password Do not Match')
        else:
            messages.warning(request,'wrong email id')
            return render(request,'login.html')
    # if request.session['email']=='student@ucmac.com' and request.session['password']=='123456':
    #     return render(request,'index.html') 
    # else:
    #     return render(request,'login.html')
    return render(request,'login.html') 

# for addition Option Page for listening 
@login_required
def addition(request):
    return render(request,'Addition.html')

# for multiplication Option Page for listening 
@login_required
def multiplication(request):
    return render(request,'Multiplication.html')

# for division Option Page for listening 
@login_required
def division(request):
    return render(request,'division.html')

# for listening practice Page
@login_required 
def listening(request):
    return render(request,'listening.html')

# for flash practice Page
@login_required
def flash(request):
    return render(request,'flash.html')

# for addition Option Page for flash card
@login_required
def flash_addition(request):
    return render(request,'flash_addition.html')

# for multiplication Option Page for flash card
@login_required
def flash_multiplication(request):
    return render(request,'flash_multiplication.html')

# for division Option Page for flash card
@login_required
def flash_division(request):
    return render(request,'flash_division.html')

#for logout page
def logout(request):
    del request.session['email']
    del request.session['password']
    return render(request,'login.html')
def validate(request):
    pass



            
# for addition generator page for flash card
def generate_flash_addition(request):
    questions=[]
    ans1=[]
    if request.method=="POST":
        try:
            no_of_digits=int(request.POST.get("digits"))
            no_of_rows=int(request.POST.get("rows"))
            no_of_questions=int(request.POST.get("questions"))
            questions_speed=int(request.POST.get('questions_speed'))
            print(no_of_digits)
            print(questions_speed)
            print(no_of_questions)
            print(no_of_rows)
            for que in range(0,no_of_questions):
                question=[]
                ans=[]
                j=0
                for i in range(0,no_of_rows//5):
                    rr=random.randrange(0,3);
                    if rr==0:
                        rand=random.randrange(2,5);
                        for row in range(0,5):
                            if rand!=2:
                                if row!=rand:
                                    n=random.randrange(int('1'*no_of_digits),int('9'*no_of_digits))
                                    question.append(n)  
                                else:
                                    n1=random.randrange(int('6'*no_of_digits),int('9'*no_of_digits))
                                    question.append(-n1) 
                            if rand==2:
                                if row==1:
                                    n=random.randrange(int('6'*no_of_digits),int('9'*no_of_digits))
                                    question.append(n) 
                                elif row!=rand:
                                    n=random.randrange(int('1'*no_of_digits),int('9'*no_of_digits))
                                    question.append(n)  
                                else:
                                    n1=random.randrange(int('6'*no_of_digits),int('9'*no_of_digits))
                                    if question[j-2]>0 and question[j-1]>0:
                                        print(question[j-2]+question[j-1])
                                        if question[j-2]+question[j-1]-n1>=0:
                                            question.append(-n1) 
                                        else:
                                            n1=random.randrange(int('6'*no_of_digits),int(question[j-2]+question[j-1]))
                                            question.append(-n1)
                                    else:
                                        question.append(-n1)
                            j+=1
                    elif rr==1:
                    # for i in range(0,no_of_rows//5):
                        rand=random.randrange(1,2);
                        if rand==2:
                            rand1=4;
                        else:
                            rand1=3;
                        for row in range(0,5):
                            if row==int(rand-1) or row==int(rand1-1):
                                n=random.randrange(int('6'*no_of_digits), int('9'*no_of_digits))
                                question.append(n)
                            elif row==rand or row==rand1:
                                n1=random.randrange(int('1'*no_of_digits), int('6'*no_of_digits))
                                question.append(-n1)
                            else:
                                n=random.randrange(int('1'*no_of_digits), int('9'*no_of_digits))
                                question.append(n)
                            j+=1
                    elif rr==2:
                    # for i in range(0,no_of_rows//5):
                        for row in range(0,5):
                            n=random.randrange(int('1'*no_of_digits), int('9'*no_of_digits))
                            question.append(n)
                            j+=1
                print(question)
                questions.append(question)
                sum=0
                for i in question:
                    # speak(i)
                    sum+=i;
                # speak("that is?")
                # time.sleep(10)
                # ans.append(sum)
                ans1.append(sum)
                print(ans1)
                # anss.append(ans)
            print(questions)
            print(ans1)
          
            return render(request,"generate_flash_addition.html",{'questions':questions,'ans':ans1,'no_of_questions':no_of_questions,'no_of_rows':no_of_rows,'questions_speed':questions_speed})
        except:
            return redirect('flash_addition')
# for addition generator page for listening card   
def generate_add(request):
    questions=[]
    ans1=[]
    if request.method=="POST":
        no_of_digits=int(request.POST.get("digits"))
        no_of_rows=int(request.POST.get("rows"))
        no_of_questions=int(request.POST.get("questions"))
        
        print(no_of_digits)
        print(no_of_questions)
        print(no_of_rows)
        for que in range(0,no_of_questions):
            question=[]
            ans=[]
            j=0
            for i in range(0,no_of_rows//5):
                rr=random.randrange(0,3);
                if rr==0:
                    rand=random.randrange(2,5);
                    for row in range(0,5):
                        if rand!=2:
                            if row!=rand:
                                n=random.randrange(int('1'*no_of_digits),int('9'*no_of_digits))
                                question.append(n)  
                            else:
                                n1=random.randrange(int('6'*no_of_digits),int('9'*no_of_digits))
                                question.append(-n1) 
                        if rand==2:
                            if row==1:
                                n=random.randrange(int('6'*no_of_digits),int('9'*no_of_digits))
                                question.append(n) 
                            elif row!=rand:
                                n=random.randrange(int('1'*no_of_digits),int('9'*no_of_digits))
                                question.append(n)  
                            else:
                                n1=random.randrange(int('6'*no_of_digits),int('9'*no_of_digits))
                                if question[j-2]>0 and question[j-1]>0:
                                    print(question[j-2]+question[j-1])
                                    if question[j-2]+question[j-1]-n1>=0:
                                        question.append(-n1) 
                                    else:
                                        n1=random.randrange(int('6'*no_of_digits),int(question[j-2]+question[j-1]))
                                        question.append(-n1)
                                else:
                                    question.append(-n1)
                        j+=1
                elif rr==1:
                # for i in range(0,no_of_rows//5):
                    rand=random.randrange(1,2);
                    if rand==2:
                        rand1=4;
                    else:
                        rand1=3;
                    for row in range(0,5):
                        if row==int(rand-1) or row==int(rand1-1):
                            n=random.randrange(int('6'*no_of_digits), int('9'*no_of_digits))
                            question.append(n)
                        elif row==rand or row==rand1:
                            n1=random.randrange(int('1'*no_of_digits), int('6'*no_of_digits))
                            question.append(-n1)
                        else:
                            n=random.randrange(int('1'*no_of_digits), int('9'*no_of_digits))
                            question.append(n)
                        j+=1
                elif rr==2:
                # for i in range(0,no_of_rows//5):
                    for row in range(0,5):
                        n=random.randrange(int('1'*no_of_digits), int('9'*no_of_digits))
                        question.append(n)
                        j+=1
            print(question)
            questions.append(question)
            sum=0
            for i in question:
                # speak(i)
                sum+=i;
            # speak("that is?")
            # time.sleep(10)
            # ans.append(sum)
            ans1.append(sum)
            print(ans1)
            # anss.append(ans)
        print(questions)
        print(ans1)
          
        return render(request,"generate_add.html",{'questions':questions,'ans':ans1,'no_of_questions':no_of_questions,'no_of_rows':no_of_rows})
    
    # return render(request,"generate.html",context=content)

# for multiplication generator page for listening card
def generate_multi(request):
    
    if request.method=="POST":
        num1=[]
        num2=[]
        ans=[]
        questions=[]
        no_of_first_digits=int(request.POST.get("firstnum_digits"))
        no_of_second_digits=int(request.POST.get("secondnum_digits"))
        no_of_questions=int(request.POST.get("questions"))
        for que in range(0,no_of_questions):
            question=[]
            j=0
            n1=random.randrange(int('1'*no_of_first_digits),int('9'*no_of_first_digits))
            n2=random.randrange(int('1'*no_of_second_digits),int('9'*no_of_second_digits))
            num1.append(n1)
            num2.append(n2)
            question.append(n1)
            question.append(n2)
            questions.append(question)
            ans.append(n1*n2)
        context={
            'num1':num1,
            'num2':num2,
            'no_of_questions':no_of_questions,
            'questions':questions,
            'ans':ans,
        }
        return render(request,"generate_multi.html",context)

# for multiplication generator page for flash card
def generate_flash_multi(request):
    if request.method=="POST":
        num1=[]
        num2=[]
        ans=[]
        questions=[]
        no_of_first_digits=int(request.POST.get("firstnum_digits"))
        no_of_second_digits=int(request.POST.get("secondnum_digits"))
        no_of_questions=int(request.POST.get("questions"))
        questions_speed=int(request.POST.get('questions_speed'))
        for que in range(0,no_of_questions):
            question=[]
            j=0
            n1=random.randrange(int('1'*no_of_first_digits),int('9'*no_of_first_digits))
            n2=random.randrange(int('1'*no_of_second_digits),int('9'*no_of_second_digits))
            num1.append(n1)
            num2.append(n2)
            question.append(n1)
            question.append(n2)
            questions.append(question)
            ans.append(n1*n2)
        context={
            'num1':num1,
            'num2':num2,
            'no_of_questions':no_of_questions,
            'questions':questions,
            'ans':ans,
            'questions_speed':questions_speed,
        }
        return render(request,"generate_flash_multi.html",context)

# for division generator page for listening card
def generate_div(request):
   if request.method=="POST":
        num1=[]
        num2=[]
        ans=[]
        questions=[]
        division_options=request.POST.get("division_options")
        no_of_first_digits,no_of_second_digits=division_options.split('÷');
        no_of_first_digits=int(no_of_first_digits)-int(no_of_second_digits)
        no_of_second_digits=int(no_of_second_digits)
        no_of_questions=int(request.POST.get("questions"))
        for que in range(0,no_of_questions):
            question=[]
            j=0
            n1=random.randrange(int('1'*no_of_first_digits),int('9'*no_of_first_digits))
            n2=random.randrange(int('1'*no_of_second_digits),int('9'*no_of_second_digits))
            num1.append(n1)
            num2.append(n2)
            question.append(n1)
            question.append(n2)
            questions.append(question)
            ans.append(n1*n2)
        context={
            'num1':num1,
            'num2':num2,
            'no_of_questions':no_of_questions,
            'questions':questions,
            'ans':ans
        }
        return render(request,'generate_div.html',context)

# for division generator page for flash card
def generate_flash_div(request):
    if request.method=="POST":
        num1=[]
        num2=[]
        ans=[]
        questions=[]
        division_options=request.POST.get("division_options")
        no_of_first_digits,no_of_second_digits=division_options.split('÷');
        no_of_first_digits=int(no_of_first_digits)-int(no_of_second_digits)
        no_of_second_digits=int(no_of_second_digits)
        no_of_questions=int(request.POST.get("questions"))
        questions_speed=int(request.POST.get('questions_speed'))
        for que in range(0,no_of_questions):
            question=[]
            j=0
            n1=random.randrange(int('1'*no_of_first_digits),int('9'*no_of_first_digits))
            n2=random.randrange(int('1'*no_of_second_digits),int('9'*no_of_second_digits))
            num1.append(n1)
            num2.append(n2)
            question.append(n1)
            question.append(n2)
            questions.append(question)
            ans.append(n1*n2)
        context={
            'num1':num1,
            'num2':num2,
            'no_of_questions':no_of_questions,
            'questions':questions,
            'ans':ans,
            'questions_speed':questions_speed,
        }
        return render(request,'generate_flash_div.html',context)
