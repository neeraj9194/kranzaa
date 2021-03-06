from django.shortcuts import render
from .models import Review
from datetime import date
# Create your views here.

#from django.shortcuts import render_to_response
import random
import datetime
import time


import nltk
from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

def cal_pos_neg(text):
    #EXAMPLE_TEXT = "well hello this is worst baddest  bad comment"
    EXAMPLE_TEXT = text
    token_word=word_tokenize(EXAMPLE_TEXT)

    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in token_word if not w in stop_words]


    tagged = nltk.pos_tag(filtered_sentence)
    synsets = []
    lemmatizer = WordNetLemmatizer()
    pos_sum=0
    neg_sum=0
    for token in tagged:
        wn_tag = penn_to_wn(token[1])
        if not wn_tag:
            continue
        lemma = lemmatizer.lemmatize(token[0], pos=wn_tag)
        if wn.synsets(lemma, pos=wn_tag):
            current_token=list(swn.senti_synsets(lemma, pos=wn_tag))[0]
            pos_sum+=current_token.pos_score()
            neg_sum+=current_token.neg_score()
            synsets.append(current_token)
            #print(current_token.obj_score())
    length_list=len(synsets)
    if length_list == 0:
        pos_avg=0
        neg_avg=0
    else:
        pos_avg=pos_sum/length_list
        neg_avg=neg_sum/length_list
    #for token in synsets:
     #   print(token)
    #print(pos_avg)
    #print(neg_avg)
    return [pos_avg,neg_avg]

def review(store,comment,ratings):
    if ratings >= 5:
        polarity=1
    else:
        polarity=-1
    pos_neg=cal_pos_neg(comment)
    obj, created=Review.objects.get_or_create(store=store,created__date=date.today(),defaults={'pos_score': 0,'neg_score':0,'polarity':0,'no_of_comments':0})
    pos=float(obj.pos_score)
    neg=float(obj.neg_score)
    pol=float(obj.polarity)
    #obj.pos_score = pos+pos_neg[0]
    #obj.neg_score = neg+pos_neg[1]
    obj.polarity =  pol+polarity
    comment_no=int(obj.no_of_comments)+1
    obj.no_of_comments = comment_no
    obj.pos_score = (pos+pos_neg[0])/comment_no
    obj.neg_score = (neg+pos_neg[1])/comment_no
    obj.save()
    return [pos_neg[0],pos_neg[1],polarity]




def linechart(request,slug,month=date.today().month):
    if request.user.is_superuser:
        """
        lineChart page
        """
        q=Review.objects.filter(store__storeslug=slug,created__month='5')
        value=[0]*31
        print(value)
        for i in range(1,31):
            value[i]=[i,0]
            #print(value)
        for senti in q:
            score=float(senti.pos_score-senti.neg_score+senti.polarity)
            day=senti.created.day
            value[day]=[day,score]
            print(value)
            value[0]=[0,0]
        for i in range(1,31):
            value[i][1]+=value[i-1][1]
                    
        return render(request,'senticomment/linechart.html', {'value':value})
    else:
        return render(request,'senticomment/not-auth.html')
