from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'aboutpage.html')
    
def WordCounterInput(request):
    return render(request, 'CountWordsTextInput.html')
  
def WordCounterOutput(request):
    FullText = request.GET["FullText"]
    FullTextList = FullText.split()
    FullTextList = [word.capitalize() for word in FullTextList]
    FullTextLen = len(FullText.split())
    wordfreq = []
    FullTextListNew = []
    for w in FullTextList:
    	if w not in FullTextListNew:
    		FullTextListNew.append(w)
    		wordfreq.append(FullTextList.count(w))

    word_dict = dict(zip(FullTextListNew,wordfreq))
    sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'CountWordsTextOutput.html', {'FullText':FullText, "FullTextLen":FullTextLen, "SortedWordDict":sorted_word_dict})