from src.converters import convert_to_int


class TestConvertToInt(object):
    def test_with_no_comma(self):
        expected = 756
        actual = convert_to_int("756")
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_with_one_comma(self):
        expected = 2081
        actual = convert_to_int("2,081")
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_with_two_commas(self):
        expected = 1034891
        actual = convert_to_int("1,034,891")
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message

    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        message = f"Expected: None, Actual: {actual}"
        assert actual is None, message

    def test_on_string_with_incorrectly_placed_comma(self):
        actual = convert_to_int("12,72,891")
        message = f"Expected: None, Actual: {actual}"
        assert actual is None, message

    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        message = f"Expected: None, Actual: {actual}"
        assert actual is None, message

