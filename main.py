import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
from ollama import chat
from ollama import ChatResponse
from scraper import Website

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
                    please provide a short summary of this website in markdown. \
                    If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

def summarize(url):
    website = Website(url)
    response: ChatResponse = chat(model='llama3.2', messages=messages_for(website))
    return response.message.content

def display_summary(url):
    summary = summarize(url)
    # display(Markdown(summary))
    return summary


print(display_summary("https://edwarddonner.com"))