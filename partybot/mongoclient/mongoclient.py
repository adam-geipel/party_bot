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
        users = db.discord_users.find()
        
        return users.to_list(None)
    
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

    try:
        db = await get_db()
        await db.discord_users.insert_one(
            {
                "uid": user.id,
                "name": user.name
            }   
        )
        
    except Exception as e:
        print("Failed to add user to collection", e)

async def add_user_subscription(user_id, guild_id, channel_id):
    try:
        db = await get_db()
        await db.discord_users.find_one_and_update(
            {"uid" : user_id },
            {"$push": 
                {
                    "subscriptions": {
                        "guild_id": guild_id,
                        "channel_id": channel_id
                    }
                }
            }, upsert=True
        )
        
    except Exception as e: 
        print("Failed to add user subscription")
        print(e)

async def find_users_by_guild_subscription(guild_id, channel_id):
    try: 
        db = await get_db()
        subscribed_users = await db.discord_users.find(
            { 
                 "subscriptions.guild_id" : { "$eq" : guild_id} , 
                 "subscriptions.channel_id" : { "$eq" : channel_id} 
            }
            ).to_list(None)
        
        print(subscribed_users)
    except Exception as e: 
       print("Failed to enumerate users subscribed to channel")  
       print(e)   
    
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
        
# asyncio.run(add_user(type('obj', (object,), {'id': 2, 'name': "bar"})))
# asyncio.run(get_discord_users())
# asyncio.run(get_discord_user_by_id(1))
# asyncio.run(add_user_subscription(1, "baz", "bash"))
# asyncio.run(find_users_by_guild_subscription("foo", "bar"))