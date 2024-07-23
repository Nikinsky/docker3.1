from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = "__all__"


class RatingSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    class Meta:
        model = Rating
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    author = UserProfileSerializers()
    class Meta:
        model = Review
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    ratings = RatingSerializers(many=True, read_only=True)
    reviews = ReviewSerializers(many=True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"