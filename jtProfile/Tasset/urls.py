from django.urls import path
from Tasset import views

urlpatterns = [
    path("", include("Tasset.urls")),
    path('admin/', admin.site.urls)
    
    #path("", views.home, name="home"),
    #path("map/", views.map, name="map"),
    #path("profile/", views.profile, name="profile"),
    #path("profile/<int:pk>/", views.profile_detail, name="profile_detail"),
    #path("inventory/", views.inventory, name="inventory"),
    #path("inventory/<int:pk>/", views.inventory_detail, name="inventory_detail"),
]