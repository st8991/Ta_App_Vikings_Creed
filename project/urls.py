# """project URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from proj_app.views import Login, Home, AccountManagement, AddAccount, DeleteAccount, EditAccount, ManageCourse, \
    AddCourse, AssignToCourse, SectionManagement
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('accounts/', AccountManagement.as_view()),
    path('addAccount/', AddAccount.as_view()),
    path('deleteAccount/<int:id>/', DeleteAccount.as_view()),
    path('editAccount/<int:id>/', EditAccount.as_view()),
    path('courses/', ManageCourse.as_view()),
    path('addCourse/', AddCourse.as_view()),
    path('assignToCourse/<int:id>/', AssignToCourse.as_view()),
    path('sections/<int:id>/', SectionManagement.as_view())
]

