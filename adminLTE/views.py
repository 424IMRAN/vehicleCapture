from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import (get_object_or_404, render,HttpResponseRedirect) 
from .forms import Video_Form,Camera_Form
from .models import Video,camera
from django.db.models import F
import json
from django.contrib import messages
from django.views.generic import ListView
#from chardet import jisfreq


def dashboard(request):
    return render(request, 'dashboard.html', {"page":1,"dashboard":"menu-open","dashboardSub":"active"})

def cameras(request):
    cam= camera.objects.all()
    data2=[]
    for data in cam:
        k = {"id":data.id,"camera_name":data.camera_name,"camera_id":data.camera_id,
             "direction_name1":data.direction_name1,"direction_id1":data.direction_id1,"direction_coordinates1":data.direction_coordinates1,
             "direction_name2":data.direction_name2,"direction_id2":data.direction_id2,"direction_coordinates2":data.direction_coordinates2,
             "direction_name3":data.direction_name3,"direction_id3":data.direction_id3,"direction_coordinates3":data.direction_coordinates3,
             "direction_name4":data.direction_name4,"direction_id4":data.direction_id4,"direction_coordinates4":data.direction_coordinates4}
        data2.append(k)        
    return render(request, 'CameraList.html',  {"camera":"menu-open","cameraList":"active","context":data2})
F
def cameraNew(request):
    if request.method == 'POST':
        create_cam(request)
        return cameras(request)
    else:
        return render(request, 'cameraNew.html', {"camera":"menu-open","cameraNew":"active"})

def edit_cam(request, list_id):
    data= camera.objects.get(pk=list_id)
    data2=[]
    k = {"id":data.id,"camera_name":data.camera_name,"camera_id":data.camera_id,
             "direction_name1":data.direction_name1,"direction_id1":data.direction_id1,"direction_coordinates1":data.direction_coordinates1,
             "direction_name2":data.direction_name2,"direction_id2":data.direction_id2,"direction_coordinates2":data.direction_coordinates2,
             "direction_name3":data.direction_name3,"direction_id3":data.direction_id3,"direction_coordinates3":data.direction_coordinates3,
             "direction_name4":data.direction_name4,"direction_id4":data.direction_id4,"direction_coordinates4":data.direction_coordinates4}
    data2.append(k)
    if request.method == 'POST':
        form = Camera_Form(request.POST, instance = data)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.save()
        return cameras(request)
    else:
        return render(request, 'CameraEdit.html',  {"camera":"menu-open","cameraNew":"active","context":data2})
    
def edit_vid(request, list_id):
    data= Video.objects.get(pk=list_id)
    data2=[]
    k={"videoName":data.inputName,"id":data.id,"initialTime":data.initialTime,"file":data.file}
    
    data2.append(k)
    if request.method == 'POST':
        form = Video_Form(request.POST, instance = data)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.save()
        return video(request)
    else:
        return render(request, 'videoEdit.html',  {"video":"menu-open","videoNew":"active","context":data2})    
    

def video(request):
    vid=Video.objects.all()
    data2=[]
    for data in vid:
        k={"videoName":data.inputName,"id":data.id,"initialTime":data.initialTime,"file":data.file}
        data2.append(k)
        print(data2)
    return render(request, 'videoList.html',  {"video":"menu-open","videoList":"active","context":data2})

def videoNew(request):
    if request.method == 'POST':
       create_profile(request)
       return video(request)
    else:
        return render(request, 'videoNew.html', {"video":"menu-open","videoNew":"active"})
        
    

def create_cam(request): 
    form = Camera_Form()
    context ={} 
    if request.method == 'POST':
        form = Camera_Form(request.POST , request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.save()
            
def delete_cam(request, list_id):
    item = camera.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Cam Details Has Been Deleted!'))
    return  cameras(request)

def delete_vid(request, list_id):
    item = Video.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Video Has Been Deleted!'))
    return video(request)         

def create_profile(request):
    form = Video_Form()
    if request.method == 'POST':
        form = Video_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
       #     user_pr.file = request.FILES['file']
       #     file_type = user_pr.file.url.split('.')[-1]
       #     file_type = file_type.lower()
#            if file_type not in IMAGE_FILE_TYPES:
#                return render(request, 'profile_maker/error.html')
            user_pr.save()
       #     video(request)
            #return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    #context = {"form": form,}
    #return render(request, 'profile_maker/create.html', context)
    #videoNew(request)