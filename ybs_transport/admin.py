from django.contrib import admin
from .models import Bus, Route, BusWithRoute, Stop, RouteWithStop

# Register your models here.
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(BusWithRoute)
admin.site.register(Stop)
admin.site.register(RouteWithStop)