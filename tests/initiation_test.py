import pytest

from fraction.fraction import Fraction


class TestInitiation:

    @pytest.mark.parametrize("numerator, denominator, expected_numerator, expected_denominator", [
        (1, 5, 1, 5),
        (3, 6, 1, 2),
        (-2, 3, -2, 3),
        (3, -5, -3, 5),
        (-4, -7, 4, 7),
        (0, 1, 0, 1),
        (0, 4, 0, 1),
        (0, 1, 0, 1),
        (4, 2, 2, 1),
        (4, 4, 1, 1),
        (9, 2, 9, 2),
        (0, 7, 0, 1),
        ])
    def test_initiation(self, numerator, denominator, expected_numerator, expected_denominator):
        new_fraction = Fraction(numerator, denominator)
        assert new_fraction.numerator == expected_numerator and new_fraction.denominator == expected_denominator

    @pytest.mark.parametrize("numerator, denominator, expected_error, error_message", [
        (8, 0, ArithmeticError, "Denominator can't be zero."),
        (3, None, AttributeError, "Denominator can't be None for Fraction object. Pass 1 in case of whole number."),
    ])
    def test_initiation_with_exception(self, numerator, denominator, expected_error, error_message):
        with pytest.raises(expected_error) as error:
            Fraction(numerator, denominator)

        assert error_message in str(error.value)
