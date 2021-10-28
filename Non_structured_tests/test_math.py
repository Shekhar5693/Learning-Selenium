import unittest

class TestMath(unittest.TestCase):
    def test_trial(self):
        #print("I am testing addition.")
        self.assertTrue(True)
    
    def test_additon(self):
        self.assertAlmostEqual(3.333, 3.33, 2)


#if __name__ == "__main__":
    #unittest.main()