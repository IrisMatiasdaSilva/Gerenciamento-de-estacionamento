from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from estacionamento.api.serializers import CleinteSerializer, VeiculoSerializer, Cliente, Veiculo, Estacionamento, EstacionamentoSerializer

from users.models import UserProfileExample

class CleinteViewSet(ModelViewSet):
    serializer_class = CleinteSerializer
   
    queryset = Cliente.objects.all()




class VeiculoViewSet(ModelViewSet):
    serializer_class = VeiculoSerializer

    queryset = Veiculo.objects.all()



class EstacionamentoViewSet(ModelViewSet):
    serializer_class = EstacionamentoSerializer

    queryset = Estacionamento.objects.all()






