
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat,name='pro_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetails,name='procatdetails'),

]