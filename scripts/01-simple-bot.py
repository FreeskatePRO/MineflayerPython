from javascript import require, On, Once, AsyncTask, once, off

# Import the javascript libraries
mineflayer = require("mineflayer")

# Create bot with basic parameters
bot = mineflayer.createBot(
    {"username": "bot megölése=BANN!", "host": "localhost", "port": 27956, "version": "1.21.4", "hideErrors": False}
)

# Login event required for bot
@On(bot, "login")
def login(this):
    pass
