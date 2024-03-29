from datetime import datetime
from images import im_enter, im_wrong, im_correct
from errors import PersonAlreadyInError, WrongDetailsError
from .validation import validName, validAddress, validPhone, validEmail

name_bool, email_bool, phone_bool, address_bool = [False for i in range(4)]


def run(curr_wid, MW):

    def reset():
        curr_wid.le_name.setText('')
        curr_wid.le_email.setText('')
        curr_wid.le_phone.setText('')
        curr_wid.le_address.setText('')

        curr_wid.lb_warning.setText('Enter Details')

        curr_wid.lb_nameico.setPixmap(im_enter)
        curr_wid.lb_phoneico.setPixmap(im_enter)
        curr_wid.lb_emailico.setPixmap(im_enter)
        curr_wid.lb_addressico.setPixmap(im_enter)

    reset()

    def fun_name():
        global name_bool
        name_bool = validName(curr_wid.le_name.text().strip())
        if name_bool:
            curr_wid.lb_nameico.setPixmap(im_correct)
        else:
            curr_wid.lb_nameico.setPixmap(im_wrong)

    def fun_email():
        global email_bool
        email_bool = validEmail(curr_wid.le_email.text().strip())
        if email_bool:
            curr_wid.lb_emailico.setPixmap(im_correct)
        else:
            curr_wid.lb_emailico.setPixmap(im_wrong)

    def fun_phone():
        global phone_bool
        phone_bool = validPhone(curr_wid.le_phone.text().strip())
        if phone_bool:
            curr_wid.lb_phoneico.setPixmap(im_correct)
        else:
            curr_wid.lb_phoneico.setPixmap(im_wrong)

    def fun_address():
        global address_bool
        address_bool = validAddress(curr_wid.le_address.text().strip())
        if address_bool:
            curr_wid.lb_addressico.setPixmap(im_correct)
        else:
            curr_wid.lb_addressico.setPixmap(im_wrong)

    def okay():
        name = curr_wid.le_name.text().strip().lower()
        email = curr_wid.le_email.text().strip()
        phone = curr_wid.le_phone.text().strip()
        address = curr_wid.le_address.text().strip()
        entry_time = datetime.now()
        exit_time = datetime.now()

        search_data1 = {'email': email,
                'in_status': True}
        search_data2 = {'phone': phone,
                'in_status': True}
        data = {'name': name,
                'email': email,
                'phone': phone,
                'address': address,
                'entry_time': entry_time,
                'exit_time': exit_time,
                'in_status': True}

        from pymongo.errors import AutoReconnect
        myc = MW.myc.logdatabase
        myc = eval('myc.{}_entry'.format(MW.logged_user))
        try:
            if all([name_bool, phone_bool, email_bool, address_bool]):
                found_data = myc.find_one(search_data1) or myc.find_one(search_data2)
                if found_data:
                    raise PersonAlreadyInError
                else:
                    var = myc.insert_one(data)
                    curr_wid.lb_warning.setText('Entry Done')
            else:
                raise WrongDetailsError
        except AutoReconnect:
            curr_wid.lb_warning.setText('Network Error')
        except PersonAlreadyInError:
            curr_wid.lb_warning.setText('Person Already Inside')
        except WrongDetailsError:
            curr_wid.lb_warning.setText('Wrong Details')

    curr_wid.le_name.textChanged.connect(fun_name)
    curr_wid.le_phone.textChanged.connect(fun_phone)
    curr_wid.le_email.textChanged.connect(fun_email)
    curr_wid.le_address.textChanged.connect(fun_address)

    curr_wid.pushbt_reset.clicked.connect(reset)
    curr_wid.pushbt_okay.clicked.connect(okay)
