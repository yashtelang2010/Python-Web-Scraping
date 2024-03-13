import requests
from bs4 import BeautifulSoup
from spellchecker import SpellChecker

def get_website_content(url):
    response = requests.get(url)
    return response.text

def extract_images(soup):
    images = soup.find_all('img')
    image_urls = [img['src'] for img in images]
    return image_urls

def find_spelling_mistakes(text):
    spell = SpellChecker()
    words = text.split()
    misspelled = spell.unknown(words)
    return list(misspelled)

def main():
    website_url = input("Enter the website URL: ")
    
    try:
        content = get_website_content(website_url)
        soup = BeautifulSoup(content, 'html.parser')
        
        image_urls = extract_images(soup)
        spelling_mistakes = find_spelling_mistakes(content)

        print("\nSpelling Mistakes:")
        print(spelling_mistakes)

        print("\nImage URLs:")
        print(image_urls)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
