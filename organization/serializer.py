from .models import Organization, Project, Tag, Link, Photo, Contact
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'links']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['name', 'url']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'contact_text']

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'name', 
            'country',
            'place',
            'tags',
            'description',
            'url',
            'projects',
            'contacts'
        ]

class OrganizationEssentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'name', 
            'country',
            'place',
            'tags',
        ]
