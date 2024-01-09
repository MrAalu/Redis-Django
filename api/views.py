from rest_framework.response import Response
from rest_framework import status
from api.models import Custom_Model
from rest_framework.views import APIView
from api.serializers import Custom_Serializer
from django.core.cache import cache


class Custom_View(APIView):
    def get(self, request):
        cache_name = "custom_model:all"

        isCached = cache.get(cache_name)

        if isCached != None:
            return Response(
                {
                    "success": True,
                    "CachedData": True,
                    "totalHits": len(isCached),
                    "data": isCached,
                },
                status=status.HTTP_200_OK,
            )

        else:
            # Using a Time Consuming Query
            model = Custom_Model.objects.filter(title__contains="lorem 949")
            serializer = Custom_Serializer(model, many=True)

            cache.set(cache_name, serializer.data, timeout=10)  # Timeout = 10Seconds

            return Response(
                {
                    "success": True,
                    "totalHits": len(serializer.data),
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
