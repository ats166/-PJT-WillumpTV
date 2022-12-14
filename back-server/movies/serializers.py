from .models import Movie,Genre,Actor,Comment
from rest_framework import serializers

        
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)

class MovieListSerializer(serializers.ModelSerializer):
    genres= GenreSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Movie
        # fields = ('genres_set','comment_name','genres',)
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        
class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'
        
        
class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('movie_id','name','character','profile_path',)


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie','user',)
        
class CommentListSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie','user',)
            