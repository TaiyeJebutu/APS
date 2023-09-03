import unittest
import sys
sys.path.insert(1, '../02 Implementation')

from GetLocation import getLocation
from geopy import Location

class MyTestCase(unittest.TestCase):
    def test_can_get_a_str(self):
        # Arrange
        getLocationInstance = getLocation()

        # Act
        location = getLocationInstance.getCurrentLocation()

        # Assert
        assert type(location) == type("")


if __name__ == '__main__':
    unittest.main()

