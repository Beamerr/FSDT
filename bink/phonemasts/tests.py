import unittest
from phonemastdata import open_csv

class CSVTest(unittest.TestCase):

    def setUp(self):
        self.data = "/Users/ian/FSDT/bink/MobilePhoneMasts.csv"

    def test_csv_read_data_titles(self):
        self.assertEqual(
            read_data(self.data)[0],['Property', 'Property Address [1]', 'Property Address [3]', 'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date', 'Lease Years', 'Current Rent']
            )

    def test_csv_read_data_property_name(self):
        self.assertEqual(read_data(self.data)[1][0], 'Beecroft Hill')

    def test_csv_read_current_rent(self):
        self.assertEqual(read_data(self.data)[5][0], '12000')

if __name__ == '__main__':
    unittest.main()