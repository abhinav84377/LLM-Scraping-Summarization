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
