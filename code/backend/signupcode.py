from code.backend import validation
from code.images import im_correct, im_wrong


class NotFoundError(Exception):
    def __init__(self):
        pass


class WrongDetailsError(Exception):
    def __init__(self):
        pass


class WrongPasswordError(Exception):
    def __init__(self):
        pass


class AlreadyExistsError(Exception):
    def __init__(self,mess=""):
        self.mess = mess

    def __str__(self):
        return '{}'.format(self.mess)


b_name, b_username, b_password, b_confirmpassword, b_phone, b_email, b_recoveryhint = [False for i in range(7)]


def run(MW):

    def fun_name():
        string = MW.le_name.text().strip()
        global b_name
        b_name = validation.validName(string)
        if b_name:
            MW.lb_nameico.setPixmap(im_correct)
        else:
            MW.lb_nameico.setPixmap(im_wrong)

    def fun_username():
        string = MW.le_username.text().strip()
        global b_username
        b_username = validation.validUsername(string)
        if b_username:
            MW.lb_usernameico.setPixmap(im_correct)
        else:
            MW.lb_usernameico.setPixmap(im_wrong)

    def fun_password():
        string = MW.le_password.text().strip()
        global b_password
        b_password = validation.validPassword(string)
        if b_password:
            MW.lb_passwordico.setPixmap(im_correct)
        else:
            MW.lb_passwordico.setPixmap(im_wrong)

    def fun_confirmpassword():
        string = MW.le_confirmpassword.text().strip()
        string_prev = MW.le_password.text().strip()
        global b_confirmpassword
        b_confirmpassword = validation.validPassword(string)
        if b_confirmpassword:
            if string == string_prev:
                MW.lb_confirmpasswordico.setPixmap(im_correct)
            else:
                MW.lb_confirmpasswordico.setPixmap(im_wrong)
                b_confirmpassword = False
        else:
            MW.lb_confirmpasswordico.setPixmap(im_wrong)

    def fun_phone():
        string = MW.le_phone.text().strip()
        global b_phone
        b_phone= validation.validPhone(string)
        if b_phone:
            MW.lb_phoneico.setPixmap(im_correct)
        else:
            MW.lb_phoneico.setPixmap(im_wrong)

    def fun_email():
        string = MW.le_email.text().strip()
        global b_email
        b_email = validation.validEmail(string)
        if b_email:
            MW.lb_emailico.setPixmap(im_correct)
        else:
            MW.lb_emailico.setPixmap(im_wrong)

    def fun_recoveryhint():
        string = MW.le_recoveryhint.text().strip()
        global b_recoveryhint
        b_recoveryhint = validation.validRecoveryhint(string)
        if b_recoveryhint:
            MW.lb_recoveryhintico.setPixmap(im_correct)
        else:
            MW.lb_recoveryhintico.setPixmap(im_wrong)

    def reset():
        MW.le_name.setText('')
        MW.le_username.setText('')
        MW.le_password.setText('')
        MW.le_confirmpassword.setText('')
        MW.le_phone.setText('')
        MW.le_email.setText('')
        MW.le_recoveryhint.setText('')
        MW.le_adminusername.setText('')
        MW.le_adminpassword.setText('')

    def collect(myc):
        in_name = MW.le_name.text().strip()
        in_username = MW.le_username.text().strip()
        in_password = MW.le_password.text().strip()
        in_phone = MW.le_phone.text().strip()
        in_email = MW.le_email.text().strip()
        in_recoveryhint = MW.le_recoveryhint.text().strip()

        query1 = {'username': in_username}
        if bool(myc.find_one(query1)):
            raise AlreadyExistsError('Username already exists ')

        data = {'name': in_name,
                'username': in_username,
                'password': in_password,
                'phone': in_phone,
                'email': in_email,
                'recoveryhint': in_recoveryhint}

        from pymongo.errors import ServerSelectionTimeoutError
        try:
            myc.insert_one(data)
            MW.lb_warning.setText('<h4>User Created</h4>')
        except ServerSelectionTimeoutError:
            MW.lb_warning.setText('Network Error')
        finally:
            myc.close()

    def submit():
        from pymongo.errors import ServerSelectionTimeoutError
        in_adminusername = MW.le_adminusername.text().strip()
        in_adminpassword = MW.le_adminpassword.text().strip()
        query = {'username': in_adminusername}
        try:
            from code.mongo_conn import myc_localhost as myc
            result = myc.logdatabase.admin.find_one(query)
            if bool(result):
                if result['password'] == in_adminpassword:
                    MW.lb_admindetailsico.setPixmap(im_correct)
                    if all([b_name, b_username, b_password, b_confirmpassword, b_phone, b_email, b_recoveryhint]):
                        collect(myc.logdatabase.users)
                    else:
                        raise WrongDetailsError
                else:
                    raise WrongPasswordError
            else:
                raise NotFoundError

        except ServerSelectionTimeoutError:
            MW.lb_warning.setText('Network Error')
        except WrongPasswordError:
            MW.lb_warning.setText('Invalid Admin Password')
            MW.lb_admindetailsico.setPixmap(im_wrong)
        except NotFoundError:
            MW.lb_warning.setText('Invalid Admin Username')
            MW.lb_admindetailsico.setPixmap(im_wrong)
        except WrongDetailsError:
            MW.lb_warning.setText('Wrong Details')
        except AlreadyExistsError as err:
            MW.lb_warning.setText(str(err))
        finally:
            myc.close()

    MW.le_name.textChanged.connect(fun_name)
    MW.le_username.textChanged.connect(fun_username)
    MW.le_password.textChanged.connect(fun_password)
    MW.le_confirmpassword.textChanged.connect(fun_confirmpassword)
    MW.le_phone.textChanged.connect(fun_phone)
    MW.le_email.textChanged.connect(fun_email)
    MW.le_recoveryhint.textChanged.connect(fun_recoveryhint)

    MW.pushbt_reset.clicked.connect(reset)
    MW.pushbt_submit.clicked.connect(submit)
