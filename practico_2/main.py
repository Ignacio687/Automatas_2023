"""Utilizando el lenguaje de programación Python, implementar la validación de las 
expresiones regulares del ejercicio anterior"""

import re
import unittest
from parameterized import parameterized
import re


class FormatValidator:
    def __init__(self):
        self.digit = "(0|1|2|3|4|5|6|7|8|9)"
        self.num = "(1|2|3|4|5|6|7|8|9)"
        self.minus = "(a|b|c|d|e|...|x|y|z)"
        self.mayus = "(A|B|C|D|E|...|X|Y|Z)"
        self.Ascii = (
            "( ! | \" | # | $ | % | & | ' | - | _ | @ | * | + | , | - | . | /  | … )"
        )

    def date(self, date):
        exp = f"((0|1|2)({self.digit})|30|31)(/|-)(({self.digit}{self.num})|10|11|12)(/|-)({self.digit*4})"
        regex = re.compile(exp)
        return regex.match(date)

    def number(self, number): 
        regex = re.compile(r"jpg|png|gif|bmp|svg")
        return regex.match(number)

    def yt_video(self, video): 
        regex = re.compile(r"jpg|png|gif|bmp|svg")
        return regex.match(video)

# TOOOM
    def mail(self, mail): 
        regex = re.compile(r"jpg|png|gif|bmp|svg")
        return regex.match(mail)

    def phone(self, phone):
        regex = re.compile(r"jpg|png|gif|bmp|svg")
        return regex.match(phone)

# nACho
    def cuil(self, cuil):
        regex = re.compile(r"jpg|png|gif|bmp|svg")
        return regex.match(cuil)

    def password(self, password):
        regex = re.compile(r"jpg|png|gif|bmp|svg")
        return regex.match(password)


class FormatValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = FormatValidator()

    @parameterized.expand([("20/08/2020"),("23-02-9000"),])
    def test_date_True(self, parameter):
        self.assertTrue(self.app.date(parameter))

    @parameterized.expand(["32/03/2147", "02-00-2003",])
    def test_date_False(self, parameter):
        self.assertFalse(self.app.date(parameter))

    # @parameterized.expand(["", "",])
    # def test_number_True(self, parameter):
    #     self.assertTrue(self.app.number(parameter))

    # @parameterized.expand(["", "",])
    # def test_number_False(self, parameter):
    #     self.assertFalse(self.app.number(parameter))

    # @parameterized.expand(["", "",])
    # def test_yt_video_True(self, parameter):
    #     self.assertTrue(self.app.yt_video(parameter))

    # @parameterized.expand(["", "",])
    # def test_yt_video_False(self, parameter):
    #     self.assertFalse(self.app.yt_video(parameter))

    # @parameterized.expand(["", "",])
    # def test_mail_True(self, parameter):
    #     self.assertTrue(self.app.mail(parameter))

    # @parameterized.expand(["", "",])
    # def test_mail_False(self, parameter):
    #     self.assertFalse(self.app.mail(parameter))

    # @parameterized.expand(["", "",])
    # def test_phone_True(self, parameter):
    #     self.assertTrue(self.app.phone(parameter))

    # @parameterized.expand(["", "",])
    # def test_phone_False(self, parameter):
    #     self.assertFalse(self.app.phone(parameter))

    # @parameterized.expand(["", "",])
    # def test_cuil_True(self, parameter):
    #     self.assertTrue(self.app.cuil(parameter))

    # @parameterized.expand(["", "",])
    # def test_cuil_False(self, parameter):
    #     self.assertFalse(self.app.cuil(parameter))

    # @parameterized.expand(["", "",])
    # def test_password_True(self, parameter):
    #     self.assertTrue(self.app.password(parameter))

    # @parameterized.expand(["", "",])
    # def test_password_False(self, parameter):
    #     self.assertFalse(self.app.password(parameter))


if __name__ == "__main__":
    unittest.main()
