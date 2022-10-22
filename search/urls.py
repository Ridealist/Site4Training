from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

from .api.views import TrainList

app_name = 'search'

urlpatterns = [
    path('', views.Search, name='search'),
    path('results/', views.SearchResult, name='results'),
    # path('api/v1/trainings/', TrainList.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)