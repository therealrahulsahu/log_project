import dns
from pymongo.errors import ConfigurationError, ConnectionFailure, ServerSelectionTimeoutError
from pymongo import MongoClient


def run(curr_wid, MW, on_widget):
    curr_wid.first = True

    def error():
        try:
            curr_wid.lb_warning.setText('Connecting...')
            curr_wid.pushbt_retry.setEnabled(False)
            myc = MongoClient('mongodb://localhost:27017/',
                              serverSelectionTimeoutMS=5000, connectTimeoutMS=5000, socketTimeoutMS=5000)
            MW.myc = myc
            on_widget()
        except (dns.exception.Timeout, ConfigurationError):
            curr_wid.lb_warning.setText('DNS Not Found')
            curr_wid.pushbt_retry.setEnabled(True)
        except ConnectionFailure:
            curr_wid.lb_warning.setText('Connection Failed')
            curr_wid.pushbt_retry.setEnabled(True)
        except ServerSelectionTimeoutError:
            curr_wid.lb_warning.setText('Server Down')
            curr_wid.pushbt_retry.setEnabled(True)

    def choose():
        if curr_wid.first:
            curr_wid.first = False
            curr_wid.pushbt_retry.setText('Retry')
            error()
        else:
            error()

    curr_wid.pushbt_retry.setText('Connect')
    curr_wid.pushbt_retry.clicked.connect(choose)
