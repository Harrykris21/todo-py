
from django.urls import path
from .import views
# app_name='todoapp'
urlpatterns = [

    path('',views.index,name='index'),
    # path('details', views.details, name='details'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),

]
