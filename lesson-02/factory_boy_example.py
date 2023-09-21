#! /usr/bin/env python3

# pip packages
# factory-boy==3.2.1
# Faker==8.8.1
from faker import Faker

def main():
    fake = Faker(locale="Ru_ru")
    for i in range(5):
        doc = {
            'name': fake.name(),
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country(),
            'text': fake.sentence()
        }
        print(doc)

if __name__ == "__main__":
    main()
