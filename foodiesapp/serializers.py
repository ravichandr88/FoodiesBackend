from rest_framework import serializers

from .models import Food
from .models import Meal
from .models import BEVERAGES
from .models import COMBOS

from .models import Slider
from .models import Gallery






from django.contrib.auth import get_user_model





from .models import Consult



from django.core.mail import send_mail

class ConsultSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    
    def get_name(self,obj):
        return obj.name.username

    class Meta:
        model = Consult
        fields = ('id','name','from_email', 'subject','message')

        
        # fields = ('id', 'name', 'position', 'group', 'from_email', 'phone', 'describe', 'file', 'create_date')


        # def create(self, validate_data):
        #     instance = super(ConsultSerializer, self).create(validate_data)
        #     send_mail(
        #     'Instance {} has been created'.format(instance.pk),
        #     'Here is the message. DATA: {}'.format(validate_data),
        #     'from@example.com',
        #     ['ak080495@gmail.com'],
        #     fail_silently=False,)
        #     return instance




class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        return self.Meta.model.objects.create_user(**data)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'password1', 'password2',
            'first_name', 'last_name','email'
        )
        read_only_fields = ('id',)



















class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','name', 'price', 'pic','field']
        # read_only_fields = ['pic']



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id','name', 'price', 'pic','field']




class BEVERAGESSerializer(serializers.ModelSerializer):
    class Meta:
        model = BEVERAGES
        fields = ['id','name', 'price', 'pic','field']



class COMBOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = COMBOS
        fields = ['id','name', 'price', 'pic','field']



class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id','title', 'image', 'thumbImage', 'alt']
      

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id','title', 'image']
      

# class GallerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gallery
#         fields = ['id','title', 'image']



















# class ProfilePicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['pic']