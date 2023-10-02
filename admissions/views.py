from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here

@login_required()
def homePage(request):
    return render(request,'index.html');

@login_required()
def addAdmission(request):
    form= StudentModelForm
    studentform={'form':form}
    
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
         
    
    return render(request,'admissions/add-admission.html',studentform);

@login_required()
def admissionReport(request):
    result=Student.objects.all();
    students={'allstudents':result}
    return render(request,'admissions/admission-report.html',students);

def deleteStudent(request):
    s=Student.object.get(id=id)
    s.delete
    return admissionReport(request)

def updateStudent(request,id):
    s=Student.object.get(id=id)
    form= StudentModelForm(instance=s)
    dict={'form':form}
    if reques.method=='POST':
        form=StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
    return render(request,'admissions/updatestudent.html',dict);

    
def addVendor(request):
    form= VendorForm
    Vform={'form':form}
    
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data)
            print(form.cleaned_data)
            print(form.cleaned_data)

    return render(request,'admissions/add-vendor.html',Vform);


#class based views
class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello..this is my first class based view</h1>")
    
            
        
            
         