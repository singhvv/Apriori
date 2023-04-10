 
import random

# Define the database sizes
D1K_SIZE = 1000
D10K_SIZE = 10000
D50K_SIZE = 50000
D100K_SIZE = 100000

 

# Define the database file names
D1K_FILE = "D1K.txt"
D10K_FILE = "D10K.txt"
D50K_FILE = "D50K.txt"
D100K_FILE = "D100K.txt"


 

# Define the function to generate a random transaction
def gen_transaction(num):
    transaction = []
    for i in range(num):
        # Generate a random item index between 0 and 99
        item_index = random.randint(0, 99)
        transaction.append(item_index)
    return transaction


 

# Define the function to generate a transactional database
def gen_database(file_name, db_size):
    with open(file_name, 'w') as db_file:
        for i in range(db_size):
            # Generate a random transaction size between 5 and 15
            transaction_size = random.randint(5, 15)
            # Generate a random transaction and write it to the file
            transaction = gen_transaction(transaction_size)
            db_file.write(" ".join([f"i{item}" for item in transaction]) + "\n")



# Generate the four transactional databases
gen_database(D1K_FILE, D1K_SIZE)
gen_database(D10K_FILE, D10K_SIZE)
gen_database(D50K_FILE, D50K_SIZE)
gen_database(D100K_FILE, D100K_SIZE)


from collections import defaultdict
from itertools import combinations

# Define a function to read a transactional database from a file
def read_database(file_name):
    with open(file_name, 'r') as db_file:
        transactions = [set(line.strip().split()) for line in db_file]
    return transactions

 
# Define the Apriori algorithm function
def apriori(db, min_support):
    # Step 1: Find frequent 1-itemsets
    item_counts = defaultdict(int)
    for transaction in db:
        for item in transaction:
            item_counts[item] += 1
    num_transactions = len(db)
    freq_k_itemsets = {frozenset([item]): count / num_transactions for item, count in item_counts.items() if count / num_transactions >= min_support}
    frequent_itemsets = freq_k_itemsets
    # Step 2: Generate k-itemsets and find frequent ones until no more frequent itemsets are found
    k = 1
    while len(freq_k_itemsets) > 0:
        k += 1
        # Generate candidate k-itemsets from frequent (k-1)-itemsets
        candidate_itemsets = set([itemset1.union(itemset2) for itemset1 in frequent_itemsets for itemset2 in frequent_itemsets if len(itemset1.union(itemset2)) == k])
        # Count the support of each candidate itemset
        item_counts = defaultdict(int)
        for transaction in db:
            for candidate_itemset in candidate_itemsets:
                if candidate_itemset.issubset(transaction):
                    item_counts[candidate_itemset] += 1
        # Find frequent k-itemsets
        freq_k_itemsets = {itemset: count / num_transactions for itemset, count in item_counts.items() if count / num_transactions >= min_support}
        frequent_itemsets.update(freq_k_itemsets)
    return frequent_itemsets, k
# db = read_database('D1K.txt')
# frequent_itemsets = apriori(db, 0.01)

 
# Define a function to write frequent itemsets to a file
def write_frequent_itemsets(file_name, frequent_itemsets):
    with open(file_name, 'w') as freq_file:
        for itemset, support in frequent_itemsets.items():
            freq_file.write("{" + ", ".join([f"i{item}" for item in itemset]) + "} " + f"{support:.2%}\n")


 
# Define the main function to run the Apriori algorithm on a database and save frequent itemsets to a file
def main(db_file_name, min_support, apriori_fn=apriori):
    print("1", db_file_name)
    db = read_database(db_file_name)
    frequent_itemsets, k = apriori_fn(db, min_support)
    print(f'k = {k-1}')
    freq_file_name = db_file_name.replace(".txt", f"_AprioriAlgo_{apriori_fn.__name__}_{int(min_support*10000)}.freq")
    write_frequent_itemsets(freq_file_name, frequent_itemsets)
    print(f"Number of itemsets found: {len(frequent_itemsets)}\n")