from django.shortcuts import render
from PyDictionary import PyDictionary
from .decorators import synonyms, antonyms
# Create your views here.

def home(request):
    return render(request, 'Dictionary/home.html', {})


def word(request):
    
    try:
        search = request.GET.get('search')        
        dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        # try:
        #     noun= meaning['Noun'][0]
        # except:
        #      noun= None
        # This is the simplest code for the above
        noun = meaning.get('Noun', [None])[0:2]#This returns None if key not present
        verb = meaning.get('Verb', [None])[0:2]
        
        if(len(meaning)== 0 or meaning== None):
                return render(request, 'Dictionary/home.html', {})
        # The antonyms and synonyms of pydictionary are not working
        # antonyms = dictionary.antonym(search)
        # synonyms = dictionary.synonym(search)
        synonym= synonyms(search)
        antonym = antonyms(search)    
        
        context = {
            'meaning_noun': noun,
            'meaning_verb': verb,
            'antonym': antonym,
            'synonym': synonym,
        }
    except:
        # return render(request, 'Dictionary/home.html', {})
        context={}
    return render(request, 'Dictionary/word.html', context)

