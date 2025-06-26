"""
URL configuration for Draz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Draz import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.home ,name='home'),
    path('login/', views.login_page,name="login-page" ),
    path('signup/', views.sign_up,name="signup-page" ),
    path('<int:id>/', views.product_page,name="product-page" ),
    path('add-to-cart/<int:id>/', views.Add_to_card, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-quantity/<int:id>/', views.update_quantity, name='update_quantity'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.search_page, name='search'),           
    path('search/', views.header, name='header'),  
    path('logout/', views.logout_user, name='logout'),
    path('close-popup/', views.close_popup, name='close-popup'),
     path('pay/', views.payment_page, name='payment'),
    path('success/', views.payment_success, name='payment-success'),
    path('cancel/', views.payment_cancel, name='payment-cancel'),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)