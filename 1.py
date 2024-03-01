total = int(input())

silver = 96
gold = silver/16

silver_price = 48
silver_total = silver*silver_price
gold_price = (total-silver_total)/gold
print(round(gold_price))
