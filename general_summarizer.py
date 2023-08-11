import openai
from split_text import SplitText
import sys
from dotenv import load_dotenv
import os
import chardet

load_dotenv('python.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

def read_file(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
        
        return rawdata.decode(encoding)


def create_list_of_texts(text):
    splitter = SplitText()
    splitter.print_text_length(text)
    return splitter.split_text(text)


def send_to_open_ai (texts, prompt, MODEL):
    sys_message = {"role": "system", "content" : prompt}
    response_list = []
    i = 0

    for text in texts:
        response = openai.ChatCompletion.create(
            model = MODEL,
            messages = [
                sys_message,
                {"role" : "user", "content" : text}
                        ],
            temperature = .3

        )
        i += 1
        print (f"We've summarized {i} sections of the text")
        response_list.append(response['choices'][0]['message']['content'])
    return response_list

def create_file(filename, responses):
     with open(filename, 'w', encoding ='utf-8') as file:
        if len(responses) > 1:
             file.write('\n'.join(responses))
        else: file.write(responses[0])

def summarize(input_path, 
              output_path, 
              prompt = 'Summarize the following', 
              MODEL = 'gpt-3.5-turbo'):
    text = read_file(input_path)
    texts = create_list_of_texts(text)
    responses = send_to_open_ai(texts, prompt, MODEL)
    create_file(output_path, responses)


#Put your files in here to just run and summarize.
if __name__ == "__main__":

    prompt = 'Summarize the following scene from a novel'
    input_path = 'MCW.txt'
    output_path = 'MCW_general_summary.txt'

    summarize(input_path, output_path, prompt = prompt)