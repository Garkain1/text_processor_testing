import unittest
from text_processor import TextProcessor


class TestTextProcessor(unittest.TestCase):

    def test_clean_text_removes_non_alpha(self):
        processor = TextProcessor("Hello, World!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "hello world")

    def test_clean_text_on_alphanumeric(self):
        processor = TextProcessor("123 ABC!!!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "abc")

    def test_clean_text_empty_string(self):
        processor = TextProcessor("")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "")

    def test_remove_stop_words(self):
        processor = TextProcessor("this is a test")
        processor.clean_text()
        processor.remove_stop_words(["this", "is"])
        self.assertEqual(processor.cleaned_text, "a test")

    def test_remove_stop_words_without_cleaning(self):
        processor = TextProcessor("this is a test")
        processor.remove_stop_words(["this", "is"])
        self.assertEqual(processor.cleaned_text, "a test")

    def test_remove_stop_words_no_stop_words(self):
        processor = TextProcessor("hello world")
        processor.clean_text()
        processor.remove_stop_words([])
        self.assertEqual(processor.cleaned_text, "hello world")

    def test_remove_stop_words_empty_text(self):
        processor = TextProcessor("")
        processor.remove_stop_words(["this", "is"])
        self.assertEqual(processor.cleaned_text, "")


if __name__ == '__main__':
    unittest.main()
