import json
from rest_framework.test import APIClient, APITestCase
from shopinc.apps.product.models import Product


class BaseTest(APITestCase):
    def setUp(self):
        self.client = APIClient(content_type="application/json")
        self.product = Product(
            name="name", slug="name-123456d", description="asdfgh", price=1234,
            added_at="2019-2-19", updated_at="2019-4-12", image_url="sdfgh"
        )
        self.product = {
            "name": "product1",
            "description": "asdfgh", "slug": "name-123456d", "price": 1234, "added_at": "2019-2-19",
            "updated_at": "2019-4-12", "image_url": "sdfgh"
        }

    def create_product(self):
        return self.client.post("/api/products/", self.product)