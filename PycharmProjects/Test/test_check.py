import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # przygotowanie do testu / warunki wstępne
        pass

    def testGoogleSearch(self):
        # właściwy test
        pass

    def tearDown(self):
        # sprzątanie po teście
        pass

    if (__name__ == '__main__'):
        unittest.main()