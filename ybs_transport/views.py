from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from config.response_formatter import success, fail
from ybs_transport.models import Bus, Route, Stop, BusWithRoute, RouteWithStop
from ybs_transport.serielizer import BusSerializer, RouteSerializer, StopSerializer, BusWithRouteSerializer, \
    RouteWithStopSerializer


class BusViewSet(ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(serializer.data)
        else:
            return fail(serializer.errors)

    # /?name = Bus 21
    def list(self, request, *args, **kwargs):
        # checking for the parameters from the URL
        if request.query_params:
            items = self.queryset.filter(**request.query_params.dict())
        else:
            items = self.queryset

        # if there is something in items else raise error
        if items:
            serializer = BusSerializer(items, many=True)
            return success(serializer.data)
        else:
            return fail(status_code=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        # item = self.queryset.filter(**request.query_params.dict())
        item = get_object_or_404(Bus, pk=kwargs.get('pk'))
        # item = self.queryset.get(pk=kwargs.get('pk'))
        data = BusSerializer(instance=item, data=request.data)

        if data.is_valid():
            data.save()
            return success(data.data)
        else:
            return fail(data.errors)


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(serializer.data)
        else:
            return fail(serializer.errors)

    # /?name = Bus 21
    def list(self, request, *args, **kwargs):
        # checking for the parameters from the URL
        if request.query_params:
            items = self.queryset.filter(**request.query_params.dict())
        else:
            items = self.queryset

        # if there is something in items else raise error
        if items:
            serializer = self.serializer_class(items, many=True)
            return success(serializer.data)
        else:
            return fail(status_code=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        # item = self.queryset.filter(**request.query_params.dict())
        item = get_object_or_404(Bus, pk=kwargs.get('pk'))
        # item = self.queryset.get(pk=kwargs.get('pk'))
        data = RouteSerializer(instance=item, data=request.data)

        if data.is_valid():
            data.save()
            return success(data.data)
        else:
            return fail(data.errors)


class StopViewSet(ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(serializer.data)
        else:
            return fail(serializer.errors)

    # /?name = Bus 21
    def list(self, request, *args, **kwargs):
        # checking for the parameters from the URL
        if request.query_params:
            items = self.queryset.filter(**request.query_params.dict())
        else:
            items = self.queryset

        # if there is something in items else raise error
        if items:
            serializer = self.serializer_class(items, many=True)
            return success(serializer.data)
        else:
            return fail(status_code=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        # item = self.queryset.filter(**request.query_params.dict())
        item = get_object_or_404(Stop, pk=kwargs.get('pk'))
        # item = self.queryset.get(pk=kwargs.get('pk'))
        data = StopSerializer(instance=item, data=request.data)

        if data.is_valid():
            data.save()
            return success(data.data)
        else:
            return fail(data.errors)


class BusWithRouteViewSet(ModelViewSet):
    queryset = BusWithRoute.objects.all()
    serializer_class = BusWithRouteSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        # checking for the parameters from the URL
        if request.query_params:
            items = self.queryset.filter(**request.query_params.dict())
        else:
            items = self.queryset

        # if there is something in items else raise error
        if items:
            serializer = self.serializer_class(items, many=True)
            return success(serializer.data)
        else:
            return fail(status_code=status.HTTP_404_NOT_FOUND)


class RouteWithStopViewSet(ModelViewSet):
    queryset = RouteWithStop.objects.all()
    serializer_class = RouteWithStopSerializer
    permission_classes = []

    # def list(self, request, *args, **kwargs):
    #     # checking for the parameters from the URL
    #     if request.query_params:
    #         items = self.queryset.filter(**request.query_params.dict())
    #     else:
    #         items = self.queryset
    #
    #     # if there is something in items else raise error
    #     if items:
    #         serializer = self.serializer_class(items, many=True)
    #         return success(serializer.data)
    #     else:
    #         return fail(status_code=status.HTTP_404_NOT_FOUND)

# Create your views here.

# class BusView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         result = Bus.objects.all()
#         # serializers = StudentSerializer(result, many=True)
#         return Response({'status': 'success', "students": []}, status=200)
#
#     # def post(self, request):
#     #     serializer = StudentSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     #     else:
