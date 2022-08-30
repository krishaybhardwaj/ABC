from nltk.corpus import wordnet
from happytransformer import HappyTextToText, TTSettings

while True:
    val = input("Dictionary(d) or grammar(g): ")

    if val == 'd':
        user_input = input("Meaning - M, Synonyms - S, Antonyms - A: ")
        x = input("Enter a word: ")
        syn = wordnet.synsets(x)
        
        # Definition of the word
        if user_input.lower() == 'm':
            print(f'Definition: { syn[0].definition()}\n') 
        else:
            pass
        
        # Synonyms for the word
        if user_input.lower() == 's':
            synonyms = []
            for syn in wordnet.synsets(x):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name()) 
        
            # Deleting repeated synonyms           
            syn2 = []
            for j in synonyms:
                if j not in syn2:
                    syn2.append(j)
                else:
                    pass
            print(f"Synonyms: {syn2}\n") 
        
        else:
            pass
        
        # Antonyms for the word
        if user_input.lower() == 'a':
            antonyms = []
            for syn in wordnet.synsets(x):
                for lemma in syn.lemmas():
                    if lemma.antonyms():
                        antonyms.append(lemma.antonyms()[0].name()) 
            
            # Deleting repeated antonyms    
            ant2 = []
            for k in antonyms:
                if k not in ant2:
                    ant2.append(k)
                else:
                    pass
            print(f"Antonyms: {ant2}\n") 
        else:
            pass
    


    else:
        happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
        
        args = TTSettings(num_beams=5, min_length=1)
        x = input("Enter any sentence: ")
        
         
        result = happy_tt.generate_text("grammar: " + x, args)
        
        print(result.text) 
    checker = input("Press q to quit, anything else to continue: ")
    if checker.lower() == 'q':
            break
        
