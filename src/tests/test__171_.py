from unittest import TestCase


class Test(TestCase):
    def test_change_making(self):
        from src.C0._174_ import change_making
        self.assertEqual(change_making(150), 2)
