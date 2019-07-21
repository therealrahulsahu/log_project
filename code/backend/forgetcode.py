from code.backend import errors


def run(curr_wid, MW):
    def fetch():
        username = curr_wid.le_username.text().strip()
        email = curr_wid.le_email.text().strip()
        recoveryhint = curr_wid.le_recoveryhint.text().strip()

        myc = MW.myc
        from pymongo.errors import ServerSelectionTimeoutError
        query = {'username': username}
        try:
            result = myc.logdatabase.users.find_one(query)
            if bool(result):
                if result['email'] == email and result['recoveryhint'] == recoveryhint:
                    curr_wid.lb_warning.setText('Password :<h4>{}</h4>'.format(result['password']))
                else:
                    raise errors.WrongEmailError
            else:
                raise errors.WrongUsernameError

        except ServerSelectionTimeoutError:
            curr_wid.lb_warning.setText('Network Error')
        except errors.WrongEmailError as e:
            curr_wid.lb_warning.setText(str(e))
            from code.images import im_correct
            curr_wid.lb_usernameico.setPixmap(im_correct)
        except errors.WrongUsernameError as e:
            curr_wid.lb_warning.setText(str(e))
            from code.images import im_wrong
            curr_wid.lb_usernameico.setPixmap(im_wrong)

    curr_wid.pushbt_fetch.clicked.connect(fetch)
