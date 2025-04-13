import requests
import json

class GetRequester:
    """A class to handle GET requests and JSON responses."""
    
    def __init__(self, url):
        """Initialize with the URL to request."""
        self.url = url

    def get_response_body(self):
        """Send GET request and return response body.
        
        Returns:
            str: The response body as text
            
        Raises:
            requests.exceptions.RequestException: If request fails
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.content  # Return response as bytes
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get response: {str(e)}")

    def load_json(self):
        """Get response body and parse as JSON.
        
        Returns:
            dict or list: Parsed JSON data
            
        Raises:
            ValueError: If response is not valid JSON
        """
        try:
            response_body = self.get_response_body()
            return json.loads(response_body)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {str(e)}")
