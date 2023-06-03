import os
import requests


def get_extension(image_url: str) -> str | None:
    # Create a list of popular extensions to check for
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    # Check that the extension exists inside the URL
    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None):
    """Download the image from any given url"""

    # Attempt to get the correct image extension from an url
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located...')

    # Check if the name already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')

    try:
        # Get the image as bytes and write it locally to our computer
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # Sample URLs
    # image_url_1: str = 'https://media.istockphoto.com/id/184276818/photo/red-apple.jpg?s=612x612&w=0&k=20&c=NvO-bLsG0DJ_7Ii8SSVoKLurzjmV0Qi4eGfn6nW3l5w=' # NOQA
    # image_url_2: str = 'https://w.wallhaven.cc/full/1p/wallhaven-1p398w.jpg'
    # image_url_3: str = 'https://www.svgrepo.com/show/376344/python.svg'

    # Get the user input for the download
    input_url: str = input('Enter a url: ')
    input_name: str = input('What would you like to name it?: ')

    # Download the image
    print('Downloading...')
    download_image(input_url, name=input_name, folder='images')
