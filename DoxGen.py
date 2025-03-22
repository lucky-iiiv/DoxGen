import json
import os

def get_input(prompt):
    value = input(prompt)
    return None if value.lower() == "skip" else value

def main():
    print("""
    
.____                   __           .___.___._______   ____
|    |    __ __   ____ |  | _____.__.|   |   |   \   \ /   /
|    |   |  |  \_/ ___\|  |/ <   |  ||   |   |   |\   Y   /
|    |___|  |  /\  \___|    < \___  ||   |   |   | \     /  
|_______ \____/  \___  >__|_ \/ ____||___|___|___|  \___/   
        \/           \/     \/\/                            

Calculator made by luckyiiiv#4938 (anxym.exe)
    """)
    
    print("Welcome to the Dox Generator. Type 'skip' to leave a field blank.")
    
    data = {
        "Personal": {
            "First Name": get_input("First Name: "),
            "Last Name": get_input("Last Name: "),
            "Age": get_input("Age: "),
            "Gender": get_input("Gender: "),
            "Birthday": get_input("Birthday: "),
            "Zodiac Sign": get_input("Zodiac Sign: "),
            "Height": get_input("Height: "),
            "Hair Color": get_input("Hair Color: "),
            "Interests": get_input("Interests (comma separated): ")
        },
        "Socials": {
            "Discord": get_input("Discord Username: "),
            "Roblox": get_input("Roblox Username: "),
            "TikTok": get_input("TikTok Username: "),
            "Snapchat": get_input("Snapchat Username: "),
            "Instagram": get_input("Instagram Username: ")
        },
        "Contact": {
            "Phone Number": get_input("Phone Number: "),
            "Email": get_input("Email: ")
        },
        "Location": {
            "Country": get_input("Country: "),
            "State": get_input("State: "),
            "City": get_input("City: "),
            "Address": get_input("Address: ")
        },
        "IP Information": {
            "IP Address": get_input("IP Address: "),
            "ISP": get_input("ISP: "),
            "City": get_input("IP City: "),
            "Region": get_input("IP Region: "),
            "Country": get_input("IP Country: ")
        }
    }
    
    def clean_dict(d):
        return {k: v for k, v in d.items() if v}
    
    data = {k: clean_dict(v) for k, v in data.items() if clean_dict(v)}
    
    file_name = "dox_data.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    
    print(f"\nDox file saved as {file_name} in {os.getcwd()}")
    
if __name__ == "__main__":
    main()
