# Sample chat logs
chat_logs = [
    "My order is delayed",
    "I want to return my purchase",
    "The app is crashing frequently",
    "Payment issues, please help",
    "Need help with account recovery",
    "Delivery was incomplete",
    "Can't login to my account",
    "Having trouble with checkout"
]

# Function to categorize issues
categories = {"Order": 0, "App": 0, "Payment": 0, "Account": 0, "Delivery": 0}

def categorize_issues(chat_logs):
    for log in chat_logs:
        log_lower = log.lower()  # Convert the log to lowercase
        for category in categories.keys():
            if category.lower() in log_lower:
                categories[category] += 1

# Step 2: Function to search by keyword
def keyword_search(keyword, chat_logs):
    keyword_lower = keyword.lower()  # Convert the keyword to lowercase for case-insensitive search
    matched_logs = [log for log in chat_logs if keyword_lower in log.lower()]
    return matched_logs

# Step 3: Display and search
keyword = input("Enter the search keyword: ")
matched_logs = keyword_search(keyword, chat_logs)

if matched_logs:
    print(f"Logs containing the keyword '{keyword}':")
    for log in matched_logs:
        print(f"- {log}")
else:
    print(f"No logs found containing the keyword '{keyword}'.")

# Run the categorization function
categorize_issues(chat_logs)
print("Categories count after categorization:", categories)
