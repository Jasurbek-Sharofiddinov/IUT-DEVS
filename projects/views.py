from django.shortcuts import render
from django.http import HttpResponse
from .models import *
projectsList=[
    {
        'id':'1',
        'title':'Ecommerce website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'School website',
        'description':'Students can register and pass their exams'
    },

    {
        'id':'3',
        'title':'Social Network',
        'description':'Awesome open source project i am still working on'
    },
]

def projects(request):
    projects=Project.objects.all()
    context={'projects':projects}

    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj=Project.objects.get(id=pk)
    # tags=projectObj.tags.all()
    # print('projectObj:',projectObj)
    return render(request,'projects/single-project.html',{'project':projectObj})