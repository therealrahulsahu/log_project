from errors import NotFoundError


def to_html(data):
    val = ''
    for x in data:
        entry_time = x['entry_time'].strftime('%c')

        if x['in_status']:
            exit_time = ''
        else:
            exit_time = x['exit_time'].strftime('%c')

        arg = [x['name'].strip(), ' '*3, entry_time.strip(), ' '*3,
               exit_time.strip(), ' '*3, x['email'].strip(), ' '*3, x['phone'].strip()]
        temp = '{:<20}{}In:{:<30}{}Out:{:<30}{}Mail:{:<40}{}Phone:{:^10}'.format(*arg)
        val += temp + '\n\n'
    return val


def run(curr_wid, MW):
    def fetch():
        search_text = curr_wid.le_name.text()
        count = curr_wid.le_nosdoc.text()

        query = {'name': {'$regex': search_text}}
        filter_data = {'_id': 0}
        myc = MW.myc
        myc = eval('myc.logdatabase.{}_entry'.format(MW.logged_user))
        from pymongo.errors import ServerSelectionTimeoutError
        try:
            count = int(count)
            data = list(myc.find(query, filter_data).limit(count))
            if data:
                curr_wid.tb_data.setText(to_html(data))
            else:
                raise NotFoundError
        except ServerSelectionTimeoutError:
            curr_wid.tb_data.setText('<h4>Network Error</h4>')
        except ValueError:
            curr_wid.tb_data.setText('<h4>Invalid No.</h4>')
        except NotFoundError:
            curr_wid.tb_data.setText('<h4>No Data Found</h4>')

    curr_wid.pushbt_fetch.clicked.connect(fetch)