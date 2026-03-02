import unittest
from ai_web_helper_pkg.ai_web_helper.core import get_response, summarize_text, format_response

class TestAITools(unittest.TestCase):
    def test_format_response(self):
        markdown_text = "Hello **World**"
        html = format_response(markdown_text)
        self.assertIn("<strong>World</strong>", html)

    def test_missing_api_key(self):
        response = get_response("Hello", "")
        self.assertEqual(response, "Error: API Key is missing.")

if __name__ == '__main__':
    unittest.main()
