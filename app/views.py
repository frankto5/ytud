from django.shortcuts import render
from pytube import YouTube
import os
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        subject= request.POST["subject"]
        message= request.POST["message"]+"\nEl usuario que envio la consulta es: "+request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list=["adm_ytud@hotmail.com"]
        send_mail(subject,message,email_from,recipient_list)        
        return render(request,"thanks.html")
    
    return render(request,"contact.html")


def donations(request):
    return render(request,"donations.html")

def download (request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    video=[]
    video = yt.streams.filter(progressive=True).all()
    audio = []
    audio = yt.streams.filter(only_audio=True , subtype="mp4")
    print(audio)
    embed_link = url.replace('watch?v=','embed/')
    context = {'audio':audio,'video':video,'embed':embed_link}
    return render(request,"download.html",context)

def ytud_download(request,resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method== 'POST':
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request,'finish.html')
    else: 
        return render(request,'error.html')
