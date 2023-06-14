from rest_framework import  serializers

from store.models import product


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'