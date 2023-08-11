import pytest

def test_openai_create_summary():
    docx_path = r"C:\Users\Dell Latitude 7400\OneDrive\Documents\test_docx.docx"    
    title = test_title

    openai_create_summary(docx_path, title)

    assert os.path.isfile(title + 'summary.txt')