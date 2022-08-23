from cgi import FieldStorage
from re import template
import requests

from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys  
from django.core.files.storage import FileSystemStorage

def button(request):
    return render(request,"home.html")

def output(request):

    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

def external(request):
    inp=request.POST.get('param')
    image=request.FILES['image']
    print("image is",image)
    fs=FileSystemStorage()
    
    fn=fs.save(image.name,image)

    furl=fs.open(fn)
    print("full url",furl)
    templateurl=fs.url(fn)
    print(templateurl)
    #ou=run([sys.executable,"/Users/P/Desktop/Django/test.py",inp],shell=False,stdout=PIPE)
    imggg=run([sys.executable,"/Users/P/Desktop/Django/convert.py",str(furl),str(fn)],shell=False,stdout=PIPE)
     
   # print(ou)
    print()
    s=str(imggg.stdout)
    s=s[2:len(s)-5]
    print(s)
    return render(request,'home.html',{'raw_url':templateurl,'edit_url':s})



