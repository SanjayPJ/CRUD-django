import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'CRUDdjango.settings')

import django
django.setup()

import random
from view_controller.models import Demo
from faker import Faker

fakegen = Faker()

for i in range(20):
    fake_name = fakegen.name()
    fake_age = i
    user1 = Demo.objects.get_or_create(name = fake_name, age = fake_age)