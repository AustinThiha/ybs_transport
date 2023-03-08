from django.db import models


# Create your models here.
class Bus(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    color_hash = models.CharField(max_length=10, blank=False, null=False)

    # charBlank = models.CharField(max_length=10, blank=True)
    # last_name = models.CharField(max_length=200)
    # address = models.CharField(max_length=200)
    # roll_number = models.IntegerField()
    # mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name + ' (' + self.color_hash + ')'


class Route(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Stop(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    latitude = models.FloatField(max_length=12, default=0.0)
    longitude = models.FloatField(max_length=12, default=0.0)

    def __str__(self):
        return self.name


class BusWithRoute(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, blank=False, null=False)
    route = models.ForeignKey('Route', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.bus.name + '(' + self.route.name + ')'

    class Meta:
        db_table = "ybs_bus_with_route"


class RouteWithStop(models.Model):
    stop = models.ForeignKey('Stop', on_delete=models.CASCADE, blank=False, null=False)
    route = models.ForeignKey('Route', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.stop.name + ' (' + self.route.name + ')'

    class Meta:
        db_table = "ybs_route_with_stop"
