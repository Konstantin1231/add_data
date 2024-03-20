from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings.openai import OpenAIEmbeddings
from pyfiglet import figlet_format
import warnings
warnings.filterwarnings('ignore')


print(figlet_format("Babayan", font= "standard"))
print("1. Type any string and press enter to save it in the database. \n2. Type 'exit' or press Ctr+C to quit the application. \n ")
load_dotenv()
embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
index = "vectordb"
vectorstore = PineconeVectorStore(index_name=index, embedding=embeddings)
try:
    while True:
        user_input = input("Enter new data: \n")
        if user_input == "exit":
            print("Exiting the application. Goodbye!")
            break
        print("")
        vectorstore.add_texts([user_input])
        print(f"Your input has been saved")
except KeyboardInterrupt:
    print("Exiting the application. Goodbye!")
