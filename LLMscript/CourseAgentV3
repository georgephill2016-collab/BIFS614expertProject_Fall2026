from transformers import AutoTokenizer, AutoModelForCausalLM

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Open-source model
# Phi-2 is a base causal language model, not an instruction-tuned chat model.
# It was trained heavily on textbook, QA, and code-style data, so when you write
# some guardrails, Phi-2 often continues with something that looks like code,
# a function, or a template because that matches patterns it saw during training.
MODEL_NAME = "microsoft/phi-2"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
model.eval()
print("Model loaded successfully.")
print("Type 'quit', 'exit', or 'q' to stop.\n")

# ----------------------------
# Interactive chat loop
# ----------------------------

#Conversation History
history = []

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    if not user_input:
        continue

    history.append(f"user:{user_input}")

    # Count input tokens
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
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
    response = tokenizer.decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)

    # Count output tokens
    output_token_count = len(generated_ids)

    # Total tokens
    total_token_count = input_token_count + output_token_count

    # Display results
    print("Response:", response.strip())
    print(f"Input Tokens:  {input_token_count}")
    print(f"Output Tokens: {output_token_count}")
    print(f"Total Tokens:  {total_token_count}")
