from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.http import require_GET, require_POST


@require_GET
def simple_route(request):
    return render(request, 'corre/index.html')

def topic_details(request, pk):
    print(pk)
    return render(request, 'corre/topic_details.html')


def slug_route(request, slug):
    if len(slug) <= 16:
        ok_slug = slug
        return HttpResponse(ok_slug)
    else:
        return HttpResponse(status = '404')


def sum_route(request, first, second):
    summa = str(int(first) + int(second))
    return HttpResponse(content = summa, status='200')


@require_GET
def sum_get_method(request):
    param = request.GET
    try:
        summa = str(int(param.__getitem__('a')) + int(param.__getitem__('b')))
    except:
        return HttpResponse(status = '400')
    return HttpResponse(content = summa, status='200')


@require_POST
def sum_post_method(request):
    param = request.post
    try:
        summa = str(int(param.a) + int(param.b))
    except:
        return HttpResponse(status = '400')
    return HttpResponse(content = summa, status = '200')

