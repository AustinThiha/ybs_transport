from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ybs_transport.models import Bus, Route, Stop, BusWithRoute, RouteWithStop


class BusSerializer(serializers.ModelSerializer):
    # , unique = True
    name = serializers.CharField(max_length=20, required=True)
    color_hash = serializers.CharField(max_length=10, required=True)

    class Meta:
        model = Bus
        # fields = ('id', 'name', 'color_hash')
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    default_error_messages = {'name_exists': 'The name already exists'}

    # , unique = True
    name = serializers.CharField(max_length=150, required=True)

    def create(self, validated_data):
        return Route.objects.get_or_create(**validated_data)[0]

    def validate(self, attrs):
        validated_attrs = super().validate(attrs)
        errors = {}

        # check if the new `name` doesn't exist for other db record, this is only for updates
        if (
                self.instance  # the instance to be updated
                and 'name' in validated_attrs  # if name is in the attributes
                and self.instance.name != validated_attrs['name']  # if the name is updated
        ):
            if (
                    Route.objects.filter(name=validated_attrs['name'])
                            .exclude(id=self.instance.id)
                            .exists()
            ):
                errors['name'] = self.error_messages['name_exists']

        if errors:
            raise ValidationError(errors)

        return validated_attrs

    class Meta:
        model = Route
        # fields = ('id', 'name')
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    # , unique = True
    name = serializers.CharField(max_length=150, required=True)
    latitude = serializers.FloatField(min_value=-1, required=True)
    longitude = serializers.FloatField(min_value=-1, required=True)
    default_error_messages = {'name_exists': 'The name already exists'}

    def create(self, validated_data):
        return Stop.objects.get_or_create(**validated_data)[0]

    def validate(self, attrs):
        validated_attrs = super().validate(attrs)
        errors = {}

        # check if the new `name` doesn't exist for other db record, this is only for updates
        if (
                self.instance  # the instance to be updated
                and 'name' in validated_attrs  # if name is in the attributes
                and self.instance.name != validated_attrs['name']  # if the name is updated
        ):
            if (
                    Stop.objects.filter(name=validated_attrs['name']).exclude(id=self.instance.id).exists()
            ):
                errors['name'] = self.error_messages['name_exists']

        if errors:
            raise ValidationError(errors)

        return validated_attrs

    class Meta:
        model = Stop
        # fields = ('id', 'name')
        fields = '__all__'


class BusWithRouteSerializer(serializers.ModelSerializer):
    route_id = serializers.IntegerField(write_only=True)
    bus_id = serializers.IntegerField(write_only=True)
    route = RouteSerializer(read_only=True)
    bus = RouteSerializer(read_only=True)

    # bus = models.ForeignKey('Bus', on_delete=models.CASCADE, blank=False, null=False)
    # route = models.ForeignKey('Route', on_delete=models.CASCADE, blank=False, null=False)
    # bus = serializers.CharField(required=True)

    class Meta:
        model = BusWithRoute
        fields = '__all__'


class RouteWithStopSerializer(serializers.ModelSerializer):
    stop_id = serializers.IntegerField(write_only=True)
    route_id = serializers.IntegerField(write_only=True)
    stop = StopSerializer(read_only=True)
    route = RouteSerializer(read_only=True)

    # stop = models.ForeignKey('Stop', on_delete=models.CASCADE, blank=False, null=False)
    # route = models.ForeignKey('Route', on_delete=models.CASCADE, blank=False, null=False)

    # bus = models.ForeignKey('Bus', on_delete=models.CASCADE, blank=False, null=False)
    # route = models.ForeignKey('Route', on_delete=models.CASCADE, blank=False, null=False)
    # bus = serializers.CharField(required=True)

    class Meta:
        model = RouteWithStop
        fields = '__all__'

    # def validate(self, attrs):
    #     validated_attrs = super().validate(attrs)
    #     errors = {}
    #
    #     # check if the new `name` doesn't exist for other db record, this is only for updates
    #     if (
    #             self.instance  # the instance to be updated
    #             and 'name' in validated_attrs  # if name is in the attributes
    #             and self.instance.name != validated_attrs['name']  # if the name is updated
    #     ):
    #         if (
    #                 Route.objects.filter(name=validated_attrs['name'])
    #                         .exclude(id=self.instance.id)
    #                         .exists()
    #         ):
    #             errors['name'] = self.error_messages['name_exists']
    #
    #     if errors:
    #         raise ValidationError(errors)
    #
    #     return validated_attrs
