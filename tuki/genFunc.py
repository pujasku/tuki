import json
import markdown

def loadConf(path):
    with open(path, 'r') as file:
        config = json.load(file)
    return config

def read_markdown_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        return file.read()

def convert_markdown_to_html(markdown_content):
    return markdown.markdown(markdown_content)