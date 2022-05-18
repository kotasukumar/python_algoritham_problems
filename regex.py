import re


def print_message(name, number, date, full_name):
    print(f"Hello {name.group()}, We have your full name as {full_name.group()} in our system. your contact number is "
          f"{number.group()}.\nPlease,let us know in case of any clarification Thank you BridgeLabz {date.group()}.")


if __name__ == "__main__":
    person_name = re.search(r'[\w]{3,}', 'sukumar')
    person_full_name = re.search(r'[\w_]{3,}', 'kota_sukumar')
    date_var = re.search(r'[\d]{2}-[\d]{2}-[\d]{4}', '18-05-2022')
    mobile_number = re.search(r'91[ ][\d]{10}', '91 1234567890')
    print_message(person_name, mobile_number, date_var, person_full_name)
