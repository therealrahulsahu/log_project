from pymongo.errors import ServerSelectionTimeoutError
from code.images import im_wrong, im_correct, im_loading


class notFoundError(Exception):
    def __init__(self):
        pass


def run(curr_wid, MW):

    def login():
        in_username = curr_wid.le_username.text().strip()
        in_password = curr_wid.le_password.text().strip()
        from code.mongo_conn import myc_localhost as myc
        query = {'username': in_username}
        try:
            result = myc.logdatabase.users.find_one(query)
            curr_wid.lb_loginico.setPixmap(im_loading)
            if bool(result):
                if result['password'] == in_password:
                    curr_wid.lb_loginico.setPixmap(im_correct)
                else:
                    raise notFoundError
            else:
                raise notFoundError
        except(notFoundError, ServerSelectionTimeoutError):
            curr_wid.lb_loginico.setPixmap(im_wrong)  # object name of lb_ has to be changed
        finally:
            myc.close()

    curr_wid.pushbt_login.clicked.connect(login)
"""    def signup():
        pass

    def forget():
        pass
"""

    #curr_wid.pushbt_signup.clicked.connect(signup)
    #curr_wid.pushbt_forget.clicked.connect(forget)

