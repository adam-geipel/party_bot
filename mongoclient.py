import os
import asyncio

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

load_dotenv()

async def ping_server():
    
    client = await get_client()
    
    try:
        client.admin.command('ping')
        print("Pinged your environment. Successfully Connected to the database")
    except Exception as e:
        print(e)
        
async def get_discord_users():
    
    try:
        db = await get_db()
        usersColl = db.discord_users
        users = usersColl.find()
        
        for document in await users.to_list(length=100):
           print(document)
    except Exception as e:
        print(e)

async def get_discord_user_by_id(id):
    
    try:
        db = await get_db()
        user = await db.discord_users.find_one({'uid': id})
        print(user)
    except Exception as e:
        print("Failed to get user by ID")

async def add_user(user):
    
    print(user)
    try:
        users_coll = await get_users_collection()
        await users_coll.insert_one(
            {
                "uid": user.id,
                "name": user.name
            }   
        )
        
    except Exception as e:
        print("Failed to add user to collection", e)

async def get_users_collection():
    
    try:
        db = await get_db()
        return db.discord_users
        
    except Exception as e:
        print("Failed to retrieve discord users collection")
    
async def get_client():
    try:
        uri = os.getenv('DB_CONNECTION_STR')
        client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        return client
    
    except Exception as e:
        print("Failed to retrieve database client connection")
        
        
async def get_db():
    try:
        client = await get_client()
        return client.party_bot
    
    except Exception as e:
        print("Failed to retrieve database")
        
# asyncio.run(add_user(type('obj', (object,), {'id': 1, 'name': "foo"})))

asyncio.run(get_discord_users())
asyncio.run(get_discord_user_by_id(1))