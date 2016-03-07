from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^grades/$', views.StudentGradeList.as_view()),
    url(r'^grades/(?P<pk>[0-9]+)/$', views.StudentGradeDetail.as_view()),

]
