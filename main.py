import openai
from dotenv import find_dotenv, load_dotenv


load_dotenv()
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

# # == Create our Assistant ==
personal_trainer_assis = client.beta.assistants.create(
     name="Software Engineer",
     instructions="""You are a software engineer. you will write code and build projects as per the user requirements. """,
     model=model,
 )
asistant_id = personal_trainer_assis.id
print(asistant_id)


# === Thread  ===
thread = client.beta.threads.create(
     messages=[
         {
            "role": "user",
             "content": "write an fibonacci series program in python",
         }
     ]
 )
thread_id = thread.id
print(thread_id)