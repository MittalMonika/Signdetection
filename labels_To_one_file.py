import os

# Base directory where 'test', 'train', 'valid' folders are located/Users/ramankhurana/Downloads/sign\ labels.v5i.yolov8 
import os
from collections import defaultdict

base_directory = '/Users/ramankhurana/Downloads/signlabels/'
subdirectories = ['test/labels', 'train/labels', 'valid/labels']
combined_content = defaultdict(list)

for subdirectory in subdirectories:
    dir_path = os.path.join(base_directory, subdirectory)
    for filename in os.listdir(dir_path):
        if filename.endswith('.txt'):
            base_name = filename.split('_')[0]  # Extract base part like 'f114a'
            file_path = os.path.join(dir_path, filename)
            with open(file_path, 'r') as file:
                combined_content[base_name].extend(file.readlines())

output_file = 'combined_labels.txt'
with open(output_file, 'w') as outfile:
    outfile.write("labels_per_document = {\n")
    for base_name, content in combined_content.items():
        formatted_content = '", "'.join([line.strip() for line in content])
        outfile.write(f"    '{base_name}': {{\n        'page_number': 1,\n        'labels': [\"{formatted_content}\"]}},\n")
    outfile.write("}\n")

