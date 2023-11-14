import unittest
import sys
import io

from copy import deepcopy
from json import load, dump
from datetime import date, timedelta
from unittest.mock import patch

from real_estate import template, main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = None

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch(
        "builtins.input",
        side_effect=[
            "1600 Pennsylvania Ave NW",
            "",
            "Washington",
            "DC",
            "20500",
            "54,900",
            "5",
            "35",
            "3 Kitchens | 28 fireplaces | 3 elevators | 8 staircases",
            "n",
        ],
    )
    def testMainDoesntChangeTemplate(self, mock_stdout, mock_input):
        tomorrow = date.today() + timedelta(days=1)
        orig_template = deepcopy(template)

        main()

        self.assertEqual(orig_template, template)

        with open("1600-Pennsylvania-Ave-NW.json") as json_file:
            output = load(json_file)
            self.assertEqual(
                output,
                {
                    "listing_date": str(tomorrow),
                    "property": {
                        "address": {
                            "street_1": "1600 Pennsylvania Ave NW",
                            "street_2": "",
                            "city": "Washington",
                            "state": "DC",
                            "zip": "20500",
                        },
                        "square_footage": 54900,
                        "bedrooms": 5,
                        "bathrooms": 35,
                        "ammenities": [
                            "3 Kitchens",
                            "28 fireplaces",
                            "3 elevators",
                            "8 staircases",
                        ],
                    },
                    "broker": {
                        "name": "Tonya Sullivan",
                        "license_number": "ABCD1234",
                        "address": {
                            "street_1": "100 Fake St",
                            "street_2": None,
                            "city": "Boston",
                            "state": "MA",
                            "zip": "90210",
                        },
                        "referrer": None,
                    },
                },
            )

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch(
        "builtins.input",
        side_effect=[
            "1600 Pennsylvania Ave NW",
            "",
            "Washington",
            "DC",
            "20500",
            "54,900",
            "5",
            "35",
            "3 Kitchens | 28 fireplaces | 3 elevators | 8 staircases",
            "Y",
            "Kevin Bacon",
        ],
    )
    def testMainHandlesReferrer(self, mock_stdout, mock_input):
        tomorrow = date.today() + timedelta(days=1)
        orig_template = deepcopy(template)

        self.assertIsNotNone(orig_template)

        main()

        self.assertEqual(orig_template, template)

        with open("1600-Pennsylvania-Ave-NW.json") as json_file:
            output = load(json_file)

            self.assertEqual(
                output,
                {
                    "listing_date": str(tomorrow),
                    "property": {
                        "address": {
                            "street_1": "1600 Pennsylvania Ave NW",
                            "street_2": "",
                            "city": "Washington",
                            "state": "DC",
                            "zip": "20500",
                        },
                        "square_footage": 54900,
                        "bedrooms": 5,
                        "bathrooms": 35,
                        "ammenities": [
                            "3 Kitchens",
                            "28 fireplaces",
                            "3 elevators",
                            "8 staircases",
                        ],
                    },
                    "broker": {
                        "name": "Tonya Sullivan",
                        "license_number": "ABCD1234",
                        "address": {
                            "street_1": "100 Fake St",
                            "street_2": None,
                            "city": "Boston",
                            "state": "MA",
                            "zip": "90210",
                        },
                        "referrer": "Kevin Bacon",
                    },
                },
            )

def gather_property_info():
    print("Address")
    street_1 = input("Street 1: ")
    street_2 = input("Street 2: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP: ")

    print("\nDetails")
    square_footage = int(input("Square Footage: ").replace(",", ""))
    bedrooms = int(input("Bedrooms: "))
    bathrooms = int(input("Bathrooms: "))
    ammenities = list(
        map(str.strip, input("Ammenities (use | between items): ").split("|"))
    )

    return {
        "address": {
            "street_1": street_1,
            "street_2": street_2,
            "city": city,
            "state": state,
        "zip": zip_code,
        },
        "square_footage": square_footage,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "ammenities": ammenities,
    }

def gather_referrer_info():
    has_referrer = input("Was there a referrer? (Y or n): ")
    if has_referrer.lower().startswith("y"):
        return input("Referrer: ")
    else:
        return None

if __name__ == "__main__":
    unittest.main()
    output = copy.deepcopy(template)
    property_info = gather_property_info()
    referrer = gather_referrer_info()

    output["listing_date"] = str(date.today() + timedelta(days=1))
    output["property"] = property_info
    output["broker"]["referrer"] = referrer

    output_file_name = property_info["address"]["street_1"].replace(" ", "-") + ".json"

    print(output)

    with open(output_file_name, "w") as output_file:
        dump(output, output_file)
        print(f"Created {output_file}")
