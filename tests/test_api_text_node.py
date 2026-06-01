import unittest

from api_text_node import ApiTextOutputNode


class ApiTextOutputNodeTest(unittest.TestCase):
    def test_returns_comfy_ui_and_result_payload(self):
        payload = ApiTextOutputNode().send_text_to_api("blue cotton shirt")

        self.assertEqual(payload["ui"]["text"], ["blue cotton shirt"])
        self.assertEqual(payload["result"], ("blue cotton shirt",))

    def test_coerces_non_string_values(self):
        payload = ApiTextOutputNode().send_text_to_api(42)

        self.assertEqual(payload["ui"]["text"], ["42"])
        self.assertEqual(payload["result"], ("42",))


if __name__ == "__main__":
    unittest.main()
