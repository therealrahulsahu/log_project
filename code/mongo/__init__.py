from pymongo import MongoClient
myc_localhost = MongoClient("mongodb://localhost:27017/")
myc_web = MongoClient('mongodb+srv://therealrahulsahu:rahulsahu1_'
                      '@democluster-2u6fb.gcp.mongodb.net/test?retryWrites=true')

