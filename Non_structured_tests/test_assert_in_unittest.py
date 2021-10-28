import unittest

class WordTest(unittest.TestCase):

    def test_word(self):
        string = "Hi this is a string"
        self.assertIn("this", string)

    def test_word_in_list(self):
        language = ["Python", "C", "java", "ruby"]
        self.assertNotIn("R", language)

if __name__ =="__main__":
    from HtmlTestRunner import HTMLTestRunner
    testRunner = HTMLTestRunner(output="htmlreports")
    unittest.main(testRunner=testRunner)
    unittest.main()