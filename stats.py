def count_words (text):
    word_list = text.split(None)
    word_count = len(word_list)
    return word_count

def histo (text) :

    lc_text = text.lower()
    # convert the text string into a list of characters
    allchars = list(lc_text)
    histo_dict = {}
    for mychar in allchars:
        
        if mychar in histo_dict:
            histo_dict[mychar] += 1
        else:
             histo_dict[mychar]= 1
    # we return a dictionary of String -> Integer (e.g. {'a':1234, 'b':3345})
    return histo_dict

def sort_on(dict):
    return dict["num"]

def sort_histo(dict):
    # we're getting a dict of key value pairs, but we want to return a list of dicts, sorted by the counts.
    dict_list = []
    allkeys = dict.keys()
    for key in allkeys:
        new_dict = {}
        char = key
        new_dict["char"] = char
        new_dict["num"] = dict[key]
        #print (new_dict)
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list