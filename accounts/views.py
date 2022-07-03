import os
from django.conf import settings
from django.http import HttpResponseRedirect
from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
import pickle
import re
import pandas as pd
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
import requests
from .models import APIData
from . import api_test
from . import forms
# Create your views here.
# import eel
#importing eel

# face library login
import io
import base64
import PIL.Image as Image
   
# part 2 face libs
from django.urls import path, include
import face_recognition
import numpy as np
def data_preprocessing():

    #load the database
    anime_db = pd.read_csv(os.path.join(settings.BASE_DIR, 'static/js/MAL_final_4.csv'))
    anime_db.fillna('', inplace=True)
    
    
    return anime_db

# eel.init('web')
# eel.start('/')
# @eel.expose
# def fun_args(x):
#         print('hello %s' % x)

user_dict={}

@login_required
def landing(request):
    
    if request.GET and request.is_ajax:
        global dep 
        dep = request.GET.get('btn_text')
        print(type(dep))
        print("dep")
    else:
        # x_val = api_test.name_list
        
        # y_val = api_test.home_list
        # z_val = api_test.cover_list
        # n_val = api_test.vid_list
    # print(x_val)
    # print(n_val)
        # APIData.objects.all().delete()
        # for i in range(0,399):
        #     value = APIData(      
        #         # animeid = api_test.animeid[i],

        #         name = api_test.name_list[i],
        #         animetype=api_test.animetype[i],
        #         episodes=api_test.episodes[i],
        #         members=api_test.members[i],
        #         score_members=api_test.smembers[i],
        #         rating=api_test.rating[i],
        #         dates=api_test.dates[i],
        #         description=api_test.desc[i],
        #         img_src=api_test.img_src[i],
        #         english_name=api_test.english_name[i],
        #         genre = api_test.genre[i],
        #         genreb = api_test.genre1[i],
        #         genrec = api_test.genre2[i],
        #         genred = api_test.genre3[i],
        #         url=api_test.url[i],
        #         youtube = api_test.youtube[i],
               
        #         )
        #     value.save()
        data = APIData.objects.all()
   

        return render(request ,'home.html',{'data':data})





def sup(request):
    
    if request.method=="POST":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT =os.path.join(BASE_DIR,'media')    
        don=MEDIA_ROOT+'/images/'
        print('don : '+don)

        picname=request.POST.get('email')
        byte_data_var=request.POST.get('pic')
        byte_data=byte_data_var[23:]
        b=base64.b64decode(byte_data)
            # print(b)
        img=Image.open(io.BytesIO(b))
            # don=Settings.BASE_DIR + '/media/'+'/images/'
        print('don : '+don)
        img.save(don + picname + '.jpg', 'JPEG')  
        
        access_image_path=don+picname+'.jpg'
        face_1_image = face_recognition.load_image_file(access_image_path)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)
        face_1_face_encoding= np.array(face_1_face_encoding)
        user_dict[picname]=face_1_face_encoding
        return HttpResponseRedirect('/')
    return render(request,'sup.html')

def sin(request):
    if request.method=="POST":
        
        # prod=pack()
        # prod.name=request.POST.get('name')
        
        # prod.pic=request.POST.get('pic')
        # print(prod.pic)
        # prod.save()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT =os.path.join(BASE_DIR,'media')    
        don=MEDIA_ROOT+'/images/'
        print('don : '+don)

        picname=request.POST.get('askemail')


        byte_data_var=request.POST.get('askpic')
        byte_data=byte_data_var[23:]
        b=base64.b64decode(byte_data)
            # print(b)
        img=Image.open(io.BytesIO(b))
            # don=Settings.BASE_DIR + '/media/'+'/images/'
        print('don : '+don)
        randomno=randint(784,457895)
        randomno=str(randomno)
        img.save(don + picname +randomno+ '.jpg', 'JPEG')
        access_login_img_path=  don + picname +randomno+ '.jpg'
        face_login_image = face_recognition.load_image_file(access_login_img_path)

        face_2_face_encoding = face_recognition.face_encodings(face_login_image)
        face_2_face_encoding= np.array(face_2_face_encoding)
        face_sup_encoding = user_dict[picname]
        check=face_recognition.compare_faces(face_sup_encoding,face_2_face_encoding)
        print(check)
        if check[0]:
            return HttpResponseRedirect('/top1anime/')

        else :
            return HttpResponseRedirect('/top1movie/') 


    return render(request,'sin.html')

@login_required
def home(request):
   
    if request.GET and request.is_ajax:
        global dep 
        dep = request.GET.get('btn_text')
        print(type(dep))
        print("dep")
    else:
        # x_val = api_test.name_list
        
        # y_val = api_test.home_list
        # z_val = api_test.cover_list
        # n_val = api_test.vid_list
    # print(x_val)
    # print(n_val)
        # APIData.objects.all().delete()
        # for i in range(0,399):
        #     value = APIData(      
        #         # animeid = api_test.animeid[i],

        #         name = api_test.name_list[i],
        #         animetype=api_test.animetype[i],
        #         episodes=api_test.episodes[i],
        #         members=api_test.members[i],
        #         score_members=api_test.smembers[i],
        #         rating=api_test.rating[i],
        #         dates=api_test.dates[i],
        #         description=api_test.desc[i],
        #         img_src=api_test.img_src[i],
        #         english_name=api_test.english_name[i],
        #         genre = api_test.genre[i],
        #         genreb = api_test.genre1[i],
        #         genrec = api_test.genre2[i],
        #         genred = api_test.genre3[i],
        #         url=api_test.url[i],
        #         youtube = api_test.youtube[i],
               
        #         )
        #     value.save()
        toprated = APIData.objects.order_by('rating')[:45]
        movie=APIData.objects.filter(animetype = 'Movie').order_by('rating')[:19]
        highwatchers = APIData.objects.order_by('score_members')[:34]
        action=APIData.objects.filter(genreb = 'Action').order_by('rating')[:19]
        mystery=APIData.objects.filter(genreb = 'Mystery').order_by('rating')[:19]
        adventure=APIData.objects.filter(genreb = 'Adventure').order_by('rating')[:19]
        Shounen=APIData.objects.filter(genrec = 'Shounen').order_by('rating')[:19]
        Mecha=APIData.objects.filter(genrec = 'Mecha').order_by('rating')[:19]
        Mechab=APIData.objects.filter(genred = 'Mecha').order_by('rating')[:19]
        Drama=APIData.objects.filter(genreb = 'Drama').order_by('rating')[:19]
        Sports=APIData.objects.filter(genreb = 'Sports').order_by('rating')[:19]
        Supernatural=APIData.objects.filter(genreb = 'Supernatural').order_by('rating')[:19]
        Sci_Fi=APIData.objects.filter(genreb = 'Sci-Fi').order_by('rating')[:19]
        Suspense=APIData.objects.filter(genreb = 'Suspense').order_by('rating')[:19]
        Suspenseb=APIData.objects.filter(genrec = 'Suspense').order_by('rating')[:19]
        Historical=APIData.objects.filter(genreb = 'Historical').order_by('rating')[:19]
        Romance=APIData.objects.filter(genreb = 'Romance').order_by('rating')[:19]
        return render(request ,'landing.html',
                    {'toprated':toprated,'hightwatch':highwatchers,
                    'toprated':toprated,'highwatchers':highwatchers,
                    'movie':movie,'mystery':mystery,
                    'action':action,'adventure':adventure,
                    'Shounen':Shounen,'Mecha':Mecha,
                    'Drama':Drama,'Sports':Sports,
                    'Mechab':Mechab,
                    'Supernatural':Supernatural,
                    'Suspenseb':Suspenseb,
                    'Sci_fi':Sci_Fi,'Suspense':Suspense,
                    'Historical':Historical,'Romance':Romance,
                    })


   

@login_required
def detailv(request,members): 
        print("strr")
        name = "naruto"
        strr= name.replace('%20',' ')
        print(strr+"hey")
        x=APIData.objects.get(members = members)
        return render(request,'detailv.html',
        {"data":x})

@login_required
def similar_by_content(request,query):
    anime_db = data_preprocessing()
    # if request.method == 'POST':
    #     result = request.form
    # query = result['name']
    x=APIData.objects.get(english_name = query)
    

    #load the model file
    
    pkl_file = open(os.path.join(settings.BASE_DIR, 'static/js/anime_indices_1.pkl'), 'rb')
    indices = pickle.load(pkl_file)
    if query not in anime_db['english_name']:
        N = anime_db[anime_db['english_name'] == query].index[0]
        anime_list = []
        for n in indices[N][1:]:
            if query not in anime_db.loc[n]['english_name']:
                info = {
                    "name": anime_db.loc[n]['name'],
                    "english_name": anime_db.loc[n]['english_name'],
                    "rating": round(anime_db.loc[n]['rating'],2),
                    "genre": anime_db.loc[n]['genre'],
                    "type": anime_db.loc[n]['type'],
                    "MAL": anime_db.loc[n]['Image-SRC']
                    
                }    
                anime_list.append(info)
        print(anime_list[1])
        return render(request,"similar.html",{"data":x,"name":query,"topanime":anime_list})


@login_required
def gen(request,genre): 
       
        fil1=APIData.objects.filter(genre = genre)
        fil2=APIData.objects.filter(genreb = genre)
        fil3=APIData.objects.filter(genrec = genre)
        fil4=APIData.objects.filter(genred = genre)
        print(fil1)
        return render(request,'genre.html',
        {"fil1":fil1,"fil2":fil2,"fil3":fil3,"fil4":fil4,"typ":genre})

def top1movie(request): 
    top_ani=APIData.objects.filter(animetype = 'Movie').order_by('rating')[:111]
    return render(request,'genre.html',
        {"fil1":top_ani,"typ":"Top 100 Movies"})

def top1anime(request): 
    top_ani=APIData.objects.filter(animetype = 'TV').order_by('rating')[:111]
    return render(request,'genre.html',
        {"fil1":top_ani,"typ":"Top 100 Animes"})

@login_required
def search_anime(request,searched):
    anime_db = data_preprocessing() 
    # n = 0
     
    searched=searched.capitalize()
    searchedlower=searched.lower()
    searchedupper=searched.upper()
    # print('Anime with the words "{}" in the title:'.format(searched))
    anime_searched = []
    i = 0
    # print('Anime with the words "{}" in the title:'.format(query))
    for i, english_name in enumerate(anime_db.english_name):
        
      
        if anime_db.english_name[i].find(searched) >= 0 or  anime_db.english_name[i].find(searchedlower)>=0 or anime_db.english_name[i].find(searchedupper)>=0:
            dic={"MAL":anime_db["Image-SRC"][i],"english_name":anime_db.english_name[i]}
            print(dic)
            anime_searched.append(dic)
            # print(anime_db.name[i]+" "+anime_db["Image-SRC"][i])
            # print('Anime: {}; Format: {}'.format(anime_db.name[i],anime_db['type'][i]))

        i+=1
        # if i == 349:
        #      break
           
            
    # if i == 0:
    print(anime_searched)
    #     anime_searched="NF"
        # print('No anime with a name similar to "{}" exists in our database.'.format(searched))


    return render(request,'detailview.html',{
        'title':searched,
        'anime_searched':anime_searched,
    })


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('askname')
        password = "###??"+username+"4?25"
# valriable = func true or false true
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT =os.path.join(BASE_DIR,'media')    
        don=MEDIA_ROOT+'/images/'
        print('don : '+don)

        picname=username


        byte_data_var=request.POST.get('askpic')
        byte_data=byte_data_var[23:]
        b=base64.b64decode(byte_data)
            # print(b)
        img=Image.open(io.BytesIO(b))
            # don=Settings.BASE_DIR + '/media/'+'/images/'
        print('don : '+don)
        randomno=randint(784,457895)
        randomno=str(randomno)
        img.save(don + picname +randomno+ '.jpg', 'JPEG')
        access_login_img_path=  don + picname +randomno+ '.jpg'
        face_login_image = face_recognition.load_image_file(access_login_img_path)

        face_2_face_encoding = face_recognition.face_encodings(face_login_image)
        face_2_face_encoding= np.array(face_2_face_encoding)
        if picname not in user_dict.keys():
             messages.success(request, 'Face Not Found Please Create Account')
             return redirect('/accounts/login')
        face_sup_encoding = user_dict[picname]
        check=face_recognition.compare_faces(face_sup_encoding,face_2_face_encoding)
        print(check)
      

        
        if check[0] is False:
            messages.success(request, 'Face not matched')
            return redirect('/accounts/login')
        user = authenticate(username = username , password = password)
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = name+"@myanimedictinary.com"
        password = "###??"+name+"4?25"

        print(password)

        try:
            if User.objects.filter(username = name).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            

            # sup()
            user_obj = User(username = name , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.is_verified = True
            profile_obj.save()
            


            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            MEDIA_ROOT =os.path.join(BASE_DIR,'media')    
            don=MEDIA_ROOT+'/images/'
            print('don : '+don)

            picname=name
            byte_data_var=request.POST.get('pic')
            byte_data=byte_data_var[23:]
            b=base64.b64decode(byte_data)
                # print(b)
            img=Image.open(io.BytesIO(b))
                # don=Settings.BASE_DIR + '/media/'+'/images/'
            print('don : '+don)
            img.save(don + picname + '.jpg', 'JPEG')  
            
            access_image_path=don+picname+'.jpg'
            face_1_image = face_recognition.load_image_file(access_image_path)
            face_1_face_encoding = face_recognition.face_encodings(face_1_image)
            face_1_face_encoding= np.array(face_1_face_encoding)
            user_dict[picname]=face_1_face_encoding
            return HttpResponseRedirect('/')
#             profile_obj.save()
            # send_mail_after_registration(email , auth_token)
            return redirect('/')

        except Exception as e:
            print(e)


    return render(request , 'register.html')


def log_out_page(request):
     
    return render(request,'logo.html')

def logout_attempt(request):
    if request.method=='POST':
        logout(request)
        return redirect('/') 
    

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



# def verify(request , auth_token):
#     try:
#         profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

#         if profile_obj:
#             if profile_obj.is_verified:
#                 messages.success(request, 'Your account is already verified.')
#                 return redirect('/accounts/login')
#             profile_obj.is_verified = True
#             profile_obj.save()
#             messages.success(request, 'Your account has been verified.')
#             return redirect('/accounts/login')
#         else:
#             return redirect('/error')
#     except Exception as e:
#         print(e)
#         return redirect('/')

def error_page(request):
    return  render(request , 'error.html')








# def send_mail_after_registration(email , token):
#     subject = 'Your accounts need to be verified'
#     message = f'Click on the link http://127.0.0.1:8000/verify/{token}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message , email_from ,recipient_list )
    