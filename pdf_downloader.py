from bs4 import BeautifulSoup
import requests
import re


def download(book_url, cookies):
    r = requests.get(book_url, cookies=cookies)

    soup = BeautifulSoup(r.content, 'html.parser')

    pdf_tag = str(soup.find_all('script')[-1])

    # checks of pdfObject is present and not in thrid party
    if pdf_tag.find('PDFObject.embed') >= 0:
        pdf_link = pdf_tag.split("\"")[1]

        book_title = soup.find('h1').text.strip().replace(
            '"', '').replace('/', '')

        download_response = requests.get(pdf_link)

        open(f'./pdfs/{book_title}.pdf',
             'wb').write(download_response.content)
