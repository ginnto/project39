from django.shortcuts import render, get_object_or_404
from . models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        image = request.FILES.get('img')
        new_student = register(name=name, age=age, address=address, img=image)
        new_student.save()
    return render(request,'index.html')



def list(request):
    obj=register.objects.all()
    return render(request,'stu_list.html',{'j':obj})


def profile(request,id):
    pro=get_object_or_404(register,pk=id)
    marks = mark.objects.filter(stu_id=id)
    return render(request,'studentDetails.html',{'i':pro,'m':marks})
