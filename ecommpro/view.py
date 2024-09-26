from django.shortcuts import HttpResponse , render , redirect

def test (request):
    if request.path.startswith('/am'):
        print('ok')
    else:
        print(request.path)
    return HttpResponse (request)