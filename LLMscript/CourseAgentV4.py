from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Open-source model
# The Phi-3-Mini-4K-Instruct is a 3.8B parameters, lightweight, state-of-the-art open model trained
# with the Phi-3 datasets that includes both synthetic data and the filtered publicly available websites
# data with a focus on high-quality and reasoning dense properties. The model belongs to the Phi-3 family
# with the Mini version in two variants 4K and 128K which is the context length (in tokens) that it can support.

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

# ----------------------------
# Phi-3 special tokens
# ----------------------------
"""
<|system|>: Marks the beginning of a system instruction block.
<|user|>: Marks the beginning of a user prompt/input.
<|assistant|>: Marks the beginning of the model's response - generate the assistant reply next.
<|end|>: Denotes the termination of a turn or message block.
<|step|>: Used for multi-step reasoning or intermediate generation markers.
<|raw|>: Denotes raw text input/output sections.
<|continue|>: Signals the model to carry on a truncated or paused generation.
<|tag|>: Used for metadata or specialized tagging. 
"""

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
model.eval()
print("Model loaded successfully.")
print("Type 'quit', 'exit', or 'q' to stop.\n")

# Context
"""
CONTEXT
Context is the memory and background information from a chat that helps a chatbot understand what you mean and give smart answers.
What Context Includes
Conversation history: Past messages and replies in a chat.
user prompt: your current question or command
Current goal: The specific task or problem you are trying to solve right now.
System rules/instructions: Instructions that tell the bot how to act or what role to play.
Retrieved Data: External documents pulled in through tools like Retrieval-Augmented Generation (RAG).
THE CONTEXT WINDOW
The Context Window is the strict limit on how much data can fit into this working memory. 
It is measured in tokens (roughly parts of words, where 1,000 tokens equal about 750 words).
If a conversation or document goes over this limit, the oldest information falls out of memory and the model forgets it.
Managing this limited space well is now known as context engineering.
WHY CONTEXT MATTERS
Fixes confusion: The bot understands words like "it" or "there" based on what you said before.
Stops repetition: You do not have to repeat your name or problem in every new message.
Feels natural: The chat flows smoothly, just like a talk between two humans. [2, 3, 4]
context also shapes the flow of the chat and changes every time the bot moves to a new step
"""

# ----------------------------
# Interactive chat loop
# ----------------------------

while True:
    user_prompt = input("You: ").strip()

    if user_prompt.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    if not user_prompt:
        continue

    context = f"""
    <|system|>
    You are a helpful assistant.<|end|>
    <|user|>
    {user_prompt}<|end|>
    <|assistant|>
    """

    # Count input tokens
    input_ids = tokenizer.encode(context, return_tensors="pt")
    input_token_count = input_ids.shape[1]

    # Generate response
    with torch.no_grad():
        output_ids = model.generate(
            input_ids, max_new_tokens=50, do_sample=True, temperature=0.7, top_p=0.9, repetition_penalty=1.0,
            pad_token_id=tokenizer.eos_token_id
        )

    # Extract generated tokens only
    generated_ids = output_ids[0][input_token_count:]
    response = tokenizer.decode(
        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )

    # Keep only the first line of the response
    response = response.strip()
    if "\n" in response:
        response = response.split("\n")[0]
    # Optional: stop if another role tag appears
    for stop_tag in ["<|user|>", "<|assistant|>", "<|system|>", "<|end|>"]:
        if stop_tag in response:
            response = response.split(stop_tag)[0].strip()

    # Count output tokens
    output_token_count = len(generated_ids)

    # Total tokens
    total_token_count = input_token_count + output_token_count

    # Display results
    print("Response:", response.strip())
    print(f"Input Tokens:  {input_token_count}")
    print(f"Output Tokens: {output_token_count}")
    print(f"Total Tokens:  {total_token_count}")
