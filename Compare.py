from __future__ import print_function #Only for Python2

res_correct=0
res_wrong=0
del_correct=0
del_wrong=0
par_correct=0
par_wrong=0
alc_correct=0
alc_wrong=0
#no_links=0
accuracy=0
with open('result.txt') as f1, open('final-biz.txt') as f2, open('output-file.txt', 'w') as outfile:
    for line1, line2 in zip(f1, f2):
        if "reservations" in line1:  				
            if line1 == line2:
                res_correct=res_correct+1
            else:
                #print(line1, end='', file=outfile)
                res_wrong=res_wrong+1
        if "delivery" in line1:  				
            if line1 == line2:
                del_correct=del_correct+1
            else:
                #print(line1, end='', file=outfile)
                del_wrong=del_wrong+1
        if "parking" in line1:  				
            if line1 == line2:
                par_correct=par_correct+1
            else:
                #print(line1, end='', file=outfile)
                par_wrong=par_wrong+1
        if "alcohol" in line1:  				
            if line1 == line2:
                alc_correct=alc_correct+1
            else:
                #print(line1, end='', file=outfile)
                alc_wrong=alc_wrong+1
    #print('correct='+str(correct), end='', file=outfile) 
    #print('wrong='+str(wrong), end='', file=outfile)       
    #no_links=(correct+wrong)/4
    #print('links='+str(no_links), end='', file=outfile)       
    #correct=no_links-wrong
    #print('correct='+str(correct), end='', file=outfile) 
    accuracy=(res_correct/(res_correct+res_wrong))*100
    #print('accuracy='+str(accuracy), end='', file=outfile) 
    print('For Reservations\n', end='', file=outfile)
    print('----------------\n', end='', file=outfile)
    print('correct predicted values='+str(res_correct)+'\n', end='', file=outfile)
    print('wrong predicted values='+str(res_wrong)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n')
#print('correct predicted values='+str(correct)+'\n')
#print('wrong predicted values='+str(wrong)+'\n')
    accuracy=(del_correct/(del_correct+del_wrong))*100
    #print('accuracy='+str(accuracy), end='', file=outfile) 
    print('For Delivery\n', end='', file=outfile)
    print('----------------\n', end='', file=outfile)
    print('correct predicted values='+str(del_correct)+'\n', end='', file=outfile)
    print('wrong predicted values='+str(del_wrong)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n')
#print('correct predicted values='+str(correct)+'\n')
#print('wrong predicted values='+str(wrong)+'\n')
    accuracy=(par_correct/(par_correct+par_wrong))*100
    #print('accuracy='+str(accuracy), end='', file=outfile) 
    print('For Parking\n', end='', file=outfile)
    print('----------------\n', end='', file=outfile)
    print('correct predicted values='+str(par_correct)+'\n', end='', file=outfile)
    print('wrong predicted values='+str(par_wrong)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n')
#print('correct predicted values='+str(correct)+'\n')
#print('wrong predicted values='+str(wrong)+'\n')
    accuracy=(alc_correct/(alc_correct+alc_wrong))*100
    #print('accuracy='+str(accuracy), end='', file=outfile) 
    print('For Alcohol\n', end='', file=outfile)
    print('----------------\n', end='', file=outfile)
    print('correct predicted values='+str(alc_correct)+'\n', end='', file=outfile)
    print('wrong predicted values='+str(alc_wrong)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n', end='', file=outfile)
    print('Accuracy percentage='+str(accuracy)+'\n')
#print('correct predicted values='+str(correct)+'\n')
#print('wrong predicted values='+str(wrong)+'\n')

    
    
    
    