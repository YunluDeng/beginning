####"https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3"#####
from google.cloud import language
import os
####Sentiment analysis####
def analyze_text_sentiment(text):

    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    x = ""
    for k, v in results.items():
        print(f"{k:10}: {v}")
        x = x + f"{k:10}: {v}\n"
    return x 

####Entity analysis####
def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    x = ""
    y = "=" * 80
    for entity in response.entities:
        print("=" * 80)
        x = x + y + "\n"
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")
            x = x + f"{k:15}: {v}\n"
        
    return x 

####Syntax analysis####
def analyze_text_syntax(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    fmts = "{:10}: {}"
    print(fmts.format("sentences", len(response.sentences)))
    x = fmts.format("sentences", len(response.sentences)) + '\n'
    print(fmts.format("tokens", len(response.tokens)))
    x = x + fmts.format("tokens", len(response.tokens)) + '\n'
    for token in response.tokens:
        print(fmts.format(token.part_of_speech.tag.name, token.text.content))
        x = x + fmts.format(token.part_of_speech.tag.name, token.text.content) + '\n'
    return x
####Content classification####
def classify_text(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)
    x = ''
    for category in response.categories:
        print("=" * 80)
        x = x + "=" * 80 + '\n'
        print(f"category  : {category.name}")
        x = x + f"category  : {category.name}" + '\n'
        print(f"confidence: {category.confidence:.0%}")
        x = x + f"confidence: {category.confidence:.0%}" + '\n'
    return x
