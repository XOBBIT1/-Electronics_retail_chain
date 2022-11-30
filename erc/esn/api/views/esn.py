from django.db.models import Avg, F
from rest_framework import generics, views, status, viewsets
from rest_framework.response import Response
from esn.tasks import updating_debt_task

from esn.models import ObjectModel
from esn.api.serializers.esn import ObjectSerializer


class ObjectView(viewsets.ModelViewSet):
    queryset = ObjectModel.objects.all()
    serializer_class = ObjectSerializer


class DebtObjectView(views.APIView):
    serializer_class = ObjectSerializer

    def get(self, request):
        debt_awg = ObjectModel.objects.all().aggregate(Avg(F('debt')))
        all_data = ObjectModel.objects.filter(debt__gt=debt_awg['debt__avg'])
        updating_debt_task.delay()

        serializer = self.serializer_class(all_data, many=True)
        serializer_data = serializer.data

        return Response(serializer_data, status=status.HTTP_200_OK)


class AllNetObjects(generics.ListAPIView):
    serializer_class = ObjectSerializer

    def get(self, *args, **kwargs):
        country_name = kwargs.get("country")
        queryset = ObjectModel.objects.filter(contacts__address__country=country_name)
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
