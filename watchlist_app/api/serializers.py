from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamingPlatform, Review


class ReviewsSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("movie", )


class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = "__all__"


class WatchlistSerializer(serializers.ModelSerializer):
    # platform = StreamingPlatformSerializer(many=True, read_only=True)
    Reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = "__all__"


# def validate_name(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name too short")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [validate_name])
#     director = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.director = validated_data.get('director', instance.director)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

# def validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name too short")
#     else:
#         return value
