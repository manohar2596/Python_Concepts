import requests
import json  # For JSON parsing
import unittest  # For test assertion

BASE_URL = "https://api.example.com"


class APITestCase(unittest.TestCase):
    def test_get_user(self):
        # Define the API endpoint
        endpoint = "/user/123"

        # Send a GET request to the API
        response = requests.get(BASE_URL + endpoint)

        # Assert the response status code (e.g., 200 for success)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        data = json.loads(response.text)

        # Perform additional assertions on the response data
        self.assertEqual(data["id"], 123)
        self.assertEqual(data["name"], "John Doe")

if __name__ == "__main__":
    unittest.main()
