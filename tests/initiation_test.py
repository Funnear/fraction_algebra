import pytest

from fraction.fraction import Fraction


class TestInitiation:

    @pytest.mark.parametrize("a, b, expected_numerator, expected_denominator", [
        (1, 5, 1, 5),
        (3, 6, 1, 2),
        (-2, 3, -2, 3),
        (3, -5, -3, 5),
        (-4, -7, 4, 7),
        (0, 1, 0, 1),
        (0, 4, 0, 1),
        (0, None, 0, 1),
        (4, 2, 2, 1),
        (4, 4, 1, 1),
        (9, 2, 9, 2),
        (0, 7, 0, 1),
        ])
    def test_initiation(self, a, b, expected_numerator, expected_denominator):
        new_fraction = Fraction(a, b)
        assert new_fraction.numerator == expected_numerator and new_fraction.denominator == expected_denominator

    def test_initiation_with_exception(self):
        with pytest.raises(ArithmeticError) as error:
            Fraction(8, 0)

        assert "Denominator can't be zero" in str(error.value)

