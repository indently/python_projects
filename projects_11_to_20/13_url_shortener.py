from typing import Final
import requests

# Constants
API_KEY: Final[str] = 'YOUR_KEY_HERE'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


# Function to shorten any link with a custom name
def shorten_link(full_link, custom_url):
    payload: dict = {'key': API_KEY, 'short': full_link, 'name': custom_url}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    print('')  # Adds an empty line

    # Gets the relevant information we need
    if url_data := data.setdefault('url'):
        if url_data['status'] == 7:
            title: str = url_data['title']
            short_link: str = url_data['shortLink']

            print('Title:', title)
            print('Link:', short_link)
        else:
            print('Error Status:', url_data['status'])


def main():
    # Take user input
    link: str = input('Enter a link: >> ')
    name: str = input('Give your link a title: >> ')

    # Shorten the link
    shorten_link(link, name)


if __name__ == '__main__':
    main()