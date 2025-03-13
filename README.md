# Web Scraper and Local Ollama Summarizer

This project provides a Python script that scrapes the content of any given website and then uses a locally running Ollama model to summarize the extracted text.

## Features

* **Website Scraping:** Extracts text content from any provided URL.
* **Local Ollama Integration:** Utilizes a locally hosted Ollama instance for text summarization.
* **Customizable Prompt:** Allows you to modify the summarization prompt for tailored results.
* **Simple Command-Line Interface:** Easy to use with minimal configuration.
* **Error Handling:** Basic error handling for common scraping and Ollama issues.

## Prerequisites

* **Python 3.6+:** Ensure you have Python installed.
* **Ollama:** Install and run Ollama with a suitable model (e.g., `llama2`, `mistral`). You can find instructions on how to install ollama on your operating system on the [ollama website](https://ollama.ai/).
* **Required Python Libraries:** Install the necessary libraries using pip:

    ```bash
    pip install requests beautifulsoup4 ollama
    ```

## Installation

1. **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

2. **Install dependencies (as described above).**

## Usage

1. **Run Ollama:** Start Ollama with your chosen model. For example:

    ```bash
    ollama run llama2
    ```

2. **Run the script:**

    ```bash
    python scraper_summarizer.py <URL> [optional: custom prompt]
    ```

    * `<URL>`: The website URL you want to scrape and summarize.
    * `[optional: custom prompt]`: A custom prompt to use for summarization. If not provided, a default prompt will be used.

    **Example:**

    ```bash
    python scraper_summarizer.py [https://www.example.com](https://www.example.com)
    python scraper_summarizer.py [https://www.example.com](https://www.example.com) "Summarize the main points concisely."
    ```

## Code Structure

* `scraper_summarizer.py`: The main script that performs website scraping and summarization.

## Code Explanation

```python
import requests
from bs4 import BeautifulSoup
import ollama
import sys

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = ' '.join(soup.stripped_strings)
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None

def summarize_text(text, prompt="Summarize the following text:"):
    try:
        response = ollama.chat(
            model='llama2', #change this to your model of choice.
            messages=[
                {
                    'role': 'user',
                    'content': f"{prompt}\n\n{text}"
                }
            ]
        )
        return response['message']['content']
    except ollama.exceptions.OllamaError as e:
        print(f"Error summarizing text: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scraper_summarizer.py <URL> [optional: custom prompt]")
        sys.exit(1)

    url = sys.argv[1]
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else "Summarize the following text:"

    scraped_text = scrape_website(url)
    if scraped_text:
        summary = summarize_text(scraped_text, custom_prompt)
        if summary:
            print("Summary:")
            print(summary)
