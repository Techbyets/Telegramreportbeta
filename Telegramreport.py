import time
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define tool name and creator information
TOOL_NAME = "Telegram account Reporting Tool beta"
MADE_BY = "Developed by TechByets"

# Header with tool name and creator
print(Fore.GREEN + "*****************************************")
print(f"*      {TOOL_NAME:^35} *")
print(f"*      {MADE_BY:^35} *")
print("*****************************************" + Style.RESET_ALL)

def simulate_reporting(username, reason):
    report_count = 0
    try:
        # Run for 10 minutes
        end_time = time.time() + 600  # 10 minutes from now
        
        while time.time() < end_time:
            report_count += 1
            print(Fore.CYAN + f"Sent report to Telegram: Reported user @{username} for reason: {reason}.")
            print(Fore.YELLOW + f"User reported {report_count} times." + Style.RESET_ALL)
            time.sleep(30)  # Show report every 30 seconds
            
        # Cool down for 5 minutes
        print("\n" + Fore.RED + "Cooling down for 5 minutes to avoid detection..." + Style.RESET_ALL)
        time.sleep(300)  # 5 minutes cooldown
        
        # Notify user after cooldown
        print("\n" + Fore.GREEN + "Cooldown period is over. You can run the tool again." + Style.RESET_ALL)
        
    except KeyboardInterrupt:
        print("\n" + Fore.YELLOW + "Tool stopped by user." + Style.RESET_ALL)

if __name__ == "__main__":
    # Prompt user for username and reason
    username = input("Enter the username to report (without @): ")
    reason = input("Enter the reason for reporting: ")

    # Start simulating reporting
    simulate_reporting(username, reason) 
