"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing,name='landing'),
    path('registration/',registration,name='registration'),
    # path('registerdata/',registerdata,name='registerdata'),
    path('show_data/',show_data,name='show_data'),
    path('login/',login, name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    # path('dashboard/admin_emp/',admin_emp,name='admin_emp'),
    path('dashboard/add_emp/',add_emp,name="add_emp"),
    path('dashboard/add_dept/',add_dept,name="add_dept"),
    path('dashboard/show-dept/', show_dept, name='show_dept'),
    path('dashboard/show-emp/', show_emp, name='show_emp'),
    path('dashboard/show-query/', show_query, name='show_query'),
    path('admindashboard/delete/<int:id>/',delete,name='delete'),
    path('admindashboard/edit_emp/<int:pk>/',edit_emp,name='edit_emp'),
    path('admindashboard/update_emp/<int:pk>/',update_emp,name='update_emp'),
    path('admindashboard/delete_dept/<int:id>/',delete_dept,name='delete_dept'),
    path('admindashboard/edit_dept/<int:pk>/',edit_dept,name='edit_dept'),
    path('admindashboard/update_dept/<int:pk>/',update_dept,name='update_dept'),
    path('admindashboard/reply_query/<int:id>/',reply_query,name='reply_query'),
    path('userdashboard/',userdashboard,name='userdashboard'),
    path('userdashboard/profile/',profile,name='profile'),
    path('userdashboard/query/',query,name='query'),
    path('userdashboard/query_status/',query_status,name='query_status'),
    path('userdashboard/all_query/',all_query,name='all_query'),
    path('userdashboard/query_data/',query_data,name='query_data'),
    path('userdashboard/edit_query/<int:pk>/',edit_query,name='edit_query'),
    path('userdashboard/delete_query/<int:pk>/',delete_query,name='delete_query'),
    path('userdashboard/Update_query/<int:pk>/',Update_query,name='Update_query'),
    path('userdashboard/query/search/',search,name='search'),
    path('userdashboard/query/reset/',reset,name='reset'),
    
    path('logout/',logout,name='logout'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
