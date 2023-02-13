# import libraries
import spacy
nlp = spacy.load('en_core_web_md')

# def functions

def watch_next(description):
    '''
    This function returns the film with the most similar description.
    It iterates to compare for the highest similarity values.
    
    '''
    contents = []
    titles = []
    sim_list = []
    with open("movies.txt", "r") as f:
        for line in f:
            split_line = line.split(":")
            contents.append(split_line[1])
            titles.append(split_line[0])
    model_sentence = nlp(description)
    for sentence in contents:
        similarity = nlp(sentence).similarity(model_sentence)
        sim_list.append(similarity)
        print(similarity)
    return titles[sim_list.index(max(sim_list))]

print(watch_next('''
Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.
'''))

