from unittest import TestCase


class Test(TestCase):
    def test_parity(self):
        from src.C0._41_ import parity
        self.assertEqual(parity(8), 0)


class Test(TestCase):
    def test_remove_last_bit(self):
        from src.C0._41_ import remove_last_bit
        self.assertEqual(remove_last_bit(15), 14)


class Test(TestCase):
    def test_get_last_bit(self):
        from src.C0._41_ import get_last_bit
        self.assertEqual(get_last_bit(7), 1)


class Test(TestCase):
    def test_parity_by_xor(self):
        from src.C0._41_ import parity_by_xor
        self.assertEqual(parity_by_xor(7), 1)


class Test(TestCase):
    def test_true_if_power_of_two(self):
        from src.C0._41_ import true_if_power_of_two
        self.assertEqual(true_if_power_of_two(2), True)
