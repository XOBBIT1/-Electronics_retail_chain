import random

from django.db.models import Avg, F
from rest_framework import generics, views, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from esn import tasks

from esn.models import ObjectModel
from esn.api.serializers.esn import ObjectSerializer


class ObjectView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):

    queryset = ObjectModel.objects.filter(name__gt=10)
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeleteObjectView(generics.RetrieveDestroyAPIView):
    queryset = ObjectModel.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)


class UpdateObjectView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = ObjectModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DebtObjectView(views.APIView):
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            serializer = self.serializer_class(
                ObjectModel.calculate_average_debt(), many=True
            )
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
        return Response(
            self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK
        )


class ProductObjects(generics.ListAPIView):
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        country_name = kwargs.get("product")
        queryset = ObjectModel.objects.filter(product__name=country_name)
        return Response(
            self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK
        )


class SendEmailView(generics.ListAPIView):
    serializer_class = ObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        queryset = ObjectModel.objects.all()
        serializer = self.serializer_class(queryset, many=True).data
        tasks.send_email_task.delay(serializer)
        return Response(
            f"Email was sent with data :{serializer}", status=status.HTTP_200_OK
        )
