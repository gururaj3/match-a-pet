from django.contrib import admin
from .models import ClientUserPet
from import_export.admin import ImportExportModelAdmin


@admin.register(ClientUserPet)
class PetViewAdmin(ImportExportModelAdmin):
    pass
    list_display = (
        "id",
        "userRegisterData",
        "pet_name",
        "pet_breed",
        "pet_age",
        "pet_color",
        "pet_gender",
        "pet_profile_image1",
        "userRegisterData_id",
    )
    search_fields = (
        "userRegisterData",
        "pet_name",
        "pet_breed",
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    pass
