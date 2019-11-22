# -*- coding: utf-8 -*-
import re

str="please sit spot.sit spot,sit.spot here now here."
def sprinklecommas(str,precedes=[],follows=[]):
    sentences=re.split(r"\.",str)
    if len(sentences)<1:
        return
    for sentence in sentences:
        if "," in sentence:
            phrases=re.split(r"\,",sentence)
            for i in range(len(phrases)):
                phrase=phrases[i]
                if i<range(len(phrases)-1):
                    words=re.split(r"\s" ,phrase)
                    if not any(words[-1]==p for p in follows):
                        follows.append(words[-1])
                if i>0:
                    precedingwith=re.split("\s",phrase) 
                    if precedingwith[0]!=None and not any(precedingwith[0]==p for p in precedes):
                        precedes.append(precedingwith[0])
    print precedingwith
    print follows




sprinklecommas(str)

