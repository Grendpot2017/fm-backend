from .models import Organization, Project, Tag, Link, Photo, Contact
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'links']

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'name', 'url']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'contact_text']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name', 
            'country',
            'place',
            'tags',
            'description',
            'url',
            'projects',
            'contacts'
        )

class OrganizationEssentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name', 
            'country',
            'place',
            'tags',
        )
