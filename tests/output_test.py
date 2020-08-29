import pytest

from fraction.fraction import Fraction


class TestOutput:

    @pytest.mark.parametrize("a, b, expected_output", [
        (2, 3, "2/3"),
        (6, 9, "2/3"),
        (3, 2, "1 1/2"),
        (15, 5, "3"),
        (15, 6, "2 1/2"),
        (8, 7, "1 1/7"),
        (400, -200, "-2"),
        (2, -6, "-1/3"),
        (-25, 10, "-2 1/2"),
        (0, 1, "0"),
        ])
    def test_output(self, a, b, expected_output):
        new_fraction = Fraction(a, b)
        fraction_print = new_fraction.__str__()
        assert expected_output in fraction_print

