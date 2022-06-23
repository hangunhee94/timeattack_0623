from unicodedata import category
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from item.models import Item as ItemModel
from item.models import Category as CategoryModel

from item.serializers import ItemSerializer
from item.serializers import CategorySerializer
# Create your views here.


class CategoryView(APIView):

    def get(self, request):

        categories = CategoryModel.objects.filter(
            name = "appliance"
        )

        serializer = CategorySerializer(categories, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)

class ItemView(APIView):

    def post(self, request):
        name =request.date.get("name","")
        category = request.data.get("category","")
        image_url = request.data.get("image_url","")

        item = ItemModel(
            **request.data
            )
        item.save()

        return Response({"message": "성공"} , status=status.HTTP_200_OK)