from pymongo.errors import AutoReconnect
from images import im_wrong, im_correct, im_enter, im_loading, im_net_error
from errors import NotFoundError


def run(curr_wid, MW):
    curr_wid.lb_loginico.setPixmap(im_enter)

    def login():
        in_username = curr_wid.le_username.text().strip()
        in_password = curr_wid.le_password.text().strip()
        myc = MW.myc
        query = {'username': in_username}
        try:
            curr_wid.lb_loginico.setPixmap(im_loading)
            result = myc.logdatabase.users.find_one(query)
            if bool(result):
                if result['password'] == in_password:
                    curr_wid.lb_loginico.setPixmap(im_correct)
                    MW.logged_user = '{}'.format(result['username'])
                    MW.feature_wid()
                else:
                    raise NotFoundError
            else:
                raise NotFoundError
        except NotFoundError:
            curr_wid.lb_loginico.setPixmap(im_wrong)
        except AutoReconnect:
            curr_wid.lb_loginico.setPixmap(im_net_error)

    curr_wid.pushbt_login.clicked.connect(login)

