import requests

# Function to get data from a specified URL
def get_data():
    # URL of the resource to be fetched
    url = 'https://api.thecatapi.com/v1/images/search'
    
    # Headers to be sent with the request, including an authorization token
    headers = {'x-api-key': 'live_ocqzkph2EkDQqDtVOvAQR7pxX2wrhi73ZyEsNX6uZloKkjKimMZx4EfRek6Fny6j'}

    # Sending a GET request to the specified URL with headers
    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response as JSON and printing the data
        data = response.json()
        print(data)
    else:
        # Printing an error message if the request failed
        print(f"Failed to retrieve data: {response.status_code}")

# Ensuring the function runs only if the script is executed directly
if __name__ == "__main__":
    get_data()
