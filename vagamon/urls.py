"""vagamon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home_page,tour_page,book_page,login_page,admin_page,logout_page,checkout_page,package_view,place_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name="Home_Page"),
    path('tour/',tour_page,name="Tour_Page"),
    path('book/',book_page,name="Book_Page"),
    path('login/',login_page,name="Login_Page"),
    path('admin-book/',admin_page,name="Admin_Page"),
    path('logout/',logout_page,name="Logout_Page"),
    path('checkout/',checkout_page,name="Checkout_Page"),
    path('packages/',package_view,name="Package_Page"),
    path('places/',place_page,name="Place_Page")

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
