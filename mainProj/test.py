from pymongo import MongoClient

# Replace with your MongoDB connection string
connection_string = "mongodb+srv://f20212168:pratham@cluster0.dibpce3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

# Access the specific database and collection
db = client["test"]
collection = db["users"]

# Define a function to count users
def count_users():
    return collection.count_documents({})

# Main function to run the script
if __name__ == "__main__":
    user_query = input("Enter your query: ")

    if user_query.lower() == "how many users are there?":
        count = count_users()
        print(f"Generated MongoDB Query: {{'query': 'db.users.count()'}}")
        print(f"Query Result: {count}")
    else:
        print("Unknown query.")
