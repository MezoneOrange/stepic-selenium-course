import unittest

import lesson1_6_step10_findtext as find_text


class TestPages(unittest.TestCase):
    welcome_text = "Congratulations! You have successfully registered!"

    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        text = find_text.fill_form(link)
        self.assertEqual(text, self.welcome_text, "Expected be same texts")

    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        text = find_text.fill_form(link)
        self.assertEqual(text, self.welcome_text, "Expected be same texts")


if __name__ == "__main__":
    unittest.main()