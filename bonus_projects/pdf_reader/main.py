import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    """Extract text from a PDF file and return it as a list of str"""

    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        # Display the amount of pages to the user
        print('Pages:', len(reader.pages))
        print('-'*10)  # Divider

        # Extract the text from each page
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def count_words(text_list: list[str]) -> Counter:
    # Flatten the lists
    all_words: list[str] = []
    for text in text_list:
        # Split each list into separate words without symbols
        split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        #print(split_message)

        # Lowercase each word in the split message
        lowered: list[str] = [word.lower() for word in split_message]

        # Flatten the list by appending to a new list
        for word in lowered:
            if word:
                all_words.append(word)

    # Return a counter object
    return Counter(all_words)


def main():
    # Extract text and create a counter
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')
    counter: Counter = count_words(extracted_text)

    # Show the text that we extracted
    for text in extracted_text:
        print(text)

    # Display the 5 most common words
    for word, mentions in counter.most_common(5):
        print(f'{word:10}: {mentions} times')


if __name__ == '__main__':
    main()
