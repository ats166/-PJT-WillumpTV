from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import authenticate, get_user_model

from articles.models import Article

UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image
    profile_image = serializers.ImageField(use_url=True)
    nickname = serializers.CharField(required=True, write_only=True)
    age = serializers.IntegerField(required=True, write_only=True)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        print(f'data={data}')
        data['profile_image'] = self.validated_data.get('profile_image', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        data['age'] = self.validated_data.get('age', '')
        data['age'] = self.validated_data.get('age', '')
        print(f'data={data}')
        return data

# class UserDetailsSerializer(serializers.ModelSerializer):
    
#     class ArticleListSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Article
#             # fields = ('id', 'title', 'content')
#             fields = '__all__'
#             read_only_fields = ('user',)
    
    
#     articles = ArticleListSerializer(many=True, read_only=True)
    
     
#     class Meta:
#         extra_fields = []
#         if hasattr(UserModel, 'nickname'):
#             extra_fields.append('nickname')
#         if hasattr(UserModel, 'age'):
#             extra_fields.append('age')
        
#         if hasattr(UserModel, 'profile_image'):
#             extra_fields.append('profile_image')
#         if hasattr(UserModel, 'point'):
#             extra_fields.append('point')
#         if hasattr(UserModel, 'username'):
#             extra_fields.append('username')
#         if hasattr(UserModel, 'articles'):
#             extra_fields.append('articles')    

#         model = UserModel
#         fields = ('pk', *extra_fields,'articles',)
#         read_only_fields = ('email',)

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class ArticleListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            # fields = ('id', 'title', 'content')
            fields = '__all__'
            read_only_fields = ('user',)
    
    
    articles = ArticleListSerializer(many=True, read_only=True)
    
     
    class Meta:
        
        model = UserModel
        
        fields ='__all__'
        read_only_fields = ('email',)