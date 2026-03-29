from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    
    # First message 
    first_message = "Welcome to the COSMOS STARSHIP event!"
    await context.bot.send_message(chat_id=chat_id, text=first_message)

    # button Claim AirDrop
    claim_airdrop_button = InlineKeyboardButton("GO TO SPACE", web_app=WebAppInfo(url='https://wueme-byte.github.io/cosmos_2D_game/'))
    claim_airdrop_markup = InlineKeyboardMarkup([[claim_airdrop_button]])

    # Second message - text + link
    second_message = (
        "Learn more about our project:\n"
        "[Official site](https://anon.tg/)\n"
        
    )

    # Buttons to DEX's
    dedust_button = InlineKeyboardButton("DeDust.io", url='https://dedust.io/swap/TON/ANON')
    stonfi_button = InlineKeyboardButton("STON.Fi", url='https://app.ston.fi/swap?chartVisible=false&ft=TON&tt=ANON')
    second_message_markup = InlineKeyboardMarkup([[dedust_button, stonfi_button]])

    await context.bot.send_photo(chat_id=chat_id, photo='https://ibb.co/1fqvq1hg', caption=second_message, parse_mode=ParseMode.MARKDOWN, reply_markup=second_message_markup)



    # text and buttons with link
    caption = """Coin our exciting event - the Anon Box Airdrop! 
What's inside Anon Box?
- Valuable NFTs from our partners
- $ANON tokens and other cryptocurrencies
- Unique prizes and surprises

Date and Time:
The airdrop has already started! Stay updated to not miss your rewards.
Benefits:
- Exclusive rights and privileges for future ANON missions
- Monthly rewards for ANON Pass holders

Stay anonymous and get ready for new surprises with ANON!"""

    # buttons
    keyboard = [
        [InlineKeyboardButton("Official site", url='https://wueme-byte.github.io/cosmos_2D_game/')],
        [InlineKeyboardButton("PLAY", web_app=WebAppInfo(url='https://wueme-byte.github.io/cosmos_2D_game/'))],
    
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # GIF
    await context.bot.send_animation(chat_id=chat_id, animation='https://i.postimg.cc/DzVL3Vk0/ezgif-6-9954069cb7.gif', caption=caption, reply_markup=reply_markup)

# token
application = Application.builder().token("8387017891:AAEZmhCZ_eY7F2PmVDMCTYzLvSObgIQBr3c").build()
application.add_handler(CommandHandler("start", start))
application.run_polling()

