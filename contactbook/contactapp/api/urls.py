from django.urls import path
from . import views
urlpatterns = [
    path('view/',views.ContactView.as_view(),name='contactview'),
    path('view/<int:pk>',views.ContactDescView.as_view(),name='contactdescview'), #for individual description
]