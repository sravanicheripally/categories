from rest_framework import serializers
from .models import Category, SubCategory, FieldName, FieldPhoto

class FieldPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldPhoto
        fields = ["id", "image", "uploaded_at"]


class FieldNameSerializer(serializers.ModelSerializer):
    photos = FieldPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = FieldName
        fields = ["id", "name", "photos"]


class SubCategorySerializer(serializers.ModelSerializer):
    fields = FieldNameSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ["id", "name", "fields"]


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "subcategories"]
