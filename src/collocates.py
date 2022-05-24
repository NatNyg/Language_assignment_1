"""
Starting out by importing the necessary libraries that I'll be using for the script and creating a nlp pipeline using the small english model 
"""
import argparse
import os 

import spacy

import math

#creating a nlp pipeline 
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 1154507

import pandas as pd


def load_file(text_file):
    """
This function loads, cleans and uses the nlp pipeline on a user-defined textfile from the 100 English Novels corpus folder 
    """
    with open(f"in/{text_file}") as text:
        clean_text = text.read()
        
    clean_text.lower()

    total_words = clean_text.split()

    corpus_size = len(total_words)
    
    doc = nlp(clean_text)
    return doc, corpus_size



def word_list(doc):
    """
This function creates a wordlist from the nlp doc just created
    """
    
    word_list = []

    for token in doc:
        if not token.is_punct and not token.is_space:
            word_list.append(token)
    str_tokens = ' '.join(str(e) for e in word_list)
    word_list_nlp = nlp(str_tokens)
    return word_list_nlp


def find_collocates(word_list_nlp, target_term):
    """
This function creates a list of the collocates of the userdefined targetterm (the window / span in this example is defined as 10 words - 5 before and 5 after the targetword - note that if the span is changed, the "before" and "after" should also be changed )
    """
    collocates = []
    for token in word_list_nlp:
        if token.text == target_term:
            before = token.i -5
            after = token.i +6
            span = word_list_nlp[before:after]
            span_before = word_list_nlp[before:token.i]
            span_after = word_list_nlp[token.i+1:after]
            for word in span_before:
                collocates.append(word)
            for word in span_after:
                collocates.append(word)
    return collocates            
    

                
def calc_MI(collocates, target_term, span, word_list_nlp, doc, corpus_size):
    """
This function calculates the MI-score for each of the collocates. To calculate the MI-score we first define the following parameters:
A = number of times the targetword appears in the text 
B = number of times each collocate appears in the text, and
AB = number of times each word inside the window accours with the target word
The MI is then calculated using the math library (I include a zero division error message, as this occored for some of the calculations. 

    """
    A = 0 

    for token in word_list_nlp:
        if token.text == target_term:
            A+=1
        else:
            pass

    B = []
    for i in range(0, len(collocates)-1):
        B_word=str(collocates[i])
        countB=0
        for token in doc:
            if token.text == B_word:
                countB+=1
        B.append(countB)
        
    AB = []

    for i in range(0, len(collocates)-1):
        B_word=str(collocates[i])
        countAB=0
        for token in collocates:
            if token.text == B_word:
                countAB+=1
        AB.append(countAB)
        
    MI = []
    for i in range(0,len(collocates)-1):
        try:
            MI_calc = math.log((AB[i]*corpus_size)/(A*B[i]*span))/math.log(2)
            MI.append(MI_calc)
        except ZeroDivisionError:
            print ("Zero Division Error occurred")
        
    return B, AB, MI
    
def save_results(collocates, B, AB, MI, text_file, target_term):
    """
This function saves the results of the collocates, B, AB and the MI-score in dataframe with the appropriate names for the columns, and then saves the dataframe to a csv to the outfolder. 
    """
    list_context = list(zip(collocates, B, AB, MI))

    df = pd.DataFrame(list_context,columns=[f'Collocates for term: "{target_term}"','B','AB','MI'])
    df = df.round(decimals =2)
    path = "out"
    collocate_file = f"Collocates {text_file}.csv"
    df.to_csv(os.path.join(path, collocate_file),index=False)
    return df
    
def parse_args():
    """
This function initialises the argument parser and defines the comand line parameters - for this script this is the name of the textfile, the target term and the span. 
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-tf","--text_file",required=False, help = "The name of the file to look for collocates in")
    ap.add_argument("-tt","--target_term",required=True, help = "The target_term to find collocates for")
    ap.add_argument("-sp","--span",required=True, help = "Desired span/window of collocates")
    args = vars(ap.parse_args())
    return args 
    
def main():
    """
This function defines which functions to run when the script is executed, and which arguments from the commandline has to be taken as parameters for the different functions. 
    """
    args = parse_args()
    doc, corpus_size = load_file(args["text_file"])
    word_list_nlp = word_list(doc)
    collocates = find_collocates(word_list_nlp, args["target_term"])
    B, AB, MI = calc_MI(collocates, args["target_term"], int(args["span"]),word_list_nlp, doc, corpus_size)
    df = save_results(collocates, B, AB, MI, args["text_file"], args["target_term"])
        
    

    
if __name__== "__main__":
    main()