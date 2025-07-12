from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'image_url']

class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    image_url = serializers.URLField(allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance
