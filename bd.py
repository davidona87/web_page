from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


class MongoDriver:
    def __init__(self):

        user= os.getenv('MONGO_USER')
        password= os.getenv('MONGO_PASSWORD')
        hostname= os.getenv('MONGO_HOSTNAME')

        uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection

    def consult(self):
        consulta=self.client.get_database('db_art').get_collection('suministros').find()
        return consulta

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)