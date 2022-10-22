from django.urls import path
from. import views

app_name = 'mypage'

urlpatterns = [
    path('', views.MyPageView.as_view(), name='mypage'),
    path('upload/', views.upload_file, name='upload'),
    path('upload/success/', views.upload_success, name='success'),
]