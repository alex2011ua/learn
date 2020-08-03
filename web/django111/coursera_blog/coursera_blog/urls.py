"""coursera_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from corre.views import *


urlpatterns = [

    url(r'^routing/simple_route', simple_route),
    url(r'^routing/topic2(?P<pk>\d+)/$', topic_details, name = "topic"),
    url(r'^routing/slug_route/(?P<slug>[-_a-z0-9]+)/$', slug_route),
    url(r'^routing/sum_route/(?P<first>\d+)/(?P<second>\d+)', sum_route),
    url(r'^routing/sum_get_method/.*', sum_get_method),
    url(r'^routing/sum_post_method/.*', sum_post_method),
    url(r'^admin/', admin.site.urls),
]
