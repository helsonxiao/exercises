#! python3
# coding:utf-8
import pickle
my_list = ['Fred', 73, 'Hello there', 81.9876e-13]
pickle_file = open('learn_pickle.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file= open('learn_pickle.pkl', 'rb')
content = pickle.load(pickle_file)
print(content)
pickle_file.close()