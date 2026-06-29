from django.urls import path
from Student.views import Home,info,add,edit,delete_obj

urlpatterns = [
    path("",Home,name='Home'),
    path("info/<int:id>/", info ,name='info'),
    path('add/',add,name='add'),
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete_obj,name='delete')
]