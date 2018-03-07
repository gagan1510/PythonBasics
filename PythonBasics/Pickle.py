import pickle

example_dict = {1: '6',
                2: '2',
                3: 'f'
                }

pickle_out = open("dict.pickle", "wb") # creating the pickle file to write in 'wb' stands for writing bytecode
pickle.dump(example_dict, pickle_out) # dumping the data in the pickle file
pickle_out.close()

pickle_in = open("dict.pickle", "rb") # this is opening the pickle file 'rb' stands for reading bytecode
dict2 = pickle.load(pickle_in) # decodes the data
print(dict2)
pickle_in.close()