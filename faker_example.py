from faker import Faker
import random

fake = Faker()

print(fake.name())
print(fake.text())
print(random.random() * 100)
