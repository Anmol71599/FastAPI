import asyncio 
from telethon import TelegramClient, events 
 
async def main(): 
    event = asyncio.Event() 
    bot_token = '5843294524:AAG4f_vpzCh0pasz_3vu37kSVlduP9bUjss' 
    client = TelegramClient('ghj'+bot_token, "25563226", "6f7f9f4e4ea37fd24801af14f2e55fce") 
    await client.start(bot_token=bot_token) 
    bot_chat_id = 5843294524
 
    @client.on(events.NewMessage(chats=bot_chat_id)) 
    async def my_event_handler(event): 
        if event.message.from_id.user_id == 5843294524: 
               if '#AD' in event.message.message or '#paidAD' in event.message.message or 'sponsored' in event.message.message: 
                print(event) 
                await client.delete_messages(event.message.peer_id.user_id, event.message.id) 
                print('message deleted successfully') 
               else: 
                    print('failed') 
                    pass 
    client.add_event_handler(my_event_handler) 
    while True: 
        await event.wait() 
        event.clear() 
 
if name == '__main__': 
    asyncio.run(main())
