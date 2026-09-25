from transformers import AutoTokenizer, AutoModelForCausalLM

import torch


# Open-source model

MODEL_NAME = "microsoft/phi-2"


# Load tokenizer and model

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)


# Prompt
#prompt = "how are you?"
prompt = input("Input your question:").strip()


# Count input tokens

input_ids = tokenizer.encode(prompt, return_tensors="pt")

input_token_count = input_ids.shape[1]


# Generate response

with torch.no_grad():

    output_ids = model.generate(

        input_ids,

        max_new_tokens=50,

        do_sample=True,

        temperature=0.7

    )


# Extract generated tokens only

generated_ids = output_ids[0][input_token_count:]

response = tokenizer.decode(generated_ids, skip_special_tokens=True)


# Count output tokens

output_token_count = len(generated_ids)


# Total tokens

total_token_count = input_token_count + output_token_count


# Display results

#print("Prompt:", prompt)

print("Response:", response.strip())

print(f"Input Tokens:  {input_token_count}")

print(f"Output Tokens: {output_token_count}")

print(f"Total Tokens:  {total_token_count}")
