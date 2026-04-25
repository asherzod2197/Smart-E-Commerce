from rest_framework import serializers
from .models import Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id', 'slug']
    

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description', 'category_id',
            'price', 'stock', 'image', 'is_available', 'created_at'
        ]
        read_only_fields = ['id', 'slug', 'created_at']
    

