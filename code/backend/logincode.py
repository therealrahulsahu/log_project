from pymongo.errors import ServerSelectionTimeoutError
from code.images import im_wrong, im_correct, im_loading


class notFoundError(Exception):
    def __init__(self):
        pass


def run(MW):

    def login():
        in_username = MW.le_username.text().strip()
        in_password = MW.le_password.text().strip()
        from code.mongo_conn import myc_localhost as myc
        query = {'username': in_username}
        try:
            result = myc.logdatabase.users.find_one(query)
            MW.lb_loginico.setPixmap(im_loading)
            if bool(result):
                if result['password'] == in_password:
                    MW.lb_loginico.setPixmap(im_correct)
                else:
                    raise notFoundError
            else:
                raise notFoundError
        except(notFoundError, ServerSelectionTimeoutError):
            MW.lb_loginico.setPixmap(im_wrong)  # object name of lb_ has to be changed
        finally:
            myc.close()

    MW.pushbt_login.clicked.connect(login)
"""    def signup():
        pass

    def forget():
        pass
"""

    #MW.pushbt_signup.clicked.connect(signup)
    #MW.pushbt_forget.clicked.connect(forget)

