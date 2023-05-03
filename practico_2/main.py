"""Utilizando el lenguaje de programación Python, implementar la validación de las 
expresiones regulares del ejercicio anterior"""

import re
import unittest
from parameterized import parameterized
import re


class FormatValidator:
    def date(self, date):
        exp = r"^(0?[1-9]|[12][0-9]|3[01])([/-])(0?[1-9]|1[012])\2(\d{4})$"
        regex = re.compile(exp)
        return regex.match(date) 

    def number(self, number):
        regex = re.compile(r"^((\d{1,3})[.])*(\d{3}),(\d{2})$")
        return regex.match(number) 

    def yt_video(self, video):
        regex = re.compile(r"([\w-]{11})$")
        result = regex.search(video)
        return regex.match(video) 

    # TOOOM
    def mail(self, mail):
        # Cuenta de Email de alumno de la Universidad de Mendoza
        regex = re.compile(r"^([a-z]{1,2})\.[a-z]+@alumno\.um\.edu\.ar$")
        return regex.match(mail) 

    def phone(self, phone):
        regex = re.compile(r"^54[023]\d\d(\d){7}$")
        return regex.match(phone) 

    # nACho
    def cuil(self, cuil):
        regex = re.compile(r"^(20|23|24|27|30)\-(\d){8}\-\d$")
        return regex.match(cuil) 

    def password(self, password):
        regex = re.compile(r"^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()_+]).{8,16}$")
        return regex.match(password) 


class FormatValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = FormatValidator()

    @parameterized.expand(
        [
            "20/12/2020", 
            "03-02-9000", 
            "31/09/2020",
            "30-02-2017"
        ]
    )
    def test_date_True(self, parameter):
        self.assertTrue(self.app.date(parameter))

    @parameterized.expand(
        [
            "32/03/2147",
            "13/13/2147",
            "00/03/2147",
            "13/00/2147",
            "13/01/21478",
            "32-03-2147",
            "13-13-2147",
            "00-03-2147",
            "13-00-2147",
        ]
    )
    def test_date_False(self, parameter):
        self.assertIsNone(self.app.date(parameter))

    @parameterized.expand(
        [
            "123.432,12", 
            "900.001,01", 
            "4.123,12", 
            "50.000,00", 
            "1.000,00", 
            "1.000.000,00"
         ]
    )
    def test_number_True(self, parameter):
        self.assertTrue(self.app.number(parameter))

    @parameterized.expand(
        [
            "123.231,123", 
            "1234.123,12", 
            "412.1234,12"
        ]
    )
    def test_number_False(self, parameter):
        self.assertIsNone(self.app.number(parameter))

    @parameterized.expand(
        [
            "PR_ykicOZYU",
            "vw-KWfKwvTQ",
            "dA-K46f7wQV"
        ]
    )
    def test_yt_video_True(self, parameter):
        self.assertTrue(self.app.yt_video(parameter))
    @parameterized.expand(
        [
            "vw-KWfKwvTQ1",
            "vw%KWfKwvTQ",
            "wKWfKwvTQ",
        ]
    )
    def test_yt_video_False(self, parameter):
        self.assertIsNone(self.app.yt_video(parameter))

    @parameterized.expand(
        [
            "m.boldrini@alumno.um.edu.ar",
            "t.bourguet@alumno.um.edu.ar",
            "i.chavez@alumno.um.edu.ar",
            "l.brasolin@alumno.um.edu.ar"
        ]
    )
    def test_mail_True(self, parameter):
        self.assertTrue(self.app.mail(parameter))

    @parameterized.expand(
        [
            "matias.boldrini@alumno.um.edu.ar",
            "t.bourguet@alumno.um",
            "t.bourguet@alumno.ar.um.edu",
            "t.bourguet@alumno.um.edu.",
        ]
    )
    def test_mail_False(self, parameter):
        self.assertIsNone(self.app.mail(parameter))

    @parameterized.expand(
        [
            "542613449543",
            "542615345151",
            "540345494976"
        ]
    )
    def test_phone_True(self, parameter):
        self.assertTrue(self.app.phone(parameter))

    @parameterized.expand(
        [
            "5426134495430",
            "5326134495430",
            "539993449543",
            "54999344954",
        ]
    )
    def test_phone_False(self, parameter):
        self.assertIsNone(self.app.phone(parameter))

    @parameterized.expand(
        [
            "27-28033514-8",
            "23-44438082-9",
            "30-48137808-7",
            "30-00000000-8"
        ]
    )
    def test_cuil_True(self, parameter):
        self.assertTrue(self.app.cuil(parameter))

    @parameterized.expand(
        [
            "27-28033514-81",
            "27-280335148",
            "271-28033514-8",
            "2-28033514-8",
            "27-onononov-8",
        ]
    )
    def test_cuil_False(self, parameter):
        self.assertIsNone(self.app.cuil(parameter))

    @parameterized.expand(
        [
            "Hola%2002",
            "Visualcode_1",
            "HOLAc@p0",
        ]
    )
    def test_password_True(self, parameter):
        self.assertTrue(self.app.password(parameter))

    @parameterized.expand(
        [
            "Hola2002", 
            "Visual%Studio%Code", 
            "hola_2002", 
            "Hola_2", 
            "test"
        ]
    )
    def test_password_False(self, parameter):
        self.assertIsNone(self.app.password(parameter))


if __name__ == "__main__":
    unittest.main(failfast=True)
