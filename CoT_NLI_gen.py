import sys
import re
import openai
import json
from time import sleep

sys.stdout = open('HS.txt', 'w') # Change the file name to the same as the prompt

openai.api_key = "..." # Enter your openai key
# dataFile = '/../NLI_dataset_using_LLM/data/coco/captions_train2017.json' # coco dataset path settings
dataFile = '/../NLI_dataset_using_LLM/data/snli/snli_train.json' # snli dataset path settings
promptFile = '/../NLI_dataset_using_LLM/prompt/HS_prompt.txt' # Set prompt file path

entailment = 'entailment' # Label settings
contradiction = 'contradiction'
neutral = 'neutral'

with open(dataFile) as f:
    json_data = json.load(f)
with open(promptFile, "r") as F:
    promptline = []
    for line in F:
        promptline.append(line.strip())

for i in range(0, 1000):   # Number of data to generate
    senten = re.sub(r'[\n*.,"\'-?:!;]','',str(json_data[i]))
    response = openai.Completion.create( 
            model="text-davinci-003", 
            prompt = str(promptline) + "What is the answer when the input sentence is "+senten+"?",
            temperature = 0,
            max_tokens= 300,
            top_p = 1,
            frequency_penalty = 0.0,
            presence_penalty = 0.0
        )

    if "@" not in response:
        print(entailment + '\t'+ senten.replace(".","") + '\t' + response.choices[0].text.strip().replace("*","").replace(".",""))
        
    # sleep(10)
f.close()
sys.stdout.close()