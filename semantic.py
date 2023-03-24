import spacy

nlp = spacy.load('en_core_web_md')

# example 1:
print("Similarity with Spacy:")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("dog")
word5 = nlp("animal")

print(f"{word1} - {word2}: ", word1.similarity(word2))
print(f"{word3} - {word2}: ", word3.similarity(word2))
print(f"{word3} - {word1}: ", word3.similarity(word1))
print(f"{word1} - {word4}: ", word1.similarity(word4))
print(f"{word1} - {word5}: ", word1.similarity(word5))
print(f"{word2} - {word5}: ", word2.similarity(word5))
print(f"{word3} - {word5}: ", word3.similarity(word5))
print(f"{word4} - {word5}: ", word4.similarity(word5))
print()

# Similarities between cat, apple, monkey, banana, dog and animal according to the examples:
# Cat and dog look most similar when compared to the others, maybe it's because they are both most common pet.
# Cat, dog and monkey are all animal but the highest similarity is between dog and animal.
# Banana and animal are the least similar words because they are in different categories.
# Apple and banana look similar because both of them fruit.

# example2:
print("Working with vectors:")
tokens = nlp("cat apple monkey banana dog animal")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print()

# example 3:
print("Working with sentences:")
sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my cat in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence, " - ", similarity)
print()

# If we run the examples with the simpler language model ‘en_core_web_sm’ instead of 'en_core_web_md' in the line 3, similarity will be different.
# Some of them will have higher similarity and some of them will have lower similarity.
# For example, banana and cat have 0.22358825939615987 similarity with model en_core_web_md.
# but they will have 0.6806929391210822 similarity if we use en_core_web_sm model.
# In similar way, similarity of dog and banana will increase from 0.18752224743366241 to 0.6650822758674622.

# On the other hand, similarity of dog and cat will decrease from 0.8220816850662231 to 0.5067517161369324.
# As a result, it can be said that en_core_web_md model is more successful than en_core_web_sm.
