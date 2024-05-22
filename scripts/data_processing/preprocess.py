import re

def clean_document(document):
    """
    Clean a single document by removing links, English words, and unnecessary whitespace.
    
    Args:
        document (str): The document text to clean.

    Returns:
        str: The cleaned document text.
    """
    if document is None:
        return ""  # Return an empty string if the document is None

    # Remove links
    document = re.sub(r'http\S+|www\S+|https\S+', '', document)
    # Remove English words
    document = re.sub(r'[a-zA-Z]', '', document)
    # Remove extra whitespace and unwanted characters
    document = re.sub(r'\s+', ' ', document).strip()
    return document
