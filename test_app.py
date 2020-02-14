from app import app


class TestViews:

    # Каждый тест изолирован - не зависит от другого
    def setup(self):
        #print('Я выполняюсь перед каждый тестом')
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        # 1. Код ответа
        # 2. Права пользователя
        # 3. На странице есть данные
        # 4. Проверка как работают формы
        assert response.status_code == 200

    def test_contacts(self):
        assert 1 + 1 == 2

    def teardown(self):
        #print('А я после каждого теста')
        pass


