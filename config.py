import pymongo
import certifi


con_str = "mongodb+srv://supremeedan:nikesb69@cluster0.frorz.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("ShoeVault")
