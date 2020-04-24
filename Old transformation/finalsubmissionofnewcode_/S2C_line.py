import spacy
import sys
import nltk
import regex as re

def get_it_all_spacy(sen):
#     print(sen)
    doc = nlp(sen)
    count=0
    cclst = list()
    sublst = list()
    verblst = list()
    subjlst = list()
    objlst = list()
    for token in doc:
        count+=1
        if "CC" in token.pos_ or " for " == " "+str(token)+" " or " so " == " "+str(token)+" ":
            cclst.append([count,str(token)])
    if len(cclst)==0:
        cclst.append([count,"CCab"])
    count = 0
    for token in doc:
        count+=1
        if "VERB" in token.pos_ or "AUX" in token.pos_:
            verblst.append([count,str(token)])
    if len(verblst)==0:
        verblst.append([count,"VBab"])
    count = 0
    for token in doc:
        count+=1
        if "NOUN" in token.pos_ or "PRON" in token.pos_ or "PROPN" in token.pos_:
            sublst.append([count,str(token)])
    if len(sublst)==0:
        sublst.append([count,"SBab"])
#     print("Subject = ",sublst)
#     print("Verb = ",verblst)
    k=0
    r=0
    i=0;
    flag = 0
    ccoccur = cclst[i][0]
    verboccur = verblst[k][0]   
    try:
        while verboccur< sublst[r][0]:
            k+=1
            verboccur = verblst[k][0]
    except:
        k-=1
        verboccur = verblst[k][0]
    try:    
        flag = 0
        while (1):
            j = sublst[r]
#             print("Accessing , ",j[1],verblst[k][1])
            ccoccur = cclst[i][0]
            verboccur = verblst[k][0]
            if j[0]<=verboccur:
                subjlst.append([j[0],j[1]])
            if j[0]>verboccur:
                objlst.append([j[0],j[1]])
            r+=1
            try:
                j = sublst[r]
            except:
                j = sublst[r-1]
            if j[0]>=verboccur:
                try:
                    while(j[0]>verboccur):
                        k+=1
                        verboccur = verblst[k][0]
                except:
                    k-=1
                    verboccur = verblst[k][0]
#                 print(k,verblst[k])
            if(flag==1):
                try:
                    objlst.append([sublst[r][0],sublst[r][1]])
                except:
#                     print("no last object")
                    pass
#                 print("broke")
                break;

            if(sublst[r][0]>=ccoccur):
                try:
                    i+=1    
                    ccoccur = cclst[i][0]
                except:
                    i-=1
                    flag = 1;
#             print(ccoccur)

    except:
#         print(sys.exc_info()[0])
        pass
#     print(subjlst,objlst)
#     print(verblst)
#     print(cclst)
    return (subjlst,objlst,verblst,cclst)
    #Data preparation completed
                        
# Rule 1 segregation
# Breaking conjunction
def rule_1(sen):
    subjlst,objlst,verblst,cclst = get_it_all_spacy(sen)
    doc = nlp(sen)
#     print(subjlst,objlst,verblst,cclst)
    broke = list()
    i =0
    j=0
    count = len(cclst)
    if cclst[0][1] == "CCab" :
        print("Already Simple --- ",sen)
        exit()
    else:
        try:
            cap = cclst[i][1]
            while (1):
#                 print(str(doc[j]))
                # print(cap)
                cap = cclst[i][1]
                if str(cap).strip()==str(doc[j]):
    #                 print(str(doc[j]))
                    broke.append(j)
                    count-=1
                    if count!=1:
                        i+=1
                    else:
                        break
                j+=1
        except:
#             print(sys.exc_info()[0])
            pass
        broke.append(len(str(doc)))
#         print(broke)
        fin = list()
        fin.append(str(doc[0:broke[0]]))
        try:
            for i in range(len(broke)):
                fin.append(str(doc[broke[i]+1:broke[i+1]]))
        except:
#             print(sys.exec_info()[0])
            pass
    final= list()
    for i in fin:
    #     print(i)
        stri = str()    
        for j in i:
            stri+= j
        final.append(stri)
    broke = final
#     print(broke)
    return (subjlst,objlst,broke)

def rule_2_3(empsubjlst,allavail,onlyobjlst,onlysubjlst):
    count = 0
    try:
        while len(empsubjlst)!=0:
            extract = len(allavail)-1
            subj3lst,obj3lst,verb3lst,cc3lst = get_it_all_spacy(allavail[extract][1])
            for i in empsubjlst:
                finstr= subj3lst[0][1]+" "+i[1]
                count=subj3lst[0][0]+1
                allavail.append([count,finstr])
#                 print(finstr)
                empsubjlst.remove(i)
        while len(onlyobjlst)!=0:
            extract = len(allavail)-1
#             print(extract,len(allavail))
            subj3lst,obj3lst,verb3lst,cc3lst = get_it_all_spacy(allavail[extract][1])
            objlen=len(obj3lst)-1
            prestr = allavail[extract][1].replace(obj3lst[objlen][1],"")
        #     print(prestr)
            for i in onlyobjlst:
                finstr = prestr+" "+i[1]
                count=allavail[extract][0]+1
                allavail.append([count,finstr])
#                 print(finstr)
                onlyobjlst.remove(i)
        while len(onlysubjlst)!=0:
            for i in onlysubjlst:
                extract = i[0]+1
                for j in range(len(allavail)):
                    if allavail[j][0] == extract:
                        extract = j
                        break
#                 print(extract)
                subj3lst,obj3lst,verb3lst,cc3lst = get_it_all_spacy(allavail[extract][1])
                subjlen = len(subj3lst)-1
                prestr = allavail[extract][1].replace(subj3lst[subjlen][1],"")
                finstr = i[1]+" "+prestr
                count=allavail[extract][0]+1
                allavail.append([count,finstr])
#                 print(finstr)
                onlysubjlst.remove(i)
        return (allavail)
    except:
#         print(sys.exc_info())
        pass

def main(sen):
	# Rule 1 check
	nlp = spacy.load("en_core_web_sm")
	subjlst,objlst,broke = rule_1(sen)
	allavail = list()
	empsubjlst = list()
	empobjlst = list()
	empverblst = list()
	onlyobjlst = list()
	onlysubjlst = list()
	count=0;
	total = len(broke)
	for i in broke:
	    subj=1;
	    verb=1;
	    obj=1;
	    count+=1
	    subj2lst,obj2lst,verb2lst,cc2lst = get_it_all_spacy(i.strip())
	#     print(verb2lst)
	    if len(subj2lst)==0:
	        subj=0
	        if len(obj2lst)!=0:
	            if any(obj2lst[0][1] in ls for ls in subjlst):
	                subj=1
	                obj=0
	    if len(obj2lst)==0:
	        obj=0;
	        if len(subj2lst)!=0:
	            if any(subj2lst[0][1] in ls for ls in objlst):
	#                 print("\nhere")
	                subj=0
	                obj=1
	    if verb2lst[0][1]=="VBab":
	        verb=0;
	    if subj==0 and verb!=0 and obj!=0:
	        empsubjlst.append([count,i])
	    if subj==0 and verb==0 and obj!=0:
	        onlyobjlst.append([count,i])
	    if subj!=0 and verb!=0:
	        allavail.append([count,i])
	    if subj!=0 and verb==0 and obj==0:
	        onlysubjlst.append([count,i])
	# print(empsubjlst,onlysubjlst,onlyobjlst,allavail)

	# Check for case in Rule2 or Rule3:
	if len(broke)==len(allavail):
	    for i in allavail:
	        print(re.sub(' +', ' ',i[1]).strip())
	else:
	    try:
	        allavail = rule_2_3(empsubjlst,allavail,onlyobjlst,onlysubjlst)
	        for i in allavail:
	            print(re.sub(r'\b(.+)\s+\1\b', r'\1', re.sub(' +', ' ',i[1]).strip()))
	    except:
	        print("Not possible to convert to simple, make sure you entered a COMPOUND sentence")

def sep_semi(inpt):
    fw = open("tempoutput.txt","w")
    line = re.sub("[^\P{P}\.;]|","",str(nlp(inpt)))
    fw.write(line+"\n")
#         r = line.split(". ")
#         for i in r:
#             if i==" ":
#                 r.remove(i)
# #         fw.write(line+"\n")
#         if(len(r)!=0):
#             for i in r:
#                 fw.write(i+"\n")
    fw.close()
    rw = open("tempoutput.txt")
    lst = list()
    for line in rw:
        lst.append(line.split(";"))
    rw.close()
    rw = open("tempoutput.txt","w")
    for i in lst:
        if(len(i)>1):
            for sep in i:
                rw.write(sep.strip())
                rw.write("\n")
        else:
            rw.write(i[0])
#                 print(sep.strip())
    rw.close()

if __name__ == '__main__':
	nlp = spacy.load("en_core_web_sm")
	sep_semi(input("Enter Input"))
	rw = open("tempoutput.txt")
	for i in rw:
		main(i)
	rw.close()
	# main(sen,ophandle)