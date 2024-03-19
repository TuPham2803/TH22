from rest_framework import serializers
from courses.models import Category, Course, Lesson, Tag, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSeriliazer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url
        return rep


class CourseSerializer(ItemSeriliazer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'created_date', 'updated_date', 'category']


class LessonSerializer(ItemSeriliazer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date', 'updated_date']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        field = ['id', 'name']


class LessonDetailSerializer(LessonSerializer):
    tags = TagSerializer

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','username','password','avatar']
