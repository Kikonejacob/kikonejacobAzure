from rest_framework import serializers
from models import student,grade

#Student serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('id','firstName','lastName','semester','className')

#grade serializers
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=grade
        fields=('userId','grade')
