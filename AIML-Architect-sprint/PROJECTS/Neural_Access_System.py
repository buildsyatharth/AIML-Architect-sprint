# Build a system that processes a batch of raw security logs and organizes them into a verified database.

# Sample raw security logs (for demonstration purposes)
names = [
    "Alexa", "Smith", "Jordan", "Taylor", "Morgan",
    "Alexa", "Jordan", "Smith", "Riley", "Taylor",
    "Morgan", "Alexa", "Casey", "Smith", "Jordan",
    "Riley", "Taylor", "Alexa", "Morgan", "Casey",
    "Smith", "Jordan", "Alexa", "Riley", "Taylor"
]

# Step 1: Process the raw logs to extract unique names and count occurrences
unique_user = set(names)
print("Cleaned and Unique Names:", unique_user)


# Step 2: Create a verified database (in this case, a dictionary) to store the unique names and their counts
security_system = {
    "Alexa":   {"role": "Lead Architect",    "status": "Active"},
    "Smith":   {"role": "Security Analyst",  "status": "Active"},
    "Jordan":  {"role": "Web3 Expert",       "status": "Active"},
    "Taylor":  {"role": "Network Engineer",  "status": "Active"},
    "Morgan":  {"role": "Database Admin",    "status": "Restricted"},
    "Riley":   {"role": "UI Developer",      "status": "Active"},
    "Casey":   {"role": "Visitor",           "status": "Restricted"}
}

# Step 3: The interface to access the verified database
user_name = input("Enter the name to access the security system: ").capitalize()

#Check if the user exists in the verified database and display their role and status
if user_name in security_system:
    #if the user exists, display their role and status
    print(f"---- Access Granted ----")
    print(f"User: {user_name}")
    print(f"Role: {security_system[user_name]['role']}")
    print(f"Status: {security_system[user_name]['status']}")
else:
    #if the user does not exist, display an access denied message
    print("---- Access Denied ----")
    print(f"User '{user_name}' not found in the security system.")  

