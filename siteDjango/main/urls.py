from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    #     path('', views.index, name="index"),
    path('', views.index, name="index"),
    path('addForm', views.addForm, name="addForm"),
    re_path(r'^scumCard/$', views.scumCard, name='scumCard'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^product_list/$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail,
            name='product_detail'),
]
