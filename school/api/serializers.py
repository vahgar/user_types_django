from rest_framework import serializers

from school.models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'school_name',
            'school_branch_area',
            'school_id',
        ]

class SchoolCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'school_name',
            'school_branch_area',
            'school_id',
        ]
