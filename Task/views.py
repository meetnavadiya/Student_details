from django.shortcuts import render,redirect
from .models import crud

# Create your views here.

def home(request):
    # print(request.__dict__)

    if request.method == 'POST':
        name=request.POST.get('name')
        roll_no=request.POST.get('roll')
        course=request.POST.get('course')
        address=request.POST.get('address')
       
        crud.objects.create(
            sname=name,
            sroll=roll_no,
            scourse=course,
            saddress=address
        )
        return redirect('home')
    
    tasks=crud.objects.all()

    context={
        'data':tasks
    }

    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def details(request,pk):
    data=crud.objects.get(id=pk)
    context={
        'data':data
    }
    return render(request,'details.html',context)

def update(request,pk):
    task=crud.objects.get(id=pk)
    if request.method == 'POST':
        
        sroll_no=request.POST.get('roll')
        sname=request.POST.get('name')
        scourse=request.POST.get('course')
        saddress=request.POST.get('address')
        
        task.roll_no=sroll_no
        task.name=sname
        task.course=scourse
        task.address=saddress
    

        task.save()
        return redirect('home')
    
    context={
        'task':task
    }

    return render(request,'update.html',context)

def delete(request,pk):
    task=crud.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
    context={
        'task':task
    }

    return render(request,'delete.html',context)