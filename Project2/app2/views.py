from django.http import HttpResponse


def showDetails(request):
    code = "<html><body bgcolor=blue><h1>Welcome to Django</h1><h3>Hello world</h3></body></html>"
    return HttpResponse(code)
