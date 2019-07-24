from errors import NotFoundError
from datetime import datetime
index = []


def run(curr_wid, MW):
    def indexing(data):
        return [x['_id'] for x in data]

    def set_to_str(data):
        return ["{}{}{}{}".format(' '*5, x['name'], ' '*10, x['email']) for x in data]

    def mark():
        i = curr_wid.combo_name.currentIndex()
        from pymongo.errors import ServerSelectionTimeoutError
        global index
        result = index[i]
        myc = MW.myc
        myc = eval('myc.logdatabase.{}_entry'.format(MW.logged_user))
        try:
            myc.update_one({'_id': result}, {'$set': {'in_status': False, 'exit_time': datetime.now()}})
            curr_wid.pushbt_mark.setEnabled(False)
            curr_wid.lb_warning.setText('Done')
            curr_wid.combo_name.clear()
        except ServerSelectionTimeoutError:
            curr_wid.lb_warning.setText('Network Error')

    def name():
        curr_wid.combo_name.clear()
        global index
        reg = curr_wid.le_name.text()
        query = {'name': {'$regex': reg}, 'in_status': True}
        filter_data = {'_id': 1, 'name': 1, 'email': 1}
        myc = MW.myc
        myc = eval('myc.logdatabase.{}_entry'.format(MW.logged_user))
        from pymongo.errors import ServerSelectionTimeoutError
        try:
            data = list(myc.find(query, filter_data).limit(5))
            if data:
                curr_wid.combo_name.addItems(set_to_str(data))
                index = indexing(data)
                curr_wid.pushbt_mark.setEnabled(True)
            else:
                raise NotFoundError
        except ServerSelectionTimeoutError:
            curr_wid.pushbt_mark.setEnabled(False)
            curr_wid.lb_warning.setText('Network Error')
            index = []
        except NotFoundError:
            curr_wid.pushbt_mark.setEnabled(False)
            curr_wid.lb_warning.setText('Document Not Found')
            index = []

    curr_wid.pushbt_fetch.clicked.connect(name)
    curr_wid.pushbt_mark.clicked.connect(mark)
