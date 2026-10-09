import io
import unittest
from unittest.mock import patch
import orderpizza


class TestMuttonPizza(unittest.TestCase):
    def test_mutton_pizza_in_menu(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            orderpizza.display_menu()
            output = mock_stdout.getvalue()
        self.assertIn("Mutton Pizza", output)
        self.assertIn("500", output)

    def test_order_mutton_pizza(self):
        inputs = ["6", "2", "7"]
        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            orderpizza.main()
            output = mock_stdout.getvalue()
        self.assertIn("Mutton Pizza", output)
        self.assertIn("2 x Mutton Pizza added to your order.", output)
