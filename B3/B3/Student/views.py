from django.shortcuts import render,get_object_or_404,redirect
from Student.models import Python

# Create your views here.
def Home(request):
    data=Python.objects.all()
    return render(request,'Home.html',{'data':data})

def info(request,id):
    marks=get_object_or_404(Python,id=id)
    return render(request,'info.html',{"marks":marks})

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        score=request.POST['score']
        sub=request.POST['sub']
        Python.objects.create(name=name,score=score,sub=sub)
        return redirect('Home')
    return render(request,'add.html')

def edit(request,id):
    stu=get_object_or_404(Python,id=id)
    if request.method=='POST':
        stu.name=request.POST['name']
        stu.score=request.POST['score']
        stu.sub=request.POST['sub']
        stu.save()
        return redirect('Home')
    return render(request,'edit.html',{'stu':stu})

def delete_obj(request,id):
    stu=get_object_or_404(Python,id=id)
    stu.delete()
    return redirect('Home')