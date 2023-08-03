# Author: Logan Dutton-Anderson

class Country:
    def __init__(self, country_name: str, capital_name: str, population: int):
        self.country_name = country_name
        self.capital_name = capital_name
        self.population = population

    def print_details(self):
        """
        :return: Returns the countries name, population and capital formatted as requested.

        Example: ("The capital of Canada (pop. 1234567) is OTTAWA")
        """

        return f"The capital of {self.country_name} (pop. {self.population}) is {self.capital_name}"

    def birth(self):
        """ Adds 1 to the population of the Country object. """
        self.population += 1

    def death(self):
        """ Removes 1 from the population of the Country object. """
        self.population -= 1

    def disaster(self):
        """
        For countries with a population of 100 million or higher, this method subtracts 100 million
        from the population. For smaller countries, it sets the population to 0.
        """
        if self.population >= 100000000:
            self.population -= 100000000
        else:
            self.population = 0
