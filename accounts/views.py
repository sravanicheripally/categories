from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Category, SubCategory, FieldName
from .serializers import CategorySerializer, SubCategorySerializer, FieldNameSerializer, FieldPhotoSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class SimpleLoginView(APIView):
    permission_classes = [AllowAny]  # anyone can access this endpoint

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Static credentials
        if username == "admin" and password == "admin123":
            return Response(
                {"message": "Login successful"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )



# Create/List Categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny] 


# Create/List SubCategories under a Category
class SubCategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    permission_classes = [AllowAny] 

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SubCategory.objects.filter(category_id=category_id)

    def perform_create(self, serializer):
        category_id = self.kwargs['category_id']
        serializer.save(category_id=category_id)


# Create/List Fields under a SubCategory
class FieldNameListCreateView(generics.ListCreateAPIView):
    serializer_class = FieldNameSerializer
    permission_classes = [AllowAny] 

    def get_queryset(self):
        subcategory_id = self.kwargs['subcategory_id']
        return FieldName.objects.filter(subcategory_id=subcategory_id)

    def perform_create(self, serializer):
        subcategory_id = self.kwargs['subcategory_id']
        serializer.save(subcategory_id=subcategory_id)


class FieldPhotoUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # handle file uploads
    permission_classes = [AllowAny] 

    def post(self, request, field_id):
        try:
            field = FieldName.objects.get(id=field_id)
        except FieldName.DoesNotExist:
            return Response({"error": "Field not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FieldPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(field=field)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
