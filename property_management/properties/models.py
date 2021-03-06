"""
Provides models from which Django will generate the database

Primary key automatically provided by Django for each class
in the form: id = models.AutoField(primary_key=True)
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Property(models.Model):
    """
    Model for an individual property
    """
    # Property name
    name = models.CharField(max_length=255, default='House listing')

    # Property's full address
    address = models.CharField(max_length=255)

    # Property's house number
    house_number = models.CharField(max_length=255, default='')

    # Property's full street name
    street = models.CharField(max_length=255, default='')

    # Property's suburb location
    suburb = models.CharField(max_length=255, default='')

    # Property's state location
    state = models.CharField(max_length=255, default='')

    # Property postcode
    postcode = models.CharField(max_length=255, default='')

    # Rent cost
    rent_cost = models.IntegerField(default=0)

    # Property description
    description = models.TextField()

    # Are pets allowed in the property?
    pets_allowed = models.BooleanField(default=False)

    # Is the property furnished?
    furnished_state = models.BooleanField(default=False)

    # Is the property furnished, char field
    furnished_state_char = models.CharField(max_length=50, default='')

    # Property manager's contact information
    contact_information = models.TextField() # refactor into JSON field (maybe)

    # Simple link to an imgur file, if no input set to blank field
    image = models.CharField(max_length=128, blank=True, default='')
    image2 = models.CharField(max_length=128, blank=True, default='')
    image3 = models.CharField(max_length=128, blank=True, default='')

    # Number of bedrooms
    bedrooms = models.IntegerField(default=0)

    # Property type (house, apartment, etc.)
    property_type = models.CharField(max_length=50, blank=True, default='')

    # Number of bathrooms
    bathrooms = models.IntegerField(default=0)

    # Number of car spaces
    car_spaces = models.IntegerField(default=0)

    # Owner
    owner = models.ForeignKey(User, limit_choices_to={'groups__name': u'owners'}, blank=True, default=0)

    # Manager
    manager = models.ForeignKey(User, limit_choices_to={'groups__name': u'managers'}, related_name="manager", blank=True, default=0)

    # Tenant information
    tenant_information = models.TextField(blank=True, default='')

    # Contract information
    contract_information = models.TextField(blank=True, default='')

    # Identifies self as address name rather than 'Property Object'
    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Properties"
