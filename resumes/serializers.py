from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'user', 'name', 'email', 'phone', 'education', 'experience', 'skills']
        read_only_fields = ['user']
