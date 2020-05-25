from django.urls import path, include
from mytodo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete<int:pk>', views.delete_todo, name='delete_todo'),
]