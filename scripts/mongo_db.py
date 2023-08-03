import datetime
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

import certifi
ca = certifi.where()

load_dotenv()


class MongoDB:
    def __init__(self):
        self.db_user = os.getenv('MONGO_ATLAS_USER')
        self.db_password = os.getenv("MONGO_ATLAS_PW")
        self.db_suffix = os.getenv("MONGO_ATLAS_SUFFIX")
        self.db_name = os.getenv("MONGO_ATLAS_DB")

        uri = f"mongodb+srv://{self.db_user}:{self.db_password}@{self.db_suffix}/{self.db_name}"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca, retryWrites=True)

        self.database = self.client[self.db_name]

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def add_user(self, user):
        coll = self.database.users
        user_id = user['user_id']

        document = coll.find_one({'user_id': user_id})

        # Check if user exists
        if document is not None:
            new_user = False
            # if 'questions_remaining' not in user:
            #     new_user = True
        else:
            new_user = True

        result = coll.update_one({'user_id': user_id}, {'$set': user}, upsert=True)

        if new_user:
            set_questions_remaining = {"questions_remaining": 3}
            coll.update_one({'user_id': user_id}, {'$set': set_questions_remaining}, upsert=True)

        print(f"User added/updated: {user_id}")

        return True

    def get_questions_remaining(self, user_id):
        coll = self.database.users

        document = coll.find_one({'user_id': user_id})

        if document is not None:
            return document['questions_remaining']
        else:
            return 0

    def decrement_questions_remaining(self, user_id):
        coll = self.database.users

        document = coll.find_one({'user_id': user_id})

        if document is not None:
            questions_remaining = document['questions_remaining']
            if questions_remaining > 0:
                questions_remaining -= 1
                coll.update_one({'user_id': user_id}, {'$set': {'questions_remaining': questions_remaining}})
                return questions_remaining
            else:
                return 0
        else:
            return 0

    def store_qa(self, user_id, question, answer, holybook, holyfigure, response_id):
        coll = self.database.questions

        mongo_doc = {
            'user_id': user_id,
            'holy_book': holybook,
            'holy_figure': holyfigure,
            'question': question,
            'answer': answer,
            'response_id': response_id,
            'date': datetime.datetime.utcnow()
        }

        coll.insert_one(mongo_doc)
        return True

    def store_openai_response(self, object):
        coll = self.database.openai_responses

        coll.insert_one(object)
        return True
