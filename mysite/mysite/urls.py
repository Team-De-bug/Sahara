"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from shop import views as shop_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from user import views as user_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',shop_views.cart, name='cart'),
    path('profile', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('signup/', user_views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    path('place', shop_views.place),
    path('remove', shop_views.remove),
    path('', shop_views.index, name="index"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
