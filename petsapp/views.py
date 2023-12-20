from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from petsapp.forms import EmployeeForm
from petsapp.models import Employee

# Create your views here.
def index(request):
    return HttpResponse("<h2>Welcome to Simple Web App")

def home(request):
    temp=loader.get_template('simple.html')
    
    return HttpResponse(temp.render())

def emp(request):
    
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")