from code import (validAddress, validEmail, validPhone, validName)
import datetime


def add_doc(details):
    import pandas as pd
    import os
    dataDirectory = os.path.expanduser("~") + "\\Documents"
    try:
        df = pd.read_csv(dataDirectory+'\\log\\log_data.csv')
        df = df.iloc[:, 1:]
        df = df.append(details, ignore_index=True)
        df.to_csv(dataDirectory+'\\log\\log_data.csv')
    except FileNotFoundError:
        try:
            os.mkdir(dataDirectory+'\\log')
        except FileExistsError:
            pass
        df = pd.DataFrame([details])
        df.to_csv(dataDirectory+'\\log\\log_data.csv')
    message = "Saved"
    return message


def run(MW):
    def okay():
        name = MW.name_field.text().strip()
        phone = MW.phone_field.text().strip()
        address = MW.address_field.text().strip()
        email = MW.email_field.text().strip()
        label = ""
        if not validAddress(address):
            label += "Address, "
        if not validEmail(email):
            label += "Email, "
        if not validPhone(phone):
            label += "Phone, "
        if not validName(name):
            label += "Name, "

        if label:
            MW.warning_lb.setText("Invalid : " + label)
        else:
            message = "Valid "
            MW.warning_lb.setText(message)
            curr_time = datetime.datetime.now()
            details = {'name': name, 'email': email, 'phone': phone, 'address': address, 'entry': curr_time}
            status = add_doc(details)
            MW.warning_lb.setText(message+status)

    def reset():
        MW.name_field.setText("")
        MW.phone_field.setText("")
        MW.address_field.setText("")
        MW.email_field.setText("")

    MW.reset_bt.clicked.connect(reset)
    MW.okay_bt.clicked.connect(okay)


def main():
    pass


if __name__ == '__main__':
    main()
