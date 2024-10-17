#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # get user input
    mb = int(input("Enter data usage (Mb): "))
    
    # charge the correct rate based on the data usage
    total = 118.0
    if (mb <= 200):
        total = 20
    elif (mb > 200 and mb <= 500):
        total = mb * 0.105
    elif (mb > 500 and mb <= 1000):
        total = mb * 110

    # print final total
    print("Total charge is ${0:.2f}".format(total))
    # YOUR CODE ENDS HERE

main()