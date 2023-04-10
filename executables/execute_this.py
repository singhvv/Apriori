import apriori


algo = input("Enter the algorithm:\napriori\nidea1\n\n")
dataset = input("\nEnter the dataset size:\n1000\n10000\n50000\n100000\n")
min_sup = input("\nEnter the minimum support as a decimal (eg. 0.01 = 1%)\n\n")
dbase = "abc"
if(dataset == "1000"):
    dbase = "D1K.txt"
    print("You have selected ", dbase, "\n")
elif(dataset == "10000"):
    dbase = "D10K.txt"
    print(dbase)
elif(dataset == "50000"):
    dbase = "D50K.txt"
    print("You have selected ", dbase, "\n")
elif(dataset == "100000"):
    dbase = "D100K.txt"
    print("You have selected ", dbase, "\n")


if(algo == "apriori"):
    print(dbase)
    print(min_sup,"\n", algo)
    apriori.main(dbase, float(min_sup))
elif(algo == "idea1"):
    i1 = "apriori_fn=apriori_idea1"
    apriori.idea1_main(dbase, float(min_sup), i1)