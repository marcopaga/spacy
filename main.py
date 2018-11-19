import spacy

nlp = spacy.load('de')

# Process whole documents
text = (u"Düsseldorf ist eine Stadt in Deutschland. "
        u"Herr Klaus Schmidt ist ein kleiner Mann mit Hut und Fahrrad.")

doc = nlp(text)

# Find named entities, phrases and concepts
print("Entities")
for entity in doc.ents:
    print(entity.text, entity.label_)

print("Tokens")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)