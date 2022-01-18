from rest_framework import serializers
from .models import Gardener

class GardenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gardener
        fields = ('id', 'user', 'street', 'city', 'state', 'zipcode')


def register_gardener(self, validated_data):
    gardener= Gardener.objects.create(
        user = validated_data['user_id'],
        street = validated_data['street'],
        city = validated_data['city'],
        state = validated_data['state'],
        zipcode = validated_data['zipcode']
        )
    gardener.save()

    return gardener
# class UpdateGardenerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gardener
#         fields = ()
