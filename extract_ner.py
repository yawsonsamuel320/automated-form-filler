from flair.data import Sentence
from flair.models import SequenceTagger

# Load the pre-trained Flair NER model for English
tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

# Create empty lists to store your data
first_names = []
last_names = []
addresses = []
phones = []
dates_of_birth = []

def extract_info(text):
    # Initialize variables to store extracted information
    first_name = ""
    last_name = ""
    address = ""
    phone = ""
    date_of_birth = ""

    # Create a Flair sentence
    sentence = Sentence(text)

    # Run NER on the sentence
    tagger.predict(sentence)

    for entity in sentence.get_spans('ner'):
        print(entity)
        entity_text = entity.text
        entity_label = entity.tag

        if entity_label == 'DATE':
            date_of_birth = entity_text.strip()

        elif entity_label == 'LOC' or entity_label == 'GPE':
            address = entity_text.strip()

        elif entity_label == 'PERSON':
            if not first_name:
                first_name = entity_text.strip()
            else:
                last_name = entity_text.strip()

        elif entity_label == 'PHONE':
            phone = entity_text.strip()
        
        # Append the extracted information to your pre-defined lists as needed
        first_names.append(first_name)
        last_names.append(last_name)
        addresses.append(address)
        phones.append(phone)
        dates_of_birth.append(date_of_birth)

    return first_names, last_names, addresses, phones, dates_of_birth
