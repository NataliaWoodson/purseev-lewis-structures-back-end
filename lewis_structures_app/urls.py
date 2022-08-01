from django.urls import include, path
from rest_framework import routers
from lewis_structures_app import views

router = routers.DefaultRouter()
router.register(r"molecules", views.MoleculeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/', views.index, name='index'),

    # path('molecule', views.index, name='index'),
    # path('querystatus', views.get_query_status, name='get'),
    # path('queryresults', views.get_query_results, name='query_results'),
]


