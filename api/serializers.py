from rest_framework.serializers import ModelSerializer
from api.models import Custom_Model


class Custom_Serializer(ModelSerializer):
    class Meta:
        model = Custom_Model
        fields = "__all__"
