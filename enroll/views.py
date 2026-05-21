from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import StudentRegistartion
from .models import User

# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm = StudentRegistartion(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentRegistartion()
    stu = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,
                                                    'stu':stu})




def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

def update_data(request,id):
    pi = User.objects.get(id=id)
    if request.method=='POST':
        fm = StudentRegistartion(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentRegistartion(instance=pi)
    return render(request,'enroll/updatestu.html',{'form':fm})