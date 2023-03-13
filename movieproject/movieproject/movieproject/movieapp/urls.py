from django.contrib import admin
from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('detail/<int:m_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:up_id>/',views.update,name='update'),
    path('delete/<int:del_id>/',views.delete,name='delete'),
]
