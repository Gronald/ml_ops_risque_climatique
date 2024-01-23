import os
import json
json_file_path = "results_query.json"
from joblib import load 

clf = load('./models/model.joblib')


if not os.path.exists(os.path.join("data","logs",json_file_path)):
    with open(os.path.join("data","logs",json_file_path),"w") as json_file:
        json.dump([],json_file)