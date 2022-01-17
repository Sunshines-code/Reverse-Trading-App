import pickle

# option = int(input("Option: "))
f = open('../resources/stock.dict', 'rb+')        
d = pickle.load(f)
print(d)