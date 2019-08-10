from errors import WrongEmailError, WrongUsernameError

from images import im_correct, im_enter, im_wrong


def run(curr_wid, MW):
    curr_wid.lb_usernameico.setPixmap(im_enter)

    def fetch():
        username = curr_wid.le_username.text().strip()
        email = curr_wid.le_email.text().strip()
        recoveryhint = curr_wid.le_recoveryhint.text().strip()

        myc = MW.myc
        from pymongo.errors import AutoReconnect
        query = {'username': username}
        try:
            result = myc.logdatabase.users.find_one(query)
            if bool(result):
                if result['email'] == email and result['recoveryhint'] == recoveryhint:
                    curr_wid.lb_warning.setText('Password :<h4>{}</h4>'.format(result['password']))
                else:
                    raise WrongEmailError
            else:
                raise WrongUsernameError

        except AutoReconnect:
            curr_wid.lb_warning.setText('Network Error')
        except WrongEmailError as e:
            curr_wid.lb_warning.setText(str(e))
            curr_wid.lb_usernameico.setPixmap(im_correct)
        except WrongUsernameError as e:
            curr_wid.lb_warning.setText(str(e))
            curr_wid.lb_usernameico.setPixmap(im_wrong)

    curr_wid.pushbt_fetch.clicked.connect(fetch)
