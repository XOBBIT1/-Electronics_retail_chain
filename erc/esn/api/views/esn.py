import random

from django.db.models import Avg, F
from rest_framework import generics, views, status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from esn import tasks

from esn.models import ObjectModel
from esn.api.serializers.esn import ObjectSerializer


class ObjectView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = ObjectModel.objects.all().filter(name__gt=10)
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeleteObjectView(generics.RetrieveDestroyAPIView):
    queryset = ObjectModel.objects.all().filter(name__gt=10)
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)


class UpdateObjectView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = ObjectModel.objects.all().filter(name__gt=10)
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, pk):
        snippet = ObjectModel.objects.get(pk=pk)
        snippet.debt = random.randint(5, 500)
        serializer = ObjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)

class DebtObjectView(views.APIView):
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasks.updating_debt_task.delay()
        try:
            debt_awg = ObjectModel.objects.all().aggregate(Avg(F('debt')))
            all_data = ObjectModel.objects.all().filter(debt__gt=debt_awg['debt__avg'])

            serializer = self.serializer_class(all_data, many=True)
            serializer_data = serializer.data

            return Response(serializer_data, status=status.HTTP_200_OK)

        except Exception:
            return Response("No data", status=status.HTTP_200_OK)


class AllNetObjects(generics.ListAPIView):
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        country_name = kwargs.get("country")
        queryset = ObjectModel.objects.filter(contacts__address__country=country_name)
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)


class ProductObjects(generics.ListAPIView):
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        country_name = kwargs.get("product")
        queryset = ObjectModel.objects.filter(product__name=country_name)
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
