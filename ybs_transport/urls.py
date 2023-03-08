from rest_framework import routers

from ybs_transport.views import BusViewSet, RouteViewSet, BusWithRouteViewSet, RouteWithStopViewSet, StopViewSet

router = routers.DefaultRouter()
router.register('bus', viewset=BusViewSet, basename='bus')
router.register('stop', viewset=StopViewSet, basename='stop')
router.register('route', viewset=RouteViewSet, basename='route')
router.register('bus_with_route', viewset=BusWithRouteViewSet, basename='bus_with_route')
router.register('route_with_stop', viewset=RouteWithStopViewSet, basename='route_with_stop')

# router.register('bus_with_route', viewset=BusWith, basename='bus_with_route')

urlpatterns = [
    # path('bus/', BusView.as_view())
]

urlpatterns += router.urls

# pip3 install psycopg2 gunicorn && pip3 freeze > requirements.txt
