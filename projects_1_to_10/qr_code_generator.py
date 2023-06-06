import qrcode  # Remember to install Pillow for colours


class MyQR:
    """A class that simplifies the creation of QR codes"""

    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        """
        Creates a qr code with some user customization

        :param file_name: The name/path of your qr code
        :param fg: The foreground colour
        :param bg: The background colour
        :return: None
        """

        # Get the user input
        # user_input: str = input('Enter text: ')
        user_input: str = 'This is an example'

        try:
            # Add the user input to the qr code and create it
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            # Display that it was successfully done
            print(f'Successfully created! ({file_name})')
        except Exception as e:
            print(f'Error: {e}')


def main():
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr(file_name='sample_qr.png',
                   fg='#48c9b0',
                   bg='white')


if __name__ == '__main__':
    main()
