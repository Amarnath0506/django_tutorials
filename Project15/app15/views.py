from django.shortcuts import render
from .models import Employee


def generateAutoEmployeeID():
    qs = Employee.objects.all()
    if qs:
        pass
    else:
        idno = 101
        return idno



def showIndex(request):
    idno = generateAutoEmployeeID()
    return render(request,"index1.html",{"auto_idno":idno})