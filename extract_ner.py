from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

# Define the model repo
model_name = "flair/ner-multi-fast"

# Download the model and tokenizer
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a NER pipeline
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

# Create empty lists to store your data
first_names = []
last_names = []
addresses = []
phones = []
dates_of_birth = []

# Define a function to capture the information from text using the Hugging Face Flair model
def extract_info(text,
                 first_names=first_names,
                 last_names=last_names,
                 addresses=addresses,
                 phones=phones,
                 dates_of_birth=dates_of_birth):
    # Initialize variables to store extracted information
    first_name = ""
    last_name = ""
    address = ""
    phone = ""
    date_of_birth = ""

    # Use the Hugging Face Flair NER model for prediction
    inputs = tokenizer(text, return_tensors="pt")
    
    # Apply nodel on tokenized input
    outputs = model(**inputs)
    
    print(outputs)

    # # Extract the information using Named Entity Recognition
    # for entity in results:
    #     entity_text = entity['word']
    #     entity_label = entity['entity']
        
    #     if entity_label == 'DATE':
    #         # DATE entity type for dates, which could include date of birth
    #         date_of_birth = entity_text.strip()

    #     elif entity_label == 'LOC':
    #         # LOC represents location entities, which could include addresses
    #         address = entity_text.strip()

    #     elif entity_label == 'PER':
    #         # PER entity type for persons, which could include first and last names
    #         if first_name:
    #             # If we already have a first name, assume the current entity is the last name
    #             last_name = entity_text.strip()
    #         else:
    #             first_name = entity_text.strip()

    #     elif entity_label == 'PHONE':
    #         # PHONE entity type (custom) for phone numbers
    #         phone = entity_text.strip()

    # # Append the extracted information to the pre-defined lists
    # first_names.append(first_name)
    # last_names.append(last_name)
    # addresses.append(address)
    # phones.append(phone)
    # dates_of_birth.append(date_of_birth)
