import os
import json

def clear_test_data():
    test_data_dir = "./ReferenceCode/test_data"
    for filename in os.listdir(test_data_dir):
        filepath = os.path.join(test_data_dir, filename)
        with open(filepath, 'w') as f:
            json.dump([], f)
