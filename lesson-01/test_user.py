import unittest
from unittest import mock

from user import User
from vk_api import ApiError


class TestUser(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_init(self):
        usr = User("smith", 42)

        self.assertEqual("smith", usr.name)
        self.assertEqual(42, usr.age)

    def test_greetings(self):
        usr = User("smith", 42)

        self.assertEqual("smith", usr.name)
        self.assertEqual("Hello, smith!", usr.greetings())
        self.assertEqual("smith", usr.name)

    def test_greetings_empty(self):
        usr = User("", 42)

        self.assertEqual("", usr.name)
        self.assertEqual("Hello, !", usr.greetings())
        self.assertEqual("", usr.name)

    def test_birthday(self):
        usr = User("smith", 42)

        self.assertEqual(42, usr.age)
        self.assertEqual(43, usr.birthday())
        self.assertEqual(43, usr.age)

    def test_get_friends_simple(self):
        usr = User("smith", 42)
        usr.get_friends()

        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.return_value = []

            self.assertEqual([], usr.get_friends())
            expected_calls = [
                mock.call("/friends", "smith", None),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

            mock_fetch.return_value = ["fr1", "fr2"]

            self.assertEqual(["fr1", "fr2"], usr.get_friends())
            expected_calls = [
                mock.call("/friends", "smith", None),
                mock.call("/friends", "smith", None),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_get_friends_with_filter(self):
        usr = User("smith", 42)
        usr.get_friends()

        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.return_value = ["fr1", "fr2"]

            self.assertEqual(["fr1", "fr2"], usr.get_friends("fr"))
            expected_calls = [
                mock.call("/friends", "smith", "fr"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_get_friends_with_filter_partial(self):
        usr = User("smith", 42)
        usr.get_friends()

        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.return_value = ["fr1", "fr2"]

            self.assertEqual(["fr2"], usr.get_friends("2"))
            expected_calls = [
                mock.call("/friends", "smith", "2"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    @mock.patch("user.fetch_vk_api")
    def test_get_friends_with_filter_total(self, mock_fetch):
        usr = User("smith", 42)

        mock_fetch.return_value = ["fr1", "fr2"]

        self.assertEqual([], usr.get_friends("3"))
        expected_calls = [
            mock.call("/friends", "smith", "3"),
        ]
        self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_get_friends_several_calls(self):
        usr = User("smith", 42)
        usr.get_friends()

        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.side_effect = lambda *a: ["fr1"]

            self.assertEqual(["fr1"], usr.get_friends())
            expected_calls = [
                mock.call("/friends", "smith", None),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_get_friends_several_calls_list(self):
        usr = User("smith", 42)
        usr.get_friends()

        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.side_effect = [[], ["fr1", "fr2"], ["fr3"]]

            self.assertEqual([], usr.get_friends())
            self.assertEqual(["fr1", "fr2"], usr.get_friends())
            self.assertEqual(["fr3"], usr.get_friends())
            # self.assertEqual(["fr3"], usr.get_friends())

            expected_calls = [
                mock.call("/friends", "smith", None),
                mock.call("/friends", "smith", None),
                mock.call("/friends", "smith", None),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_get_friends_several_calls_if_error(self):
        usr = User("smith", 42)
        usr.get_friends()

        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.side_effect = ApiError("err509")

            with self.assertRaises(ApiError) as err:
                usr.get_friends()

            self.assertEqual("err509", str(err.exception))
            self.assertEqual(ApiError, type(err.exception))

            with self.assertRaises(Exception) as err:
                usr.get_friends()

            expected_calls = [
                mock.call("/friends", "smith", None),
                mock.call("/friends", "smith", None),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)
