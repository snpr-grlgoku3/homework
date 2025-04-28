import sys

def shutdown():
    response = input("Are you sure you want to shut down the program? (yes/no): ").strip().lower()
    if response == "yes":
        print("Shutting down the program...")
        sys.exit()
    else:
        print("Shutdown cancelled. Continuing the program...")
print("Program is running...")
shutdown()