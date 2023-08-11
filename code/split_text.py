import tiktoken


class SplitText:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.encoding = tiktoken.encoding_for_model(model_name)

    def split_text(self, text, chunk_size=3500, overlap=100):
        encoded_text = self.encoding.encode(text)
        chunks = [encoded_text[i:i+chunk_size] for i in range(0, len(encoded_text), chunk_size - overlap)]
        decoded_chunks = [self.encoding.decode(chunk) for chunk in chunks]
        return decoded_chunks

    
    def print_text_length(self, text):
        encoded_text = self.encoding.encode(text)
        print (f'The text is {len(encoded_text)} tokens long')