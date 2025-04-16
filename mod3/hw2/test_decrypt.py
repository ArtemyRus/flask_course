import unittest

from decrypt import decrypt

class TestDecryption(unittest.TestCase):
    def test_one_dot(self):
        test_cases = [
            ("абра-кадабра.", "абра-кадабра"),
            (".", ""),
        ]
        for (decr, encr) in test_cases:
            with self.subTest():
                self.assertEqual(decrypt(decr), encr)

    def test_two_dots(self):
        test_cases = [
            ("абраа..-кадабра", "абра-кадабра"),
            ("абраа..-.кадабра", "абра-кадабра"),
            ("абра--..кадабра", "абра-кадабра"),
            ("1..2.3", "23"),
        ]
        for (decr,encr) in test_cases:
            with self.subTest():
                self.assertEqual(decrypt(decr), encr)

    def test_many_dots(self):
        test_cases = [
            ("абрау...-кадабра", "абра-кадабра"),
            ("абра........", ""),
            ("абр......a.", "a"),
            ("1.......................", ""),
        ]
        for (decr, encr) in test_cases:
            with self.subTest():
                self.assertEqual(decrypt(decr), encr)
