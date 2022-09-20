import unittest

from cron_parser import parse_string, valid_value_range


class TestCronParser(unittest.TestCase):

    def test_every_hour(self):
        assert parse_string("*","hour") == " ".join(str(c) for c in valid_value_range["hour"])

    def test_interval_hour(self):
        assert parse_string("7-9","hour") == "7 8 9"

    def test_list_month(self):
        assert parse_string("7,9","month") == "7 9"

    def test_interval_day(self):
        assert parse_string("7/9","day") == "7 16 25"

    def test_interval_minute(self):
        assert parse_string("*/20","minute") == "0 20 40"

    def test_single_minute(self):
        assert parse_string("20","minute") == "20"