from django.shortcuts import render


def showIndex(request):
    d1 = {
    101:{"name":"Ram","salary":12000.00},
    102:{"name":"Ravi","salary":18000.00},
    103:{"name":"Rajesh","salary":10000.00}
    }

    return render(request,"index.html",{"data":d1})
