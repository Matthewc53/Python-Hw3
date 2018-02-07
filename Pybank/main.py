import os
import csv

csv1 = os.path.join("csv1.csv")
total_months = int(0)
total_revenue = float(0)
avg_changeinrev = float(0)
high = float(0)
low = float(0)
highdate = ""
lowdate = ""
revchange = float(0)
prevrevenue = float(0)


with open(csv1,newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next (csvreader,None)
    for row in csvreader:
        value = float(row[1])
        total_months = total_months+1
        total_revenue = total_revenue + value
        revchange = value - prevrevenue
        avg_changeinrev = revchange/total_months
        prevrevenue = value
        if (high < revchange):
            high = revchange
            highdate = row[0]
        if (low > revchange):
            low = revchange
            lowdate = row[0]

print ("total months " + str(total_months))
print ("total revenue $" + str(total_revenue))
print ("avg changeinrev " +str(avg_changeinrev))
print ("highest revenue change " + str(high))
print ("highest revenue date " +str(highdate))
print ("lowest revenue date " +str(lowdate))
print ("lowest rev change" + str(low))


file = open("revenuechngs.txt","w")
file.write("total months " + str(total_months)+"\n")
file.write("total revenue $" + str(total_revenue)+"\n")
file.write("avg changeinrev " +str(avg_changeinrev)+"\n")
file.write("highest revenue change " + str(high)+"\n")
file.write("highest revenue date " +str(highdate)+"\n")
file.write("lowest revenue date " +str(lowdate)+"\n")
file.write("lowest rev change" + str(low)+"\n")
