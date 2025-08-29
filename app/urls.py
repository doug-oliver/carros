
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView, CarsListView, CarDetailView, UpdateCarView, DeleteCarView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),  # Assuming you have a register view
    path('login/', login_view, name='login'),  # Using Django's built-in login view for simplicity
    path('logout/', logout_view, name='logout'),  # Placeholder for logout view
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),  # Assuming you have a cars app with urls defined
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),  # Detail view for a specific car
    path('cars/<int:pk>/update/', UpdateCarView.as_view(), name='car_update'),  # Update view for a specific car
    path('cars/<int:pk>/delete/', DeleteCarView.as_view(), name='car_delete'),  # Delete view for a specific car
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
