from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def echo(request):
    dat = str(datetime.datetime.now())[10:-7]
    b = request.META
    a = {}
    a['statement'] = b.get('HTTP_X_PRINT_STATEMENT')

    a['metod'] = request.method
    param = None
    if a['metod'] == 'GET':
        param = request.GET
    elif a['metod'] == 'POST':
        param = request.POST

    if len(param) >= 1:
        a['key'] = True
        a['param'] =[]
        for item, key in param.items():
            c = str(item)+': '+str(key)
            a['param'].append(c)
    else:
        a['key'] = None
    print(a['statement'])
    lis = ['1','2','3']
    return render(request, 'echo.html', a)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
