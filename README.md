# Gemini-AI-for-discord-bot
Gemini ai chat bot for discord bot (chat bot)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini AI Chatbot Discord Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            font-size: 2em;
        }
        h2 {
            font-size: 1.5em;
        }
        ul {
            list-style: disc;
            padding-left: 20px;
        }
        code {
            font-family: monospace;
            background-color: #f0f0f0;
            padding: 5px;
        }
    </style>
</head>
<body>
    <h1>Gemini AI Chatbot Discord Bot</h1>

    <p>This Discord bot utilizes the powerful Gemini AI generative language model from Google AI to provide informative and creative responses to user queries.</p>

    <h2>Features</h2>
    <ul>
        <li>Leverages the power of Gemini AI for intelligent conversation.</li>
        <li>Responds to user prompts initiated with the `!ask` command.</li>
        <li>Enforces safety settings to maintain a positive and respectful environment.</li>
        <li>Splits lengthy responses into fragments for better readability within Discord's message character limit.</li>
    </ul>

    <h2>Installation</h2>

    <p>Here are the prerequisites and steps to install the bot:</p>

    <h3>Prerequisites</h3>
    <ul>
        <li><a href="https://www.python.org/downloads/">Python 3.6 or later</a></li>
        <li><a href="https://discord.com/developers/applications">Discord account and developer portal access</a></li>
        <li>Gemini AI API key (instructions on how to obtain it will be provided later)</li>
    </ul>

    <h3>Steps</h3>
    <ol>
        <li>Clone or download the repository.</li>
        <li>Install dependencies using pip:</li>
        <pre><code>pip install discord google-generativeai</code></pre>
        <li>(Optional, recommended) Create a `.env` file to store your Discord bot token securely. Add a line like `DISCORD_TOKEN=your_bot_token_here`.</li>
        <li>Configure your environment by setting the `GEMINI_API_KEY` environment variable to your Gemini AI API key.</li>
    </ol>

    <h2>Running the Bot</h2>

    <p>Here's how to start the bot:</p>

    <ol>
        <li>Replace `your_bot_token_here` in `client.run(discord_token)` with your actual Discord bot token.</li>
        <li>(Optional) Start the bot using the `.env` file:</li>
        <pre><code>python main.py</code></pre>
        <li>(Without `.env` file) Start the bot by setting the `DISCORD_TOKEN` environment variable and then running:</li>
        <pre><code>export DISCORD_TOKEN=your_bot_token_here  # Set environment variable
python main.py</code></pre>
    </ol>

    <p>**Instructions on obtaining a Gemini AI API key will be provided here.**</p>
</body>
</html>

