import re
def classify_with_regex(log_message):
    regex_pattern = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version.*": "System Notification",
        r"File .* uploaded successfully by user.*": "System Notification",
        r"Disk cleanup completed successfully": "System Notification",
        r"System reboot initiated by user": "System Notification",
        r"Account with ID .*": "User Action"
    }

    for pattern,label in regex_pattern.items():
        if re.search(pattern,log_message,re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    print(classify_with_regex("User User1 logged in."))
    print(classify_with_regex("Backup started at 12:00"))
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("System updated to version 1.0"))
    print(classify_with_regex("File file1 uploaded successfully by user user1"))
    print(classify_with_regex("Disk cleanup completed successfully"))
    print(classify_with_regex("System reboot initiated by user"))
    print(classify_with_regex("Account with ID 1234567890"))
    print(classify_with_regex("Hey Bye Hei Bye"))



