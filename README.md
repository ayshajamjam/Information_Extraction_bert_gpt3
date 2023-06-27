# OpenAI Information Extraction

## About
This project is about information extraction on the web, or the task of extracting "structured" information that is embedded in natural language text on the web. It was completed as part of my Advanced Database Systems course.

We implemented a version of the **Iterative Set Expansion (ISE) algorithm**. For a target information extraction task, we have an "extraction confidence threshold," a "seed query" for the task, and a desired number of tuples *k*. Using ISE, we start with the seed query (which corresponds to a plausible tuple for the relation to extract) and use it to return *k* tuples in line with the specified relation from web pages with at least the given extraction confidence.

## Learning

How to:

1. retrieve and parse webpages
2. prepare and annotate text on the webpages for subsequent analysis
3. extract structured information from the webpages

## Information Extraction

## Extracting information from websites

In order to retrieve a set of websites for a user-defined query, we used the Google Search Engine API to get the top-10 results. After extracting the URLs of these results, we used BeautifulSoup to scrape the HTML from the sites. Some websites block scrapers or an not accessible, and we handled these cases using try/except blocks, which just skip over such URLs.

While processing the URL, we remove tags that don't have useful information such as script, header, footer, style, nav, and meta. We then extract the useful content from the remaining tags and truncate the length to 10,000 characters for efficiency.

We feed this text to text_to_Sentences() to clean each sentence by removing extra spaces, newlines, tabs, etc.

### Approach 1: SpanBERT
This is a "traditional" information extraction approach, involving multiple steps of data annotation

### Approach 2: OpenAI's GPT-3 API
"one shot" learner. GPT-3 is a language model with 175 billion parameters. It does not involve gradient updates or fine-tuning. 

For this approach, we first used the spacy library to annotate sentences. We iterate through each sentence extracted from the HTML page and determine all possible candidate pairs of words where the subject and object fit the relation. For example, if the relation is "Works_For", we look for a subject=PERSON and object=ORGANIZATION. We filter candidate pairs to match the subject and object order. For each of the four relations, we define different prompts in prompts.py to send the OpenAI API. If a particular sentence has pairs that match the relation, we feed this sentence to gpt3.

## Setting Up the Project Locally

**Using python 3.7.x**

2. python3.7 -m venv "env"
3. source env/bin/activate
4. check version: python --version
5. env/bin/pip3 install google-api-python-client 
6. Install pip3 (unless already installed)
    - sudo apt update (VM only)
    - sudo apt install python3-pip (VM only)
7. Install Beautiful Soup:
    - pip3 install beautifulsoup4
8. Install spaCy library:
    - sudo apt-get update (VM only)
    - pip3 install -U pip setuptools wheel
    - pip3 install -U spacy
    - python3 -m spacy download en_core_web_lg
9. Download and run the pre-trained SpanBERT classifier
    - git clone https://github.com/zackhuiiiii/SpanBERT
    - cd SpanBERT
    - pip3 install -r requirements.txt
    - bash download_finetuned.sh
        - If this command doesn't work, first run: "brew install wget"
10. pip3 install openai
11. Install third party libraries for web scraping
    - pip3 install requests
    - pip3 install html5lib
    - pip3 install bs4
12. python3 -m spacy download en_core_web_sm


[Other Project Info (for owner only)](https://docs.google.com/document/d/1u1pGZR3K5LxIauEn7biBIdqLPfcykEySUdIrAZM5pAA/edit)


### Tools used

- **Google Custom Search API**
- **Beautiful Soup**: used to extract the actual plain text from a given webpage, and ignore HTML tags, links, images, and all other content that would interfere with the information extraction process
- **spaCy**: library used to process and annotate text through linguistic analysis (e.g., split sentences from paragraphs, tokenize text, detect named entities)
- **SpanBERT**: SpanBERT is a BERT-based relation classifier that considers as input (1) a sentence; (2) a subject entity from the sentence; and (3) an object entity from the sentence. SpanBERT then returns the predicted relation and the respective confidence value. We use it to extract the following four types of relations from text documents:
    1. Schools_Attended (internal name: per:schools_attended)
    2. Work_For (internal name: per:employee_of)
    3. Live_In (internal name: per:cities_of_residence)
    4. Top_Member_Employees (internal name: org:top_members/employees)

- **OpenAI GPT-3 API**: used to extract the above relations from text documents by exploiting large language models, as a state-of-the-art alternative to SpanBERT

### Input

**[-spanbert|-gpt3]** is either -spanbert or -gpt3, to indicate which relation extraction method we are requesting>
**<google api key>** is your Google Custom Search Engine JSON API Key (see above)
**<google engine id>** is your Google Custom Search Engine ID (see above)
**<openai secret key>** is your OpenAI API secret key (see above)
**<r>** is an integer between 1 and 4, indicating the relation to extract: 1 is for Schools_Attended, 2 is for Work_For, 3 is for Live_In, and 4 is for Top_Member_Employees
**<t>** is a real number between 0 and 1, indicating the "extraction confidence threshold," which is the minimum extraction confidence that we request for the tuples in the output; t is ignored if we are specifying -gpt3
**<q>** is a "seed query," which is a list of words in double quotes corresponding to a plausible tuple for the relation to extract (e.g., "bill gates microsoft" for relation Work_For)
**<k>** is an integer greater than 0, indicating the number of tuples that we request in the output