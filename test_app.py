import unittest
from unittest.mock import patch
from app import TestAPI


class TestApp(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """

    api = TestAPI("GEOPLUGIN")

    @patch("app.TestAPI.get_ip", return_value="192.168.0.1")
    def test_get(self, input):
        """
        Any method that starts with 'test_' will be considered as a test case.
        """
        self.assertIsInstance(self.api.get(), dict)


if __name__ == "__main__":
    unittest.main()
