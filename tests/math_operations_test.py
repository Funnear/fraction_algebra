import pytest

from fraction.fraction import Fraction


class TestMathOperations:

    @pytest.mark.parametrize("first_operand, second_operand", [
        (Fraction(1, 2), 'a string'),
        (Fraction(1, 2), 2.09),
        (Fraction(1, 2), None),
        (Fraction(1, 2), Fraction),
    ])
    def test_sum_with_exception(self, first_operand, second_operand):
        with pytest.raises(NotImplementedError) as error:
            result = first_operand + second_operand
            print(result)

        assert "Operation {} + {} is not implemented yet.".format(first_operand, second_operand) in str(error.value)

    @pytest.mark.parametrize("first_operand, second_operand", [
        (Fraction(1, 2), 'a string'),
        (Fraction(1, 2), 2.09),
        (Fraction(1, 2), None),
        (Fraction(1, 2), Fraction),
    ])
    def test_mul_with_exception(self, first_operand, second_operand):
        with pytest.raises(NotImplementedError) as error:
            result = first_operand * second_operand
            print(result)

        assert "Operation {} * {} is not implemented yet.".format(first_operand, second_operand) in str(error.value)

    @pytest.mark.parametrize("first_operand, second_operand", [
        (Fraction(1, 2), 'a string'),
        (Fraction(1, 2), 2.09),
        (Fraction(1, 2), None),
        (Fraction(1, 2), Fraction),
    ])
    def test_sub_with_exception(self, first_operand, second_operand):
        with pytest.raises(NotImplementedError) as error:
            result = first_operand * second_operand
            print(result)

        assert "Operation {} * {} is not implemented yet.".format(first_operand, second_operand) in str(error.value)

    @pytest.mark.parametrize("first_operand, second_operand", [
        (Fraction(1, 2), Fraction(7, 5)),
        (Fraction(1, 2), 83),
        (Fraction(1, 2), 'a string'),
        (Fraction(1, 2), 2.09),
        (Fraction(1, 2), None),
        (Fraction(1, 2), Fraction),
    ])
    def test_div_with_exception(self, first_operand, second_operand):
        with pytest.raises(NotImplementedError) as error:
            result = first_operand / second_operand
            print(result)

        assert "Operation {} / {} is not implemented yet.".format(first_operand, second_operand) in str(error.value)

    @pytest.mark.parametrize("first_operand, second_operand, result_numerator, result_denominator", [
        (Fraction(0, 1), Fraction(2, 3), 2, 3),
        (Fraction(0, 1), Fraction(0, 1), 0, 1),
        (Fraction(1, 3), Fraction(2, 3), 1, 1),
        (Fraction(3, 11), Fraction(30, 11), 3, 1),
        (Fraction(2, 5), Fraction(2, 7), 24, 35),
        (Fraction(9, 3), Fraction(7, 8), 31, 8),
        (Fraction(6, 8), Fraction(0), 3, 4),
        (Fraction(1, -3), Fraction(2, 3), 1, 3),
        (Fraction(7, 8), Fraction(-6, 10), 11, 40),
        (Fraction(-7, 8), Fraction(-6, 10), -59, 40),
        (Fraction(7, 8), 25, 207, 8),
        (Fraction(-7, 3), 800, 2393, 3),
        (Fraction(-7, 3), -2, -13, 3),
        (Fraction(1, 2), True, 3, 2),
        (Fraction(6, 2), False, 3, 1),
    ])
    def test_sum(self, first_operand, second_operand, result_numerator, result_denominator):
        result_fraction = first_operand + second_operand
        assert result_fraction.numerator == result_numerator and result_fraction.denominator == result_denominator

    @pytest.mark.parametrize("first_operand, second_operand, result_numerator, result_denominator", [
        (Fraction(0, 1), Fraction(2, 3), -2, 3),
        (Fraction(0, 1), Fraction(0, 1), 0, 1),
        (Fraction(1, 1), Fraction(2, 7), 5, 7),
        (Fraction(5, 6), Fraction(2, 6), 1, 2),
        (Fraction(1, 7), Fraction(2, 7), -1, 7),
        (Fraction(-1, 7), Fraction(2, 7), -3, 7),
        (Fraction(-1, 7), Fraction(-2, 7), 1, 7),
        (Fraction(1, 7), Fraction(-2, 7), 3, 7),
        (Fraction(2, 3), Fraction(2, 7), 8, 21),
        (Fraction(18, 3), Fraction(2, 7), 40, 7),
        (Fraction(42, 5), Fraction(2, 5), 8, 1),
        (Fraction(1, 5), 2, -9, 5),
        (Fraction(4, 1), 2, 2, 1),
        (Fraction(1, 2), True, -1, 2),
        (Fraction(6, 2), False, 3, 1),
    ])
    def test_sub(self, first_operand, second_operand, result_numerator, result_denominator):
        result_fraction = first_operand - second_operand
        assert result_fraction.numerator == result_numerator and result_fraction.denominator == result_denominator

    @pytest.mark.parametrize("first_operand, second_operand, result_numerator, result_denominator", [
        (Fraction(0, 1), Fraction(2, 3), 0, 1),
        (Fraction(2, 3), Fraction(0, 1), 0, 1),
        (Fraction(5, 7), Fraction(1, 7), 5, 49),
        (Fraction(7, 5), Fraction(3, 2), 21, 10),
        (Fraction(3, 1), Fraction(1, 3), 1, 1),
        (Fraction(3, 10), Fraction(2, 5), 3, 25),
        (Fraction(1, 10), Fraction(2, 10), 1, 50),
        (Fraction(10, 1), Fraction(1, 2), 5, 1),
        (Fraction(10, 1), Fraction(1, 3), 10, 3),
        (Fraction(10, 1), 2, 20, 1),
        (Fraction(1, 10), 2, 1, 5),
        (Fraction(10, 1), 3, 30, 1),
        (Fraction(7, 5), True, 7, 5),
        (Fraction(7, 5), False, 0, 1),
        (Fraction(5, 5), Fraction(1, 3), 1, 3),
        (Fraction(2, 5), Fraction(-1, 3), -2, 15),
        (Fraction(-2, 5), Fraction(1, 3), -2, 15),
        (Fraction(-2, 5), Fraction(-1, 3), 2, 15),
    ])
    def test_mul(self, first_operand, second_operand, result_numerator, result_denominator):
        result_fraction = first_operand * second_operand
        assert result_fraction.numerator == result_numerator and result_fraction.denominator == result_denominator

