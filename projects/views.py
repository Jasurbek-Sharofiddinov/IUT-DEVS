from django.shortcuts import render
from django.http import HttpResponse

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
    page='projects'
    number=10
    context={'page':page,'number':number,'projects':projectsList}

    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectsObj=None
    for i in projectsList:
        if i['id'] == pk:
            projectsObj=i

    return render(request,'projects/single-project.html',{'project':projectsObj})