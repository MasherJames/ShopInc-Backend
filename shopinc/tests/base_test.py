import json
from rest_framework.test import APIClient, APITestCase
from shopinc.apps.product.models import Product


class BaseTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = {
            "name": "product1",
            "description": "asdfgh", "slug": "name-123456d", "price": 1234,
            "added_at": "2019-2-19", "updated_at": "2019-4-12",
            "image_url": "sdfgh"
        }

        self.user = {
            "username": "Masher", "email": "masher@gmail.com",
            "password": "Password123"
        }

        self.invalid_username = {
            "username": "Ma", "email": "masher@gmail.com",
            "password": "Password123"
        }

        self.invalid_email = {
            "username": "Masher", "email": "mashergmail.com",
            "password": "Password123"
        }

        self.invalid_password = {
            "username": "Masher", "email": "masher@gmail.com",
            "password": "#@$%$^"
        }

        self.login_user_data = {
            "email": "masher@gmail.com",
            "password": "Password123"
        }

        self.slug = dict(self.create_product().data)['slug']

    def create_product(self):
        return self.client.post("/api/products/", self.product)

    def get_product(self):
        return self.client.get("/api/products/")

    def get_single_product(self):
        return self.client.get(f"/api/products/{self.slug}")

    def get_nonexisting_product(self):
        return self.client.get("/api/products/$%&*^(&&&&")

    def update_product(self):
        return self.client.put(f"/api/products/{self.slug}", self.product)

    def delete_product(self):
        return self.client.delete(f"/api/products/{self.slug}")

    def create_user(self):
        return self.client.post("/api/register/", self.user)

    def create_user_with_invalid_username(self):
        return self.client.post("/api/register/", self.invalid_username)

    def create_user_with_invalid_email(self):
        return self.client.post("/api/register/", self.invalid_email)

    def create_user_with_invalid_password(self):
        return self.client.post("/api/register/", self.invalid_password)

    def login_user(self):
        return self.client.post("/api/login/", self.login_user_data)
