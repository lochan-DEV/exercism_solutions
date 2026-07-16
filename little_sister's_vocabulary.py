"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    worded="un"+word
    return worded
    
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    groups = [prefix]
    for word in vocab_words[1:]:
        groups.append(prefix + word)
    return " :: ".join(groups)

def remove_suffix_ness(word):
    worded=word.removesuffix("ness")
    if worded[-1]=="i":
        return worded[:-1] + "y"
    else:
        return worded
        
        
   


def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index]
    stripped = word.strip(".")
    return stripped + "en"