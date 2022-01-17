import pickle


stocks = {'APPL':'APPL'}



pickle_out = open("resources/stock.dict","wb")
pickle.dump(stocks, pickle_out)
pickle_out.close()