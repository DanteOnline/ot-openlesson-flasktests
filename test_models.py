from database import db_session, init_db
from models import Category, get_categories_with_description
from faker import Faker


class TestModels:

    def setup(self):
        # Создавать данные
        init_db()

        db_session.query(Category).delete()
        db_session.commit()

        fake = Faker()
        for _ in range(5):
            name = fake.name()
            category = Category(name=name)
            db_session.add(category)

        for _ in range(5):
            name = fake.name()
            text = fake.text()
            category = Category(name=name, description=text)
            db_session.add(category)

        db_session.commit()

    def test_get_categories_with_description(self):

        # Тесты
        assert db_session.query(Category).count() == 10
        assert len(get_categories_with_description(db_session)) == 5
