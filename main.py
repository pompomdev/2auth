# Added the remove system and made error messages more specific.

import pyotp
import time
import pickle
import os


def save_entries():
    name = input("Name: ")
    secret = input("Secret: ")

    if name and secret:
        try:
            with open('data/entries.2auth', 'rb') as file:
                saved_entries = pickle.load(file)
        except FileNotFoundError:
            saved_entries = {}

        saved_entries[name] = secret

        os.makedirs('data', exist_ok=True)

        with open('data/entries.2auth', 'wb') as file:
            pickle.dump(saved_entries, file)

        print(f"\nEntry for \"{name}\" has been saved successfully.\n")
    else:
        print("Please fill in all fields correctly.")


def remove_entry():
    if os.path.exists('data/entries.2auth'):
        with open('data/entries.2auth', 'rb') as file:
            saved_entries = pickle.load(file)

        if saved_entries:
            print("\nExisting Entries:")
            print("-----------------")
            for entry in saved_entries:
                print(entry)
            print("-----------------\n")
        else:
            print("\nNo entries found.\n")
            return

        entry_to_remove = input("Enter the name of the entry you want to remove: ")

        if entry_to_remove in saved_entries:
            del saved_entries[entry_to_remove]

            with open('data/entries.2auth', 'wb') as file:
                pickle.dump(saved_entries, file)

            print(f"\nEntry \"{entry_to_remove}\" has been removed successfully.\n")
        else:
            print(f"\nEntry \"{entry_to_remove}\" not found.\n")
    else:
        print("\nNo saved entries found.\n")


def generate_codes():
    if os.path.exists('data/entries.2auth'):
        with open('data/entries.2auth', 'rb') as file:
            saved_entries = pickle.load(file)

        if saved_entries:
            print("\nExisting Entries:")
            print("-----------------")
            for entry in saved_entries:
                print(entry)
            print("-----------------\n")
        else:
            print("\nNo entries found.\n")
            return

        entries = input("Enter the names of the entries separated by commas (e.g., entry1,entry2): ")
        entries = entries.split(',')

        if entries:
            otps = {}
            entries_not_found = []
            for entry in entries:
                if entry in saved_entries:
                    secret = saved_entries[entry]
                    otp = pyotp.TOTP(secret)
                    otps[entry] = otp
                else:
                    entries_not_found.append(entry)

            if entries_not_found:
                print(f"\nThe following entries were not found: {', '.join(entries_not_found)}\n")

            if otps:
                print("\nGenerating OTP Codes:")
                print("---------------------")
                while True:
                    for entry, otp in otps.items():
                        try:
                            code = otp.now()
                            print(f"The OTP code for \"{entry}\" is: {code}")
                        except pyotp.pyotp.ExpiredToken:
                            print(f"The OTP code for \"{entry}\" has expired.")
                
                    print("---------------------")
                    time.sleep(30)
            else:
                print("\nNo entries found.\n")

        else:
            print("\nNo entries provided.\n")

    else:
        print("\nNo saved entries found.\n")


def print_menu():
    print("2Auth Safer")
    print("-----------")
    print("1. Save Entries")
    print("2. Generate OTP Codes")
    print("3. Remove Entry")
    print("4. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            save_entries()
        elif choice == "2":
            generate_codes()
        elif choice == "3":
            remove_entry()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
