from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def simple_route(request):
    return HttpResponse(content = '', status = '200')


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
    param = request.POST
    try:
        summa = str(int(param.__getitem__('a')) + int(param.__getitem__('b')))
    except:
        return HttpResponse(status = '400')
    return HttpResponse(content = summa, status = '200')

