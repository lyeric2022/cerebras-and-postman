import os
from cerebras.cloud.sdk import Cerebras

client = Cerebras(
    # This is the default and can be omitted
    api_key="INSERT API KEY"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Give me back a tetris game in python code",
        }
    ],
    model="llama-4-scout-17b-16e-instruct",
)

# Extract just the message content
message_content = chat_completion.choices[0].message.content

# Print just the message
print(message_content)

# Write just the message content to a file
with open("message_only.txt", "w") as file:
    file.write(message_content)