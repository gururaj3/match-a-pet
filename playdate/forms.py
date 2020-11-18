from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ClientUserPet


class ClientUserPetForm(forms.ModelForm):

    # shelter_id = forms.CharField(disabled = True)
    # email = forms.CharField(disabled = True)
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    age_choices = (
        ("Baby", "Baby"),
        ("Young", "Young"),
        ("Adult", "Adult"),
        ("Senior", "Senior"),
    )

    pet_age = forms.ChoiceField(choices=age_choices)
    pet_gender = forms.ChoiceField(choices=gender_choices)

    class Meta:
        model = ClientUserPet
        fields = [
            "pet_name",
            "pet_breed",
            "pet_age",
            "pet_color",
            "pet_gender",
            # "date_entered",
            "pet_profile_image1",
            "pet_profile_image2",
            "pet_profile_image3",
        ]
        labels = {
            "pet_profile_image1": ("Pet Profile Picture 1"),
            "pet_profile_image2": ("Pet Profile Picture 2"),
            "pet_profile_image3": ("Pet Profile Picture 3"),
        }
