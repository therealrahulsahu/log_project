from pymongo import MongoClient as __client
myc_localhost = __client("mongodb://localhost:27017/")
myc_web = __client('mongodb+srv://therealrahulsahu:rahulsahu1_@democluster-2u6fb.gcp.mongodb.net/test?retryWrites=true')

