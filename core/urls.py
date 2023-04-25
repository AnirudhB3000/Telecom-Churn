from django.urls import re_path
from core import views

urlpatterns=[
    re_path(r'^churn$',views.churnApi), #r is for routing
    re_path(r'^churn/([0-9]+)$', views.churnApi),
    re_path(r'^reviews$',views.ReviewApi),
    re_path(r'^reviews/([0-9]+)$', views.ReviewApi)
]