from pymongo.errors import ServerSelectionTimeoutError
from code.images import im_wrong, im_correct, im_loading
from code.backend import errors


def run(curr_wid, MW):
    def login():
        in_username = curr_wid.le_username.text().strip()
        in_password = curr_wid.le_password.text().strip()
        myc = MW.myc
        query = {'username': in_username}
        try:
            result = myc.logdatabase.users.find_one(query)
            curr_wid.lb_loginico.setPixmap(im_loading)
            if bool(result):
                if result['password'] == in_password:
                    curr_wid.lb_loginico.setPixmap(im_correct)
                    MW.logged_user = '{}'.format(result['username'])
                    MW.feature_wid()
                else:
                    raise errors.NotFoundError
            else:
                raise errors.NotFoundError
        except(errors.NotFoundError, ServerSelectionTimeoutError):
            curr_wid.lb_loginico.setPixmap(im_wrong)

    curr_wid.pushbt_login.clicked.connect(login)

