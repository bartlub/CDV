import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # przygotowanie do testu / warunki wstępne
        print("Test przygotowany")
        pass

    def testGoogleSearch(self):
        # właściwy test
        print("Test wykonany")
        pass

    def tearDown(self):
        # sprzątanie po teście
        print("Posprzątane")
        pass

    if (__name__ == '__main__'):
        unittest.main()
