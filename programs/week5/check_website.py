import sys
import requests

def check_website(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if 200 <= response.status_code < 400:
            print(f"The website at {url} is working (Status Code: {response.status_code}).")
        else:
            print(f"The website at {url} is not working (Status Code: {response.status_code}).")
    except requests.RequestException as e:
        print(f"Error: Could not connect to {url}. Details: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_website.py <URL>")
    else:
        check_website(sys.argv[1])

#python "d:\Dilasha\python\check_website.py" https://www.example.com for output
