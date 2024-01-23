import os
import json
json_file_path = "results_query.json"


if not os.path.exists(os.path.join("data","logs",json_file_path)):
    with open(os.path.join("data","logs",json_file_path),"w") as json_file:
        json.dump([],json_file)