from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq = Groq()

def classify_with_llm(log_message):
    prompt = f"""
    Classify the log message into one of the these categories:
    (1)Workflow Error , (2) Depreciation Warning .
    If you cant figure out a category , return "Unclassified".
    Only return the category name .No preamble
    Log message: {log_message}

"""

    chat_completion = groq.chat.completions.create(
    model="llama3-70b-8192",
    messages=[

        {
            "role": "user",
            "content": prompt,
        }
    ])

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    print(classify_with_llm("System reboot initiated by user"))
    print(classify_with_llm("Case escalation for Ticket Id 76 failed because the associated case is already closed"))
