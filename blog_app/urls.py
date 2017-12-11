"""project URL Configuration

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
from blog_app.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog_app import views


urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view(), name='post-detail'),
    url(r'^new/$', BlogCreateView.as_view(), name='post-new'),
    url(r'^(?P<pk>\d+)/edit/$', BlogUpdateView.as_view(), name='post-edit'),
    url(r'^(?P<pk>\d+)/delete/$', BlogDeleteView.as_view(), name='post-delete'),
    # /users include handles django login and logout classed based views 
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup')
]
