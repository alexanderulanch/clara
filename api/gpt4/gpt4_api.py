import os
import openai
from transformers import BartTokenizer, BartForConditionalGeneration

openai.api_key = os.environ["OPENAI_API_KEY"]

tokenizer = BartTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
summarization_model = BartForConditionalGeneration.from_pretrained(
    "sshleifer/distilbart-cnn-12-6"
)


def process_conversation_history(conversation, threshold=3900):
    formatted_messages = "\n".join(
        [f"{role}: {message}" for role, message in conversation]
    )

    if len(formatted_messages) <= threshold:
        return conversation

    inputs = tokenizer(
        formatted_messages, return_tensors="pt", max_length=threshold, truncation=True
    )
    summary_ids = summarization_model.generate(
        inputs["input_ids"], num_return_sequences=1, max_length=100
    )
    summarized_conversation = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    summarized_messages = [
        {"role": role, "content": message.strip()}
        for line in summarized_conversation.splitlines()
        for role, message in (line.split(":", 1),)
        if len(line.split(":", 1)) == 2
    ]

    return summarized_messages


def generate_response(conversation, model="gpt-4", max_tokens=50, temperature=0.5):
    processed_conversation = process_conversation_history(conversation)
    formatted_messages = [
        {"role": role, "content": message} for role, message in processed_conversation
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=formatted_messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    if response.choices:
        return response.choices[0].message["content"]
    return ""
