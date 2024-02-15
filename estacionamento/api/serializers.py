from rest_framework import serializers
from estacionamento.models import Cliente, Veiculo, Estacionamento

class CleinteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veiculo
        fields = '__all__'

class EstacionamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estacionamento
        fields = '__all__'