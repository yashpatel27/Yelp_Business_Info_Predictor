import nltk
from nltk.util import ngrams
#import re
from nltk.tokenize import sent_tokenize
#from nltk import load
#from operator import itemgetter

def processReservations(sentence,tagger,neg_tag):
    a=open('Reservations.txt','a')
    #result_no=[]
    fivegrams = ngrams(sentence,5) #compute 2-grams    
   	 #for each 2gram
    for tg in fivegrams:  
        if tg[2] in tagger:
            if tg[0] in neg_tag or tg[1] in neg_tag or tg[3] in neg_tag or tg[4] in neg_tag:
                a.write(tg[2]+' no\n')#result_no.append(tg)
                break;
            else:
                a.write(tg[2]+' yes\n')
                break;
    #return result_no

def processParking(sentence,tagger,neg_tag):
    a=open('Parking.txt','a')
    #result_no=[]
    fivegrams = ngrams(sentence,5) #compute 2-grams    
   	 #for each 2gram
    for tg in fivegrams:  
        if tg[2] in tagger:
            if tg[0] in neg_tag or tg[1] in neg_tag or tg[3] in neg_tag or tg[4] in neg_tag:
                a.write(tg[2]+' no\n')#result_no.append(tg)
                break;
            else:
                a.write(tg[2]+' yes\n')
                break;
    #return result_no

def processDelivery(sentence,tagger,neg_tag):
    a=open('Delivery.txt','a')
    #result_no=[]
    fivegrams = ngrams(sentence,5) #compute 2-grams    
   	 #for each 2gram
    for tg in fivegrams:  
        if tg[2] in tagger:
            if tg[0] in neg_tag or tg[1] in neg_tag or tg[3] in neg_tag or tg[4] in neg_tag:
                a.write(tg[2]+' no\n')#result_no.append(tg)
                break;
            else:
                a.write(tg[2]+' yes\n')
                break;

def processAlcohol(sentence,tagger,neg_tag):
    a=open('Alcohol.txt','a')
    #result_no=[]
    fivegrams = ngrams(sentence,5) #compute 2-grams    
   	 #for each 2gram
    for tg in fivegrams:  
        if tg[2] in tagger:
            if tg[0] in neg_tag or tg[1] in neg_tag or tg[3] in neg_tag or tg[4] in neg_tag:
                a.write(tg[2]+' no\n')#result_no.append(tg)
                break;
            else:
                a.write(tg[2]+' yes\n')
                break;

def counter(path,word1,word2,word3):
    freq={} # new dictionary. Maps each word to each frequency 
	
    #initialize the frequency of the two words to zero.
    freq[word1]=0
    freq[word2]=0

    my_file=open(path) # open a connection to the file 
    my_file.seek(0) #ensure you're at the start of the file..
    first_char = my_file.read(1) #get the first character
    if not first_char:
        final.write(word3+' no' + '\n')
    else:
        my_file.seek(0) #first character wasn't empty, return to start of file.
        #use file now    
        for line in my_file: # read the file line by line 
            # lower() converts all the letters in the string to lower-case
            # strip() removes blank space from the start and end of the string
            # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D] 
            
            words=line.lower().strip().split(' ')
           
            # use for to go over all the words in the list 
            for word in words: # for each word in the line
                if word==word1: 
                    freq[word1]=freq[word1]+1 # if the word is word1, then increase the count of word1 by 
                elif word==word2: 
                    freq[word2]=freq[word2]+1 # if the word is word2, then increase the count of word2 by 1
        
        if freq[word1] > freq[word2]:
            final.write(word3+' yes' + '\n')
        else:
            final.write(word3+' no' + '\n')
    my_file.close() #close the connection to the text file 

    #return freq[word1],freq[word2]

def run(fpath):
    x=open('Reservations.txt','w')
    y=open('Delivery.txt','w')
    z=open('Parking.txt','w')
    w=open('Alcohol.txt','w')

    #posLex=loadLexicon('positive-words.txt')
    #negLex=loadLexicon('negative-words.txt')
    biz_res={'reservations'}#,'delivery','alcohol','parking'}
    biz_del={'delivery'}
    biz_par={'parking'}    
    biz_alc={'wine','beer','cocktail'}    
    neg_words={'no','not','never','none','nor','neither','don''t'}
    #make a new tagger
    #_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    #tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()
    #split sentences
    sentences=sent_tokenize(text)
    #print ('NUMBER OF SENTENCES: ',len(sentences))

    #final_result=[]

    # for each sentence
    for sentence in sentences:

        #sentence=re.sub('[^a-zA-Z\d]','',sentence)#replace chars that are not letters or numbers with a spac
        #sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

        #tokenize the sentence
        terms = nltk.word_tokenize(sentence.lower())   

        #POStags=['NN'] # POS tags of interest 		
        #POSterms=getPOSterms(terms,POStags,tagger)
        #nouns=POSterms['NN']
        #adjectives=POSterms['JJ']
        #adverbs=POSterms['RB']
        #final_result+=
        processReservations(terms,biz_res,neg_words)
        processDelivery(terms,biz_del,neg_words)
        processParking(terms,biz_par,neg_words)        
        processAlcohol(terms,biz_alc,neg_words)
        #get the results for this sentence 
        #adjAfterAdv+=getAdvAdjTwograms(terms, adjectives, adverbs)
        
    #print(final_result)
    counter('Reservations.txt','yes','no','reservations')
    counter('Delivery.txt','yes','no','delivery')
    counter('Parking.txt','yes','no','parking')
    counter('Alcohol.txt','yes','no','alcohol')
    x.truncate(0)
    y.truncate(0)
    z.truncate(0)
    w.truncate(0)
    x.close()
    y.close()
    z.close()
    w.close()

if __name__=='__main__':
    final=open('final-biz.txt','w')
    #Reading the file from which the restaurants names are taken to search in Yelp and Scrape the reviews
    path=r'links.txt'    
    
    fin=open(path)

    for line in fin:                                        #For each name of restaurant in the List
        words = line.lower().strip()    
        print (words)
        if "-san-franc" in words:       
            start = words.index( "/biz/" ) + len( "/biz/" )
            end = words.index( "-san-franc", start )
        elif "-brisbane" in words:
                start = words.index( "/biz/" ) + len( "/biz/" )
                end = words.index( "-brisbane", start )
        else:
            if "-alameda" in words:
                start = words.index( "/biz/" ) + len( "/biz/" )
                end = words.index( "-alameda", start )
    
        names = str(words[start:end])
        names = names.replace('-',' ')
        #f=open('Yelp\San_Fransisco\American\Reviews''\\'+names+'.txt','w')      #New file Created by Restaurant name to store the reviews
        #f=open('Yelp_reviews_new''\\'+names+'.txt','w')      #New file Created by Restaurant name to store the reviews

        final.write(names + '\n')
        final.write('---------------' + '\n')	
        
        run(names+'.txt')
        final.write('\n')
    final.close()














