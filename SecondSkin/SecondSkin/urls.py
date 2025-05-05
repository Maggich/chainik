from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.popular_list, name='home'),
    path('<slug:slug>/', views.product_detail, name='detail'),  # ← вот правильно
]
