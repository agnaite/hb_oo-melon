import random
import datetime

"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """ An abstract Calss for Melon Order"""


    def __init__(self, species=None, qty=0,order_type=None, tax=0):
        """ Initialize order attributes """

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

        if self.qty > 100:
            raise TooManyMelonsError("too many melons")
    
    def get_base_price(self):
        """This creates a base price for splurge pricing"""
        hours = datetime.datetime.now().time().hour
        day = datetime.date.today().weekday()
        splurge = random.randint(5, 9)
        # checks if hours are between 8AM-11AM and day is a weekday
        # if so, adds $4 to base price
        if hours in range(8, 11) and day in range(0, 5):
            splurge = splurge + 4
        return splurge

    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price = base_price * 1.5   
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total = total + 3
        return total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ Govenrment Melon Order """

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty, "government")
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """ This function has to pass in a Boolean which determined during inspection""" 
        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
     def __init__(self, value):
        super(TooManyMelonsError, self).__init__(value)


