from datetime import datetime
from code.backend import errors
from code.backend import validation
from code import images

name_bool, email_bool, phone_bool, address_bool = [False for i in range(4)]


def run(curr_wid, MW):
    def reset():
        curr_wid.le_name.setText('')
        curr_wid.le_email.setText('')
        curr_wid.le_phone.setText('')
        curr_wid.le_address.setText('')

        curr_wid.lb_warning.setText('Enter Details')

        curr_wid.lb_nameico.setPixmap(images.im_enter)
        curr_wid.lb_phoneico.setPixmap(images.im_enter)
        curr_wid.lb_emailico.setPixmap(images.im_enter)
        curr_wid.lb_addressico.setPixmap(images.im_enter)

    def fun_name():
        global name_bool
        name_bool = validation.validName(curr_wid.le_name.text().strip())
        if name_bool:
            curr_wid.lb_nameico.setPixmap(images.im_correct)
        else:
            curr_wid.lb_nameico.setPixmap(images.im_wrong)

    def fun_email():
        global email_bool
        email_bool = validation.validEmail(curr_wid.le_email.text().strip())
        if email_bool:
            curr_wid.lb_emailico.setPixmap(images.im_correct)
        else:
            curr_wid.lb_emailico.setPixmap(images.im_wrong)

    def fun_phone():
        global phone_bool
        phone_bool = validation.validPhone(curr_wid.le_phone.text().strip())
        if phone_bool:
            curr_wid.lb_phoneico.setPixmap(images.im_correct)
        else:
            curr_wid.lb_phoneico.setPixmap(images.im_wrong)

    def fun_address():
        global address_bool
        address_bool = validation.validAddress(curr_wid.le_address.text().strip())
        if address_bool:
            curr_wid.lb_addressico.setPixmap(images.im_correct)
        else:
            curr_wid.lb_addressico.setPixmap(images.im_wrong)

    def okay():
        name = curr_wid.le_name.text().strip()
        email = curr_wid.le_email.text().strip()
        phone = curr_wid.le_phone.text().strip()
        address = curr_wid.le_address.text().strip()
        entry_time = datetime.now()
        exit_time = datetime.now()

        search_data = {'email': email,
                'phone': phone,
                'in_status': True}
        data = {'name': name,
                'email': email,
                'phone': phone,
                'address': address,
                'entry_time': entry_time,
                'exit_time': exit_time,
                'in_status': True}

        from pymongo.errors import ServerSelectionTimeoutError
        myc = MW.myc.logdatabase
        myc = eval('myc.{}_entry'.format(MW.logged_user))
        try:
            if all([name_bool, phone_bool, email_bool, address_bool]):
                found_data = myc.find_one(search_data)
                if found_data:
                    raise errors.PersonAlreadyInError
                else:
                    var = myc.insert_one(data)
                    curr_wid.lb_warning.setText('Entry Done')
            else:
                raise errors.WrongDetailsError
        except ServerSelectionTimeoutError:
            curr_wid.lb_warning.setText('Network Error')
        except errors.PersonAlreadyInError:
            curr_wid.lb_warning.setText('Person Already Inside')
        except errors.WrongDetailsError:
            curr_wid.lb_warning.setText('Wrong Details')

    curr_wid.le_name.textChanged.connect(fun_name)
    curr_wid.le_phone.textChanged.connect(fun_phone)
    curr_wid.le_email.textChanged.connect(fun_email)
    curr_wid.le_address.textChanged.connect(fun_address)

    curr_wid.pushbt_reset.clicked.connect(reset)
    curr_wid.pushbt_okay.clicked.connect(okay)
