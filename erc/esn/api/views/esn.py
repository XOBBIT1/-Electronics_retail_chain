from django.db.models import Avg, F
from esn.models import Factory, IndividualEntrepreneur, Dealership, Distributor, LargeRetailChain
from esn.api.serializers.esn import FactorySerializer, DealershipSerializer, \
    DistributorSerializer, LargeRetailChainSerializer, IndividualEntrepreneurSerializer
from rest_framework import generics, viewsets, views, status
from rest_framework.response import Response


class FactoryView(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class IndividualEntrepreneurView(viewsets.ModelViewSet):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class DebtIndividualEntrepreneurView(views.APIView):
    serializer_class = IndividualEntrepreneurSerializer

    def get(self, request):
        debt_awg = IndividualEntrepreneur.objects.all().aggregate(Avg(F('debt')))
        all_data = IndividualEntrepreneur.objects.filter(debt__lte=debt_awg['debt__avg'])

        serializer = self.serializer_class(all_data, many=True)

        new_data = serializer.data

        return Response(new_data, status=status.HTTP_200_OK)


class DebtDealershipView(views.APIView):
    serializer_class = DealershipSerializer

    def get(self, request):
        debt_awg = Dealership.objects.all().aggregate(Avg(F('debt')))
        all_data = Dealership.objects.filter(debt__lte=debt_awg['debt__avg'])

        serializer = self.serializer_class(all_data, many=True)

        new_data = serializer.data
        return Response(new_data, status=status.HTTP_200_OK)


class DebtDistributorView(views.APIView):
    serializer_class = DistributorSerializer

    def get(self, request):
        debt_awg = Distributor.objects.all().aggregate(Avg(F('debt')))
        all_data = Distributor.objects.filter(debt__lte=debt_awg['debt__avg'])

        serializer = self.serializer_class(all_data, many=True)

        new_data = serializer.data
        return Response(new_data, status=status.HTTP_200_OK)


class DebtLargeRetailChainView(views.APIView):
    serializer_class = LargeRetailChainSerializer

    def get(self, request):
        debt_awg = LargeRetailChain.objects.all().aggregate(Avg(F('debt')))
        all_data = LargeRetailChain.objects.filter(debt__lte=debt_awg['debt__avg'])

        serializer = self.serializer_class(all_data, many=True)

        new_data = serializer.data
        return Response(new_data, status=status.HTTP_200_OK)


class DealershipView(viewsets.ModelViewSet):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class DistributorView(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class LargeRetailChainView(viewsets.ModelViewSet):
    queryset = LargeRetailChain.objects.all()
    serializer_class = LargeRetailChainSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)

