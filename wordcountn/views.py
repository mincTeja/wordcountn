from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html',{'hey':"hi how are you?"})

def count(request):
    fulltext=request.GET["fulltext"]
    d={}
    l=fulltext.split(" ")
    for i in l:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    print(d)
    return render(request,"count.html",{"fulltext":fulltext,"count":len(l),"word_dict":d.items()})

def about(request):
    return render(request,"about.html")