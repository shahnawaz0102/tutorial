from django.urls import path
from contractor_app import views

urlpatterns = [
    path("register/",views.register),
    path("login/",views.user_login),
    path("index/",views.index),
    path("index2/",views.index2),
    path("my_view/",views.my_view),
    path('work_detail/', views.work_detail, name='work_detail'),
    path("contractor_detail/",views.contractor_detail),
    path('connect_to_contractor/', views.connect_contractor)
]
