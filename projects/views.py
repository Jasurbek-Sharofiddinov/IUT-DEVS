from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
from django.shortcuts import redirect


def projects(request):
    projects=Project.objects.all()
    context={'projects':projects}

    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj=Project.objects.get(id=pk)
    # tags=projectObj.tags.all()
    # print('projectObj:',projectObj)
    return render(request,'projects/single-project.html',{'project':projectObj})

def createProject(request):
    form=ProjectForm()
    if request.method=='POST':
        print(request.POST)
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')


    context={'form':form}
    return render(request,"projects/project_form.html",context)
def updateProject(request,pk):
    project =Project.objects.get(id=pk)
    form=ProjectForm(instance=project)

    if request.method=='POST':
        print(request.POST)
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')


    context={'form':form}
    return render(request,"projects/project_form.html",context)

def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return  render(request,'projects/delete_template.html',context)