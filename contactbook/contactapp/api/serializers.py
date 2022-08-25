
from rest_framework import serializers
from contactapp.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name','email','mob']
