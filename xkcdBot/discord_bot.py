"""A simple discord.py program to post xkcd comics."""

# Logging configuration. Go to DEBUG level if you want much more detail
import logging

from settings import *

logging.basicConfig(level=logging.INFO)

import discord, asyncio
from xkcd import random_comic_message


# Create a subclass of Client that defines our own event handlers
# Another option is just to write functions decorated with @client.async_event
class MyClient(discord.Client):
    @asyncio.coroutine
    def on_ready(self):
        """Asynchronous event handler for when we are fully ready to interact with the server."""
        print('Logged in %s %s' % (self.user.name, self.user.id))

        # Store a couple of destinations for messages
        global random_channel
        # kristjan = None
        random_channel = None

        # Enumerate the channels. This works over all servers the user is participating in
        print('Channels')
        for channel in self.get_all_channels():
            print(' ', channel.server, channel.name, channel.type)
            if channel.name == "random":
                # Store away the #games channel object for later use
                random_channel = channel

        # # Enumerate the members for every serv
        # print('Members')
        # for member in self.get_all_members():
        #     print(' ', member.name, member.status)
        #     if member.name == "Kristjan":
        #         kristjan = member

        # Send a message to a destination
        if random_channel is not None:
            while True:
                yield from self.send_message(random_channel, random_comic_message())
                yield from asyncio.sleep(14400)  # posts after every 2 hours

    @asyncio.coroutine
    def on_message(self, message):
        """Asynchronous event handler that's called every time a message is seen by the user."""
        print('Message received\n ', message.content)
        if "*xkcd" in message.content and "random" == message.channel.name and info != message.content:
            yield from self.send_message(random_channel,
                                         random_comic_message() + "\n `BOT called by {}`".format(message.author))
        if "info" in message.content.lower() and self.user in message.mentions and "random" == message.channel.name:
            yield from self.send_message(random_channel, info)

# Run the client, a blocking call that logs in and runs the event loop. Exits on Ctrl-C
client = MyClient()
client.run(email, password)
