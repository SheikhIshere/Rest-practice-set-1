from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    models = Person
    fields = ['name', 'age']