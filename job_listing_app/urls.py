from django.urls import path

from . import views

app_name='job_listing_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_job, name='upload'),
    path('uploads/<path>/', views.index),
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'),
    
]