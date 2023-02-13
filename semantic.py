import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))



tokens = nlp('cat apple monkey banana pumpkin halloween squash')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Note - the cat / monkey / banana trifecta.
# This is not that interesting:
# it just means that monkeys / bananas co-occur more than other pairs
# See new example pumpkin / squash / halloween
# Pumpkins and halloween co-occur  = higher similarity
# Note that 'squash' is polysemous (sport / vegetable)
# Running with other sports could be interesting

# Running with _sm gives a message about the model not having word vectors.
# The similarity scores are odd
# e.g. apple cat is more similar than monkey banana