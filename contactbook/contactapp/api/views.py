from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models.functions import Lower

#models & serializers import
from contactapp.models import Contact
from contactapp.api.serializers import ContactSerializer


class ContactView(generics.ListCreateAPIView):    #for viewing & Creating Contacts
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all().order_by(Lower('name'))    #viewing the list in alphabetically order by ignoring case
    serializer_class = ContactSerializer

class ContactDescView(generics.RetrieveUpdateDestroyAPIView): # for individual viewing & Updating and deleting
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer