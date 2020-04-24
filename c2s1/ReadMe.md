# Major Issues (Algo limitation):
I have completed the code, and I have found 2 cases where the code doesn't give the correct output. These are both the limitations of the ALGORITHM
1. The first case is where spacy doesn't give the correct Part of Speech tagging, in this case there is nothing that the code can do to resolve the issue, meaning it is its limitation.
2. The second case is where the sentences are complex compound sentences. This algorithm is specifically for the compound sentences and it performs the same well.

Other issues (Code limitation but not algo):

- Certain websites denote "For" as a conjunction while wikipedia doesn't.
This works in most cases but for certain cases such as this very sentence, for is not only a coordinating conjunction but also a 'mark' that gives meaning to the second clause.
For now, I have taken it as a coordinating conjunction, hence there would be certain sentences with for, which when broken doesn't make any sense, as those clauses become dependant from independent.

- The following few sentences were corrected but for those that couldn't be corrected, the comment shows the problem. All the other sentences from the input file gives the desired result. For the sentences with no comment, there is no error and the code works perfectly for those.
3. Should we start class now or wait for everyone to get here //Complex compound
5. Tell the truth work hard and come to dinner on time. // Complex compound
7. Any fool can criticize condemn and complain  and most fools do. // Complex compound
8. Only two things are infinite the universe and human stupidity and Im not sure about the former. // compound check
9. Go and never darken my towels again.
11. Will Mary go or will John go
13. There are no eggs in the fridge nor is there any bread in the cupboard.//check
14. but to be certain is ridiculous.
15.  For dust thou art and unto dust shalt though return // spacy error
17. Power tends to corrupt and absolute power corrupts absolutely. //Corrupts -- recognized as noun by spacy.. -- correct as tends to corrupt for proper working
18. Theres one law for the rich and another for the poor. // For according to wikipedia is not a conjunction.. and hence accordingly would change the output
20. Money is a good servant but a bad master. // Similar to peanut jelly.. not considered as a single word
21.  Talk of the Devil and he is bound to appear. //Complex compound.. "Talk of the devil" --> Dependant clause

- The final issue  are for the sentences:
1. I like peanut butter and jelly
2. Money is a good servant but a bad master

These sentences involve an adjective along with the object.
In such cases, a more sophisticated code, that includes the adjective and object noun as single words would be required. I tried it in my code, while it works for these cases, it drastically changes the output of others, and hence I didn't include it.
The algorithm would work for it, but not the current 2 implementations
Hence this is the limitation of the CODE and not the ALGORITHM

-- Attached is a notebook file that runs on the input given by the user:
- S2C_bulk.ipynb
- It saves the output in the current folder wherever the python file is run from.
-- Attached is also the output file run on the input.txt file.
-- Attached is also a single line input S2C_line.py file.
-- Attached is also a requirements.txt file
- For this file, after you download it in a location where the python file/notebook is to be run,
- Run the command -- pip install -r requirements.txt (if using pip else if using pip3 then use pip3)
- This will install all the imports required to run the file...
