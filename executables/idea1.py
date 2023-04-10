from collections import defaultdict
from itertools import combinations
import apriori

# Define the Apriori algorithm function
def apriori_idea1(db, min_support):
    # Step 1: Find frequent 1-itemsets
    item_counts = defaultdict(int)
    for transaction in db:
        for item in transaction:
            item_counts[item] += 1
    num_transactions = len(db)
    freq_k_itemsets_all = {frozenset([item]): count / num_transactions for item, count in item_counts.items()}
    freq_k_itemsets = {frozenset([item]): count / num_transactions for item, count in item_counts.items() if count / num_transactions >= min_support}
    db_all_freq1 = []  # db with all transactions with freq itemset
    for transaction in db:
        satisfy_supp = False
        for it in transaction:
            if freq_k_itemsets_all[frozenset({it})] >= min_support:
                satisfy_supp = True
        if satisfy_supp:
            db_all_freq1.append(transaction)
            
    
    ########
    print(len(db), len(db_all_freq1))
    item_counts = defaultdict(int)
    for transaction in db_all_freq1:
        for item in transaction:
            item_counts[item] += 1
    num_transactions = len(db_all_freq1)
    freq_k_itemsets = {frozenset([item]): count / num_transactions for item, count in item_counts.items() if count / num_transactions >= min_support}
    ########

    frequent_itemsets = freq_k_itemsets
    # Step 2: Generate k-itemsets and find frequent ones until no more frequent itemsets are found
    k = 1
    while len(freq_k_itemsets) > 0:
        k += 1

        # Generate candidate k-itemsets from frequent (k-1)-itemsets
        candidate_itemsets = set([itemset1.union(itemset2) for itemset1 in frequent_itemsets for itemset2 in frequent_itemsets if len(itemset1.union(itemset2)) == k])
        # Count the support of each candidate itemset
        item_counts = defaultdict(int)
        for transaction in db_all_freq1:
            for candidate_itemset in candidate_itemsets:
                if candidate_itemset.issubset(transaction):
                    item_counts[candidate_itemset] += 1
        # Find frequent k-itemsets
        freq_k_itemsets = {itemset: count / num_transactions for itemset, count in item_counts.items() if count / num_transactions >= min_support}
        frequent_itemsets.update(freq_k_itemsets)

    return frequent_itemsets, k
