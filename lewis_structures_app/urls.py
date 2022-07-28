from django.urls import include, path
from rest_framework import routers
from lewis_structures_app import views

router = routers.DefaultRouter()
router.register(r"electrons", views.ElectronViewSet)
router.register(r"atoms", views.AtomViewSet)
router.register(r"molecules", views.MoleculeViewSet)
# router.register(r"electrons/bond", views.ElectronViewSet.bond)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
