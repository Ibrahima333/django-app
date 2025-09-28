from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/',views.band_list,name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('about-us/',views.about,name='about'),
    path('contact-us/',views.contact_us, name='contact'),
    path('bands/add',views.band_create, name='band_create'),
    path('bands/<int:id>/change/', views.band_update, name='band_change'),
    path('bands/<int:id>/delete/', views.band_delete, name='band_delete'),
    
]
