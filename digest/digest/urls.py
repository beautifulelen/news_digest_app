"""digest URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import NewsViewSet, CategoryViewSet, JobViewSet, SearchView, SearchDetailView
from .settings import DEBUG

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'news', NewsViewSet, base_name='news')
router.register(r'categories', CategoryViewSet, base_name='category')
if DEBUG:
    router.register(r'jobs', JobViewSet)
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/search$' , SearchView.as_view()),
    url(r'^api/search/(?P<pk>[0-9]+)$', SearchDetailView.as_view()),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)