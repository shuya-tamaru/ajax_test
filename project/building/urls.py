from django.urls import path
from .import views

app_name = 'building'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('main/', views.photo_add_view, name='main-view'),
    path('add/',views.AddView.as_view(), name='add'),
    path('hello-world/',views.hello_world_view, name='hello-world'),


    # path('add/',views.add,name='add'),


]
