import sys
import re
import openai
import json
from time import sleep
import jsonlines

# sys.stdout = open('snli_train.txt', 'w') # Change the file name to the same as the prompt
dataFile = '/../NLI_dataset_using_LLM/data/snli/snli_1.0_train.jsonl' # coco dataset path settings


sent = []
final_sent = []

with jsonlines.open(dataFile) as f:
    for line in f:
        sent.append(line['sentence1'])
    
    for i in range(0, 550151):

        if sent[i] != sent[i+1]:
            final_sent.append(sent[i])

    # import pdb; pdb.set_trace()

with open("snli_train.json","w") as s:
    json.dump(final_sent, s)
    s.write("\n")

# sys.stdout.close()