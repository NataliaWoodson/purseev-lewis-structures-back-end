from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('querystatus', views.get_query_status, name='get'),
    # path('queryresults', views.get_query_results, name='query_results'),
]