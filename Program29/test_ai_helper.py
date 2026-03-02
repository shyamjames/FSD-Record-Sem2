import unittest
import sys
import os

# Ensure the package is in the path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'ai_web_helper_pkg')))
from ai_web_helper.core import get_response, summarize_text, format_response

class TestAITools(unittest.TestCase):
    def test_format_response_markdown(self):
        """Test if format_response correctly converts markdown to HTML."""
        markdown_text = "This is a **test** of the *emergency* broadcast system."
        html = format_response(markdown_text)
        self.assertIn("<strong>test</strong>", html)
        self.assertIn("<em>emergency</em>", html)

    def test_missing_api_key_get_response(self):
        """Test get_response with an empty API key."""
        response = get_response("Hello", "")
        self.assertEqual(response, "Error: API Key is missing.")
        
    def test_missing_api_key_summarize(self):
         """Test summarize_text with an empty API key."""
         response = summarize_text("This is some text.", "")
         self.assertEqual(response, "Error: API Key is missing.")

if __name__ == '__main__':
    unittest.main()
