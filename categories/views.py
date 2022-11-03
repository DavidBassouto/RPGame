from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from skills.models import Skill


class CreateCategoryView(generics.CreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects