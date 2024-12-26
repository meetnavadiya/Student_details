from django.shortcuts import render,redirect
from .models import crud,Contact
from django.db.models import Q


# Create your views here.

def home(request):
    query = request.GET.get('q', '')

    if query:
        data = crud.objects.filter(name__icontains=query)
    else:
        data=crud.objects.all()
    
    context={
        'data':data
    }
    return render(request,'home.html', context)
 
def add(request):
    if request.method == 'POST':
        roll_no=request.POST.get('roll')
        name=request.POST.get('name')
        course=request.POST.get('course')
        address=request.POST.get('address')
        crud.objects.create(
            roll_no=roll_no,
            name=name,
            course=course,
            address=address
        )
        return redirect('home')
    return render(request,'add.html')


def about(request):
    return render(request,'about.html')


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

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        return redirect('con_msg')
    
    return render(request,'contact.html')

def con_msg(request):
    return render(request,'con_msg.html')