import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Expected data points based on the provided quotes
        expected_data_point_ABC = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
        expected_data_point_DEF = ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)

        # Assertion for ABC stock
        self.assertEqual(getDataPoint(quotes[0]), expected_data_point_ABC)

        # Assertion for DEF stock
        self.assertEqual(getDataPoint(quotes[1]), expected_data_point_DEF)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Expected data points based on the provided quotes
        expected_data_point_ABC = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)
        expected_data_point_DEF = ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)

        # Assertion for ABC stock
        self.assertEqual(getDataPoint(quotes[0]), expected_data_point_ABC)

        # Assertion for DEF stock
        self.assertEqual(getDataPoint(quotes[1]), expected_data_point_DEF)

    """ ------------ Add more unit tests ------------ """

if __name__ == '__main__':
    unittest.main()
