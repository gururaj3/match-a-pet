from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import ShelterRegisterData, Pet, UserRegisterData, User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("accounts:register-shelter")
        self.dummy_user = User.objects.create(
            # is_shelter=True,
            username="peter7",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            address="5th Ave",
            city="Manhattan",
            state="New York",
            zip_code="11209",
            password="test123abc",
        )
        self.dummyy_user = User.objects.create(
            is_shelter=True,
            is_clientuser=False,
            username="peter77",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            phone="124356789",
            address="5th Ave",
            city="Manhattan",
            state="New York",
            zip_code="11209",
            latitude="12.90",
            longitude="13.47",
            password="test123abc",
        )
        self.dummy_shelterRegisterData = ShelterRegisterData.objects.create(
            user=self.dummy_user,
            shelter_profile_image="default.jpg",
        )
        self.assertEqual(str(self.dummy_shelterRegisterData), "peter7")

        self.user = {
            "is_shelter": True,
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password": "test123abc",
            # "password2": "test123abc",
        }
        self.shelter_user = {
            "is_shelter": True,
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }
        self.user_no_username = {
            "username": "",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_name_exists = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_email_exists = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_hm_invalid_email = {
            "username": "peter7",
            "email": "pet@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        return super().setUp


class TestViews(TestCase):

    # ** Home View, Login View and Logout View
    def test_home_view(self):
        client = Client()

        response = client.get(reverse("accounts:accounts-home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/home.html")

    def test_login_view(self):
        client = Client()

        response = client.get(reverse("accounts:login"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_logout_view(self):
        client = Client()

        response = client.get(reverse("accounts:logout"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/home.html")

    def test_shelter_login_post_view(self):
        client = Client()

        response = client.post(reverse("accounts:login"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_shelter_logout_post_view(self):
        client = Client()

        response = client.post(reverse("accounts:logout"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/home.html")

    # ** Shelter Views
    def test_shelter_register_view(self):
        client = Client()

        response = client.get(reverse("accounts:register-shelter"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_shelter_profile_view(self):
        client = Client()

        response = client.get(reverse("accounts:shelter-profile"))
        self.assertEquals(response.status_code, 302)

    # ** ClientUser Views
    def test_user_register_view(self):
        client = Client()

        response = client.get(reverse("accounts:register-user"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_user_profile_view(self):
        client = Client()

        response = client.get(reverse("accounts:user-profile"))
        self.assertEquals(response.status_code, 302)

    # ** Pet Views
    def test_pet_register_view(self):
        client = Client()

        response = client.get(reverse("accounts:pet-register"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pets.html")

    # ** User Views
    def test_shelter_register_post_view(self):
        client = Client()
        self.dummy_user = User.objects.create(
            username="peter7",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            address="5th Ave",
            city="Manhattan",
            state="New York",
            zip_code="11209",
            password="test123abc",
        )

        response = client.post(reverse("accounts:register-shelter"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")
        self.assertEquals(str(self.dummy_user.email), "peter@matchapet.com")
        self.assertEquals(str(self.dummy_user.username), "peter7")
        self.assertEquals(str(self.dummy_user.first_name), "Peter")
        self.assertEquals(str(self.dummy_user.last_name), "Voltz")
        self.assertEquals(str(self.dummy_user.address), "5th Ave")
        self.assertEquals(str(self.dummy_user.city), "Manhattan")
        self.assertEquals(str(self.dummy_user.state), "New York")
        self.assertEquals(str(self.dummy_user.zip_code), "11209")

    def test_browse_view_pets(self):
        client = Client()
        response = client.get(reverse("accounts:view-pets"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/view_pets.html")


class RegisterTestView(BaseTest):

    # Setup for the test

    def test_can_view_register_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_user_can_register_shelter(self):
        user_count = User.objects.count()
        response = self.client.post(
            self.register_url, self.shelter_user, format="text/html"
        )
        user_count = user_count + 1
        # self.assertEqual(User.objects.count(), user_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")
        # self.assertRedirects(
        #     response, reverse("accounts:login"), fetch_redirect_response=True
        # )

    def test_register_view_user_logged_in(self):
        user_login = self.client.login(
            username=self.dummyy_user.username, password="test123abc"
        )
        self.assertFalse(user_login)

    #     response = self.client.get(self.register_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(
    #         response, reverse("dashboard:dashboard"), fetch_redirect_response=False
    #     )


# class TestUserRegisterView(TestCase):
#     def test_view_register_page(self):
#         client = Client()

#         self.dummy_user = User.objects.create(
#                     username="peter7",
#                     email="peter@matchapet.com",
#                     first_name="Peter",
#                     last_name="Voltz",
#                     address="5th Ave",
#                     city="Manhattan",
#                     state="New York",
#                     zip_code="11209",
#                     password="test123abc",
#                 )

#         self.dummy_shelterRegisterData = ShelterRegisterData.objects.create(
#             user=self.dummy_user,
#             shelter_profile_image="default.jpg",
#         )

#         self.dummy_pet = Pet.objects.create(
#             shelterRegisterData = self.dummy_shelterRegisterData,
#             pet_name="Dog",
#             pet_breed="Shihtzu",
#             pet_age="4",
#             pet_color="White",
#             pet_gender="Female",
#         )

#         client.login(username=self.dummy_user.username, password="test123abc")
#         # response = client.get(reverse("accounts:pet-register"))
#         self.url = reverse("accounts:pet-register")
#         response = client.post(
#             self.url,
#             {
#                 "pet_name": "Sheila",
#                 "pet_breed": "Dog",
#                 "pet_age": "Baby",
#                 "pet_color": "White",
#                 "pet_gender": "Female",
#                 "pet_profile_image1": "default.jpg",
#                 "pet_profile_image2": "default.jpg",
#                 "pet_profile_image3": "default.jpg",
#             },
#         )
#         self.assertEqual(response.status_code, 200)

# def test_shelter_register_post_view1(self):
#     client = Client()
#     self.registerURL = reverse("accounts:register-shelter")
#     self.dummy_user = ShelterRegisterData.objects.create(
#         # shelter_id=5,
#         username="peter7",
#         email="peter@matchapet.com",
#         first_name="Peter",
#         last_name="Voltz",
#         shelter_city="Manhattan",
#         shelter_state="New York",
#         password="test123abc",
#     )

#     response = client.post(
#         self.registerURL,
#         {
#             "username": "peter7",
#             "email": "peter@matchapet.com",
#             "first_name": "Peter",
#             "last_name": "Voltz",
#             "shelter_city": "Manhattan",
#             "shelter_state": "New York",
#             "password1": "test123abc",
#             "password2": "test123abc",
#         },
#     )
#     self.assertEquals(response.status_code, 200)
#     self.assertTemplateUsed(response, "accounts/register.html")
#     self.assertEquals(str(self.dummy_user.email), "peter@matchapet.com")
#     self.assertEquals(str(self.dummy_user.username), "peter7")
#     self.assertEquals(str(self.dummy_user.first_name), "Peter")
#     self.assertEquals(str(self.dummy_user.last_name), "Voltz")
#     self.assertEquals(str(self.dummy_user.shelter_state), "New York")

# def test_shelter_update_post_view1(self):
#     client = Client()
#     self.registerURL = reverse("accounts:shelter-profile")
#     self.dummy_user = ShelterRegisterData.objects.create(
#         # shelter_id=5,
#         username="peter7",
#         email="peter@matchapet.com",
#         first_name="Peter",
#         last_name="Voltz",
#         shelter_city="Manhattan",
#         shelter_state="New York",
#         password="test123abc",
#     )

#     shelterid = ShelterRegisterData.objects.get(email="peter@matchapet.com")

#     response = client.post(self.registerURL, {})
#     self.assertEquals(response.status_code, 302)
#     self.assertEquals(shelterid.username, "peter7")
#     self.assertEquals(shelterid.email, "peter@matchapet.com")
#     self.assertEquals(str(self.dummy_user.email), "peter@matchapet.com")
#     self.assertEquals(str(self.dummy_user.username), "peter7")
#     self.assertEquals(str(self.dummy_user.first_name), "Peter")
#     self.assertEquals(str(self.dummy_user.last_name), "Voltz")
#     self.assertEquals(str(self.dummy_user.shelter_state), "New York")

# def test_pet_register_post_view(self):
#     client = Client()
#     self.dummy_user = ShelterRegisterData.objects.create(
#         email="peter@matchapet.com",
#     )
#     self.dummy_pet = Pet.objects.create(
#         id=self.dummy_user,
#         # pet_id="5",
#         pet_name="Sheila",
#         pet_breed="Dog",
#         pet_age="4",
#         pet_color="White",
#         pet_gender="Female",
#         # date_entered="12/1/2020",
#     )

#     petid = Pet.objects.get(pet_name="Sheila")
#     # shelterid = ShelterRegisterData.objects.get(shelter_id=5)

#     response = client.post(reverse("accounts:pet-register"), {})
#     self.assertEquals(response.status_code, 200)
#     self.assertEquals(str(petid.id), "peter@matchapet.com")
#     self.assertTemplateUsed(response, "accounts/pets.html")
#     self.assertEquals(str(self.dummy_pet.id), "peter@matchapet.com")

# def test_pet_register_post_view1(self):
#     client = Client()
#     self.dummy_user = ShelterRegisterData.objects.create(
#         email="peter@matchapet.com",
#     )
#     self.dummy_pet = Pet.objects.create(
#         email=self.dummy_user,
#         pet_id="5",
#         pet_name="Sheila",
#         pet_breed="Dog",
#         pet_age="4",
#         pet_color="White",
#         pet_gender="Female",
#         date_entered="12/1/2020",
#     )

#     response = client.post(reverse("accounts:pet-register"), {
#         "email":"peter@matchapet.com",
#         "pet_name": "Sheila",
#         "pet_breed": "Dog",
#         "pet_age": "4",
#         "pet_color": "White",
#         "pet_gender": "Female",
#         "date_entered": "12/1/2020",
#     })

#     petid = Pet.objects.get(pet_id=5)

#     self.assertEquals(response.status_code, 200)
#     self.assertTemplateUsed(response, "accounts/pets.html")
#     self.assertEquals(str(self.dummy_pet.email), "peter@matchapet.com")
#     self.assertEquals(self.dummy_pet.pet_name, "pet_name")
