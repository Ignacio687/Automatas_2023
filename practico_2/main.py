'''Utilizando el lenguaje de programación Python, implementar la validación de las 
expresiones regulares del ejercicio anterior'''

import re
import unittest
import parameterized

class FormatValidator():
    def date(self, date):
        return True
    
    def number(self, number):
        return True

    def yt_video(self, video):
        return True

    def mail(self, mail):
        return True

    def phone(self, phone):
        return True

    def cuil(self, cuil):
        return True

    def password(self, password):
        return True

class FormatValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = FormatValidator()

    @parameterized.expand(["", "",])
    def test_date_True(self, parameter):
        self.assertTrue(self.app.date(parameter))
    
    @parameterized.expand(["", "",])
    def test_date_False(self, parameter):
        self.assertFalse(self.app.date(parameter))

    @parameterized.expand(["", "",])
    def test_number_True(self, parameter):
        self.assertTrue(self.app.number(parameter))
    
    @parameterized.expand(["", "",])
    def test_number_False(self, parameter):
        self.assertFalse(self.app.number(parameter))
    
    @parameterized.expand(["", "",])
    def test_yt_video_True(self, parameter):
        self.assertTrue(self.app.yt_video(parameter))
    
    @parameterized.expand(["", "",])
    def test_yt_video_False(self, parameter):
        self.assertFalse(self.app.yt_video(parameter))

    @parameterized.expand(["", "",])
    def test_mail_True(self, parameter):
        self.assertTrue(self.app.mail(parameter))
    
    @parameterized.expand(["", "",])
    def test_mail_False(self, parameter):
        self.assertFalse(self.app.mail(parameter))

    @parameterized.expand(["", "",])
    def test_phone_True(self, parameter):
        self.assertTrue(self.app.phone(parameter))
    
    @parameterized.expand(["", "",])
    def test_phone_False(self, parameter):
        self.assertFalse(self.app.phone(parameter))

    @parameterized.expand(["", "",])
    def test_cuil_True(self, parameter):
        self.assertTrue(self.app.cuil(parameter))
    
    @parameterized.expand(["", "",])
    def test_cuil_False(self, parameter):
        self.assertFalse(self.app.cuil(parameter))

    @parameterized.expand(["", "",])
    def test_password_True(self, parameter):
        self.assertTrue(self.app.password(parameter))
    
    @parameterized.expand(["", "",])
    def test_password_False(self, parameter):
        self.assertFalse(self.app.password(parameter))

if __name__ == "__main__":
    unittest.main()