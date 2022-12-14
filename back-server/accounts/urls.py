from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # GET
    path('profile/<str:username>/', views.profile), # 프로필 뷰 접속
]