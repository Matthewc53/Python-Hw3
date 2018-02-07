import os
import csv

voterdata = os.path.join("voterdatahw.csv")
total_votes=int(0)
vestal=int(0)
candidate1 = "Vestal"
candidate_votes = []
with open(voterdata,newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next (csvreader,None)
    for row in csvreader:
        value = float(row[0])
        total_votes = total_votes+1
print ("total votes" + str(total_votes))
print("Candidates who received votes:" "Vestal,""Torres,","Seth,","Cordin,")

candidate_dict = {"Vestal","Torres","Seth","Cordin"}
with open(voterdata,newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next (csvreader,None)
    for row in csvreader:
        voter_id  =  row[0]
        county    =  row[1]
        candidate =  row[2]


    if candidate in candidate_dict:
        d = { "Vestal": 0 } +1# take current value set to current val +1
    else:
        Torres = 1# set new key in dict and set val = 1
print (vestal)
#---------------------------------------------------
# Remember how to access values

# d = { 'Vestal': 100 } # How many votes he currently has

#
#>>> print(d['Vestal'])
100
# We want a list of candidates and list of their votes

# this will look like [name1, name2, nam3, name4]
candidate_list = []

# this will look like [vote_count1, vote_count2, vote_count3, vote_count4]
vote_count_list = []

##########OUR HEADER################
#  index is 0     index is 1      index=2
# ['Voter ID',     'County',     'Candidate']
for row in csvreader:
    voter_id  =  row[0]
    county    =  row[1]
    candidate =  row[2]


    if candidate not in candidate_list:
		# add newly occuring candidate to the candidate list
		# add his first vote to votes list
    else:
        # find index location of candidate because he was added already
		# use prev. index location to find corresponding vote count in other list
		# set vote count equal to vote count +1
