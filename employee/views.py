from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# HOME / EMPLOYEE LIST
def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


# ADD EMPLOYEE
def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
            salary=request.POST['salary'],
            mobile=request.POST['mobile']
        )
        return redirect('home')

    return render(request, 'add.html')


# UPDATE EMPLOYEE
def update_employee(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.department = request.POST['department']
        emp.salary = request.POST['salary']
        emp.mobile = request.POST['mobile']
        emp.save()
        return redirect('home')

    return render(request, 'update.html', {'emp': emp})


# DELETE EMPLOYEE
def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('home')
