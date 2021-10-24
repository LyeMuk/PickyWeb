# from pickyweb.home import forms
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tags, Links
# from django.contrib.auth.models import Tags

from itertools import chain
# Create your views here.
h_count=0
def home(request):
    global h_count
    h_count=h_count+1
    if request.method == "POST":
        if request.POST['Search'] != "":
            tag=[]
            link = Links.objects.values('url', 'name', 'tag')
            serch = request.POST['Search']
            serch=serch.lower()
            srchList = serch.split()
            for ele in srchList:
                el=Tags.objects.filter(tag=ele).first()
                if el is not None:
                    t=Tags.objects.filter(tag=ele).values('id', 'tag', 'detail')
                    tag= list(chain(tag,t))
            for ele in srchList:
                details=Tags.objects.all().values('detail')
                presentTag=[]
                for i in details:
                    hash=i['detail'].split('#')
                    if ele in hash:
                        h=Tags.objects.filter(detail=i['detail']).values('id', 'tag', 'detail')
                        for i in tag:
                            presentTag.append(i['tag'])
                        if h[0]['tag'] not in presentTag:
                            tag= list(chain(tag,h))    
            return render(request, 'home.html', {'tagi':tag, 'link':link})
    tag = Tags.objects.values('id', 'tag', 'detail')
    link = Links.objects.values('url', 'name', 'tag')
    return render(request, 'home.html', {'tagi':tag, 'link':link,'h':h_count})


def addone(request,pk):
    created="null"
    at="null"
    what="null"

    tagdict=Tags.objects.values('tag').distinct()
    tagdict=list(tagdict)


    if pk==1:
        if request.method == "POST":
            l=Links()
            url=request.POST.get("url")
            l.url=url
            if l.url!="":
                l.name=((url.split("://")[1]).split("/")[0])
                l.tag=request.POST.get("tag")
                l.save()
                what="Link"
                created=l.url
                at=l.tag

    else:
        if request.method == "POST":
            t=Tags()
            t.tag=request.POST.get("tag")
            taglist=[]
            for s in tagdict:
                taglist.append(s['tag'])
            if t.tag!="" and t.tag not in taglist:
                t.detail=request.POST.get("detail")
                t.pic=request.POST.get("pic")
                t.save()
                what="Tag"
                created=t.tag
                at=t.detail
    return render(request, 'add.html',{'what':what,'created':created,'at':at,'tagdict':tagdict})

p=0
def gopickey(request):
    global p 
    p+=1
    return render(request,'PickyWeb.html',{'p':p})

def Password(request):
    if request.method=="POST":
        Password=request.POST.get("Password")
        if Password=="ramu":
            tagdict=Tags.objects.values('tag').distinct()
            tagdict=list(tagdict)
            return render(request,'add.html',{'tagdict':tagdict})
    return render(request,'Password.html')