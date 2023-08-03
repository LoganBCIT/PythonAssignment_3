# Author: Logan Dutton-Anderson

import random
import country

from data import countries_and_capitals


def main():
    try:
        all_countries = []
        for country_and_capital in countries_and_capitals:
            random_population = random.randrange(1000000, 1000000001)
            country_object = country.Country(country_and_capital[0], country_and_capital[1], random_population)
            all_countries.append(country_object)

        for country_object in all_countries:  # printing start details
            print(country_object.print_details())

        print('-------------------------------------------------------')

        for country_object in all_countries:  # printing details after every country gives birth
            country_object.birth()
            print(country_object.print_details())

        print('-------------------------------------------------------')

        for country_object in all_countries:  # printing details after every country has someone die
            country_object.death()
            print(country_object.print_details())

        print('-------------------------------------------------------')

        for country_object in all_countries:  # printing details after a disaster in each country
            country_object.disaster()
            print(country_object.print_details())

    except ValueError as e:
        print(str(e))
        print("oops")


if __name__ == '__main__':
    main()
