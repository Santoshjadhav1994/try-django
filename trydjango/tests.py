from django.test import TestCase
import os
from django.conf import settings

from django.contrib.auth.password_validation import validate_password


class TryDjangoConfigTest(TestCase):
    
    def test_secret_key_strength(self):
        # settings.SECRET_KEY
        SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
        # self.assertNotEqual(SECRET_KEY,'abc123')
        
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Weak Secret Key {e.message}"
            self.fail(msg)