import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with open('survey_results.txt', 'w', encoding='utf-8') as file:
            file.write('')

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_submit_survey(self):
        response = self.app.post('/submit', data=dict(
            name='John',
            age='25',
            question1='I like dumplings because they are tasty.',
            question2='I love Siberian dumplings.',
            question3='No, I would not like to turn into a dumpling.',
            question4='Once I ate 100 dumplings in one sitting.'
        ))
        self.assertEqual(response.status_code, 200)

    def test_survey_results_file(self):
        self.app.post('/submit', data=dict(
            name='John',
            age='25',
            question1='I like dumplings because they are tasty.',
            question2='I love Siberian dumplings.',
            question3='No, I would not like to turn into a dumpling.',
            question4='Once I ate 100 dumplings in one sitting.'
        ))
        with open('survey_results.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn('Name: John, Age: 25', content)
            self.assertIn('Question 1: I like dumplings because they are tasty.', content)
            self.assertIn('Question 2: I love Siberian dumplings.', content)
            self.assertIn('Question 3: No, I would not like to turn into a dumpling.', content)
            self.assertIn('Question 4: Once I ate 100 dumplings in one sitting.', content)

if __name__ == '__main__':
    unittest.main()