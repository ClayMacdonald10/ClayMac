# Lab 11: Creating and using a fine-tuned model
# Lab 11b: On line 14 enter the job ID obtained from Lab 11a
# The fine tuning may take ten to twenty minutes. Once you run this script and obtain "succeeded", write down/copy the model ID and use it for lab11c
# Note: OpenAI sends an email once the job is complete, but as you are using my OPenAI key, I will receive it

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")
openai_model = 'gpt-4o-mini' 
client = OpenAI(api_key = api_key)

job_id = "ftjob-Au8MSIzl0l1PySX3RssR7Kks" # <----------- Copy your Job ID here

job = client.fine_tuning.jobs.retrieve(job_id)

print("Status:", job.status)
# Status Results:
# - validating_files: The dataset is being checked for format and content issues.
# - queued: The job is waiting in line to start fine-tuning.
# - running: The fine-tuning job is actively in progress.
# - succeeded: The job completed successfully, and your model is ready to use!
# - failed: The job encountered an error and did not complete.
# - cancelled: The job was cancelled (manually or automatically).

print("Fine-tuned model:", job.fine_tuned_model) # <------- Find your Model ID here