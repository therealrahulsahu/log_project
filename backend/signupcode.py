from errors import AlreadyExistsError, WrongDetailsError, WrongPasswordError ,NotFoundError
from images import im_correct, im_wrong, im_enter
from .validation import validName, validPhone, validEmail, validUsername, validPassword, validRecoveryhint
b_name, b_username, b_password, b_confirmpassword, b_phone, b_email, b_recoveryhint = [False for i in range(7)]


def run(curr_wid,MW):

    def fun_name():
        string = curr_wid.le_name.text().strip()
        global b_name
        b_name = validName(string)
        if b_name:
            curr_wid.lb_nameico.setPixmap(im_correct)
        else:
            curr_wid.lb_nameico.setPixmap(im_wrong)

    def fun_username():
        string = curr_wid.le_username.text().strip()
        global b_username
        b_username = validUsername(string)
        if b_username:
            curr_wid.lb_usernameico.setPixmap(im_correct)
        else:
            curr_wid.lb_usernameico.setPixmap(im_wrong)

    def fun_password():
        string = curr_wid.le_password.text().strip()
        global b_password
        b_password = validPassword(string)
        if b_password:
            curr_wid.lb_passwordico.setPixmap(im_correct)
        else:
            curr_wid.lb_passwordico.setPixmap(im_wrong)

    def fun_confirmpassword():
        string = curr_wid.le_confirmpassword.text().strip()
        string_prev = curr_wid.le_password.text().strip()
        global b_confirmpassword
        b_confirmpassword = validPassword(string)
        if b_confirmpassword:
            if string == string_prev:
                curr_wid.lb_confirmpasswordico.setPixmap(im_correct)
            else:
                curr_wid.lb_confirmpasswordico.setPixmap(im_wrong)
                b_confirmpassword = False
        else:
            curr_wid.lb_confirmpasswordico.setPixmap(im_wrong)

    def fun_phone():
        string = curr_wid.le_phone.text().strip()
        global b_phone
        b_phone = validPhone(string)
        if b_phone:
            curr_wid.lb_phoneico.setPixmap(im_correct)
        else:
            curr_wid.lb_phoneico.setPixmap(im_wrong)

    def fun_email():
        string = curr_wid.le_email.text().strip()
        global b_email
        b_email = validEmail(string)
        if b_email:
            curr_wid.lb_emailico.setPixmap(im_correct)
        else:
            curr_wid.lb_emailico.setPixmap(im_wrong)

    def fun_recoveryhint():
        string = curr_wid.le_recoveryhint.text().strip()
        global b_recoveryhint
        b_recoveryhint = validRecoveryhint(string)
        if b_recoveryhint:
            curr_wid.lb_recoveryhintico.setPixmap(im_correct)
        else:
            curr_wid.lb_recoveryhintico.setPixmap(im_wrong)

    def reset():
        curr_wid.le_name.setText('')
        curr_wid.le_username.setText('')
        curr_wid.le_password.setText('')
        curr_wid.le_confirmpassword.setText('')
        curr_wid.le_phone.setText('')
        curr_wid.le_email.setText('')
        curr_wid.le_recoveryhint.setText('')
        curr_wid.le_adminusername.setText('')
        curr_wid.le_adminpassword.setText('')


        curr_wid.lb_nameico.setPixmap(im_enter)
        curr_wid.lb_usernameico.setPixmap(im_enter)
        curr_wid.lb_passwordico.setPixmap(im_enter)
        curr_wid.lb_confirmpasswordico.setPixmap(im_enter)
        curr_wid.lb_phoneico.setPixmap(im_enter)
        curr_wid.lb_emailico.setPixmap(im_enter)
        curr_wid.lb_recoveryhintico.setPixmap(im_enter)
        curr_wid.lb_admindetailsico.setPixmap(im_enter)

    reset()

    def collect(myc):
        in_name = curr_wid.le_name.text().strip()
        in_username = curr_wid.le_username.text().strip()
        in_password = curr_wid.le_password.text().strip()
        in_phone = curr_wid.le_phone.text().strip()
        in_email = curr_wid.le_email.text().strip()
        in_recoveryhint = curr_wid.le_recoveryhint.text().strip()

        query1 = {'username': in_username}
        if bool(myc.find_one(query1)):
            raise AlreadyExistsError('Username already exists ')

        data = {'name': in_name,
                'username': in_username,
                'password': in_password,
                'phone': in_phone,
                'email': in_email,
                'recoveryhint': in_recoveryhint}

        myc.insert_one(data)
        curr_wid.lb_warning.setText('<h4>User Created</h4>')
        reset()
        MW.login_wid()

    def submit():
        from pymongo.errors import ServerSelectionTimeoutError
        in_adminusername = curr_wid.le_adminusername.text().strip()
        in_adminpassword = curr_wid.le_adminpassword.text().strip()
        query = {'username': in_adminusername}
        try:
            myc = MW.myc
            result = myc.logdatabase.admin.find_one(query)
            if bool(result):
                if result['password'] == in_adminpassword:
                    curr_wid.lb_admindetailsico.setPixmap(im_correct)
                    if all([b_name, b_username, b_password, b_confirmpassword, b_phone, b_email, b_recoveryhint]):
                        collect(myc.logdatabase.users)
                    else:
                        raise WrongDetailsError
                else:
                    raise WrongPasswordError
            else:
                raise NotFoundError

        except ServerSelectionTimeoutError:
            curr_wid.lb_warning.setText('Network Error')
        except WrongPasswordError:
            curr_wid.lb_warning.setText('Invalid Admin Password')
            curr_wid.lb_admindetailsico.setPixmap(im_wrong)
        except NotFoundError:
            curr_wid.lb_warning.setText('Invalid Admin Username')
            curr_wid.lb_admindetailsico.setPixmap(im_wrong)
        except WrongDetailsError:
            curr_wid.lb_warning.setText('Wrong Details')
        except AlreadyExistsError as err:
            curr_wid.lb_warning.setText(str(err))

    curr_wid.le_name.textChanged.connect(fun_name)
    curr_wid.le_username.textChanged.connect(fun_username)
    curr_wid.le_password.textChanged.connect(fun_password)
    curr_wid.le_confirmpassword.textChanged.connect(fun_confirmpassword)
    curr_wid.le_phone.textChanged.connect(fun_phone)
    curr_wid.le_email.textChanged.connect(fun_email)
    curr_wid.le_recoveryhint.textChanged.connect(fun_recoveryhint)

    curr_wid.pushbt_reset.clicked.connect(reset)
    curr_wid.pushbt_submit.clicked.connect(submit)
