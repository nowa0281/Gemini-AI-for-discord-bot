
import discord
from discord.ext import commands 
import google.generativeai as genai
import asyncio
import os 

intents = discord.Intents.default()
intents = True
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
   await client.change_presence(
    status=discord.Status.online,
   
    )
print(f"Logged in as {client.user.name} ({client.user.id})")
print("The bot is now ready to use")
print("----------------------------")







# gemini ai chat-bot
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

 # Model and chat session configuration (adjust parameters as needed)
generation_config = {
     "temperature": 1,  # Controls randomness (higher = more creative, less coherent)
     "top_p": 0.95,  # Probability weighting for likely continuations
     "top_k": 64,  # Maximum number of vocabulary tokens to consider
     "max_output_tokens": 8192,  # Maximum number of tokens in the response
     "response_mime_type": "text/plain",
 }
safety_settings = [
     {
         "category": "HARM_CATEGORY_HARASSMENT",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
     {
         "category": "HARM_CATEGORY_HATE_SPEECH",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
     {
         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
     {
         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
 ]

model = genai.GenerativeModel(
     model_name="gemini-1.5-flash",
     safety_settings=safety_settings,
     generation_config=generation_config,
 )

chat_session = model.start_chat(history=[])




@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself



    if message.content.startswith("!ask"):
        # Extract user input
        user_input = message.content[len("!ask"):].strip()

        # Generate Gemini AI response
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)

        member = message.author

        # max response to 2000 characters
        fragment_response = response.text[:1800]

        # Send the first fragment (first 2000 characters)
        await message.channel.send(f"{member.mention}  {fragment_response}")

        # Add a delay (1-2 seconds) to avoid rate limits
        await asyncio.sleep(1)

        # If the full response exceeds 2000 characters, send the remaining fragment
        if len(response.text) > 1800:
            remaining_fragment = response.text[2000:]
            await message.channel.send(remaining_fragment)

    print(message)

client.run(discord_token)
