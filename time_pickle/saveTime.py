import datetime, pickle, os

first_time = True
if os.path.isfile("last_run.pkl"):
    pickle_file = open("last_run.pkl", "rb")
    last_time = pickle.load(pickle_file)
    pickle_file.close()
    print("The last time this program was run was ", last_time)
    first_time = False

pickle_file = open("last_run.pkl", 'wb')
pickle.dump(datetime.datetime.now(), pickle_file)
pickle_file.close()
if first_time:
    print("Created new pickle file.")