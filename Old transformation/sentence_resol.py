import stanfordnlp
import sys
import pandas as pd
import os
#----------#
def depend_resolve(doc):
	print(*[f"{word.dependency_relation}({word.text} - {word.index} , {(doc.sentences[0].words[word.governor-1].text if word.governor > 0 else 'root')} - {word.governor})" for word in doc.sentences[0].words], sep='\n')
	lst = list()
	for word in doc.sentences[0].words:
	    print(word)
	    if(word.governor>1):
	        lst.append((word.dependency_relation, word.text,word.index,doc.sentences[0].words[word.governor-1].text,word.governor))
	    else:
	        lst.append((word.dependency_relation, word.text,word.index,doc.sentences[0].words[word.governor-1].text,"root"))
	return lst;
#----------#
def sent_resolve(lst):
	res = list();
	fin = list();
	k =0;
	flag=0
	for i in lst:
	    # print(i[0])
	    if("subj" in i[0]):
	        # print("true")
	        str1 = i[1]
	        str2 = i[3]
	        res.clear()
	        res.append(i)
	        res.append((":"))
	        # print(res)
	        for j in lst:
	            if("subj" not in j[0] and (str1 in j[1] or str1 in j[3] or str2 in j[1] or str2 in j[3]) ):
	                flag = 1
	                res = res[:] + [j]
	        if(flag==1):
	            fin = fin[:] + res
	            fin.append("\n")
	            # print(fin)
	            flag = 0
	return fin
def df_tocsv(df,fin,l):
	res = list()
	k = 0
	for i in fin:
	    if "\n" in i :
	        k = k+1
	    if ":" not in i:
	        lst = list(i)
	        lst.insert(0,k)
	        lst.insert(0,l)
	        a = tuple(lst)
	        res.append(a)
	print(res)
	df = df.append(res)
	print(df)
	return df	
def main():
	pip = stanfordnlp.Pipeline()
	nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos,lemma,depparse', lang='en')
	print("Enter sentence")
	str = sys.stdin.readlines()
	print(str)
	l = 0
	df = pd.DataFrame()
	for i in str:
		if i == None:
			continue
		try:
			doc = nlp(i)
			res = depend_resolve(doc)
			# print(res)
			final = sent_resolve(res)
			print(final)
			if(len(final) == 0):
				print("LENGTH _____)))")
				res = [l]	
				print(res)
				df = df.append(res)
				l=l+1
				continue
			df = df_tocsv(df,final,l)
			print(df.head())
		except:
			print(i)
	cwd = os.getcwd()
	df.to_csv(cwd + 'depen_list')

		

if __name__ == '__main__':
	main()