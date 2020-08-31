from math import gcd, floor, ceil  # gcd - Greatest Common Devisor


class Fraction:

    @staticmethod
    def __lcm__(a, b):
        """Least Common Multiple"""
        return (a * b) // gcd(a, b)

    def reduce(self):
        fraction_gcd = gcd(self.numerator, self.denominator)
        if fraction_gcd != 1:
            self.numerator //= fraction_gcd
            self.denominator //= fraction_gcd

    def __init__(self, numerator: int, denominator: int) -> object:
        """

        :type numerator: int
        :type denominator: int
        """
        if denominator == 0:
            raise ArithmeticError("Denominator can't be zero.")
        elif denominator is None:
            raise AttributeError("Denominator can't be None for Fraction object. Pass 1 in case of whole number.")

        if numerator * denominator < 0:
            sign = -1
        else:
            sign = 1

        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator == 0:
            self.numerator = 0
            self.denominator = 1
        elif numerator == denominator:
            self.numerator = 1
            self.denominator = 1
        else:
            self.numerator = numerator
            self.denominator = denominator
            self.reduce()

        self.numerator *= sign

    def __str__(self):
        display_string = ''

        if self.numerator < 0:
            display_string += '-'

        a = abs(self.numerator)
        b = self.denominator

        if a == b:
            display_string += '1'
            return display_string
        elif a > b:
            if a % b == 0:
                display_string += str(a // b)
                return display_string
            else:
                display_integer = a // b
                display_numerator = a % b
                display_denominator = b

                if a != 0:
                    reduced = Fraction(display_numerator, display_denominator)
                    reduced.reduce()
                    display_numerator = reduced.numerator
                    display_denominator = reduced.denominator

                display_string += '{} {}/{}'.format(display_integer, display_numerator, display_denominator)
                return display_string
        else:
            display_string += '{}/{}'.format(a, b)
            return display_string

    def __add__(self, other):

        sum_numerator = 0
        sum_denominator = 1

        if isinstance(other, Fraction):
            if self.denominator == 1:
                if other.denominator == 1:
                    sum_numerator = self.numerator + other.numerator
                else:
                    sum_denominator = other.denominator
                    sum_numerator = self.numerator * other.denominator + other.numerator
            elif other.denominator == 1:
                sum_denominator = self.denominator
                sum_numerator += self.numerator

            elif self.denominator == other.denominator:
                sum_numerator += self.numerator + other.numerator
                sum_denominator = self.denominator
            else:
                sum_denominator = Fraction.__lcm__(self.denominator, other.denominator)
                sum_numerator = (self.numerator
                                 * (sum_denominator // self.denominator)
                                 + other.numerator
                                 * (sum_denominator // other.denominator))

        elif isinstance(other, int):
            sum_denominator = self.denominator
            sum_numerator += other * sum_denominator
            sum_numerator += self.numerator
        else:
            message = 'Operation {} + {} is not implemented yet.'.format(self, other)
            raise NotImplementedError(message)

        sum_of_fractions = Fraction(sum_numerator, sum_denominator)
        return sum_of_fractions

    def __sub__(self, other):

        if isinstance(other, Fraction):
            subtraction_denominator = other.denominator
            subtraction_numerator = (-1) * other.numerator
            subtraction = Fraction(subtraction_numerator, subtraction_denominator)

            difference = self + subtraction

        elif isinstance(other, int):
            difference = self + (-1) * other

        else:
            message = 'Operation {} - {} is not implemented yet.'.format(self, other)
            raise NotImplementedError(message)

        return difference

    def __mul__(self, other):

        product_numerator = self.numerator
        product_denominator = self.denominator

        if isinstance(other, Fraction):
            product_numerator *= other.numerator
            product_denominator *= other.denominator

        elif isinstance(other, int):
            product_numerator *= other

        else:
            message = 'Operation {} * {} is not implemented yet.'.format(self, other)
            raise NotImplementedError(message)

        product = Fraction(product_numerator, product_denominator)
        return product

    def __truediv__(self, other):
        message = 'Operation {} / {} is not implemented yet.'.format(self, other)
        raise NotImplementedError(message)

    def __int__(self):
        if self.numerator == 0:
            return 0
        elif self.numerator > 0:
            return floor(self.numerator / self.denominator)
        else:
            return ceil(self.numerator / self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

