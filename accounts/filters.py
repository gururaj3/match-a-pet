import django_filters
from django import forms
from .models import Pet


class PetFilter(django_filters.FilterSet):

    color_choices = (("Black", "Black"), ("White", "White"))
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    pet_color = django_filters.ChoiceFilter(choices=color_choices)
    pet_gender = django_filters.ChoiceFilter(choices=gender_choices)

    class Meta:
        model = Pet
        fields = ("pet_name", "pet_breed", "pet_color", "pet_gender")
