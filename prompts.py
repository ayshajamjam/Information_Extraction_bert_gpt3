prompt1 = """ Given a sentence, extract from it all instances of the following relationship types as possible in the format (PERSON, UNIVERSITY).
PERSON is the subject and UNIVERSITY is the object and the PERSON attended UNIVERSITY. 
Seperate each result on a new line with no spaces before or after the result.

Example: ('Jeff Bezos', 'Princeton University')

Sentence: {}

Output: """


prompt2 = """ Given a sentence, extract from it all instances of the following relationship types as possible in the format (PERSON, ORGANIZATION).
PERSON is the subject and ORGANIZATION is the object and the PERSON previously worked at or currently works at ORGANIZATION. 
Seperate each result on a new line with no spaces before or after the result.

Example: ('Alec Radford', 'OpenAI')

Sentence: {}

Output: """

prompt3 = """ Given a sentence, extract from it all instances of the following relationship types as possible in the format (PERSON, LOCATION).
PERSON is the subject and LOCATION is the object and the PERSON lives in LOCATION which can be a district, province, city, state, or country. 
Seperate each result on a new line with no spaces before or after the result.

Example: ('Mariah Carey', 'New York City')

Sentence: {}

Output: """

prompt4 = """ Given a sentence, extract from it all instances of the following relationship types as possible in the format (ORGANIZATION, PERSON).
ORGANIZATION is the subject and PERSON is the object and the PERSON is a top member employee of the ORGANIZATION. 
Seperate each result on a new line with no spaces before or after the result.

Example: ('Nvidia', 'Jensen Huang')

Sentence: {}

Output: """
