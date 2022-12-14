from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.index),
    path('movies/<int:movie_id>/', views.detail, name='detail'),
    path('actors/', views.actor),
    path('actors/<int:movie_id>/',views.detail_actor),
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    path('movies/comments/<int:movie_id>/', views.comment_list),
    path('movies/recommend/', views.recommend),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]