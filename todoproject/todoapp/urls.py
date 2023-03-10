from django.contrib import admin
from django.urls import path
from . import views
app_name='todoapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add,name='add'),
    path('delete/<int:del_id>/',views.delete,name='delete'),
    path('update/<int:up_id>/',views.update,name='update'),
    path('listview/',views.listview.as_view(),name='listview'),
    path('cbvdetail/<int:pk>/',views.detailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
     path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete'),
]
