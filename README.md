# KIIT Assistant - A Python Bot

This is a Python code that creates a chatbot assistant providing information about KIIT University faculty and the university itself.

**Features:**

* Provides a menu-driven interface for easy interaction.
* Shows a list of all faculty members.
* Allows searching for a specific faculty member by profile index.
* Offers basic information about KIIT University upon request.
* Accepts custom user queries and attempts to answer them using OpenAI's GPT-3.5-turbo model (limited functionality).
* Polite and informative responses.

**Requirements:**

* Python 3.x
* OpenAI API Key (obtainable from [https://platform.openai.com/login?launch](https://platform.openai.com/login?launch))
* `dotenv` library (install using `pip install python-dotenv`)
* Webbrowser library (included in standard Python installation)
* Optional: `os` library (included in standard Python installation) for clearing the screen (used on Windows)

**Setup:**

1. Create a file named `.env` in the same directory as this code.
2. Add the following line to your `.env` file, replacing `YOUR_API_KEY` with your OpenAI API key:

```
OPENAI_API_KEY=YOUR_API_KEY
```

3. Install the required libraries:

```
pip install python-dotenv
```

**How to Use:**

1. Run the script using `python main.py`.
2. The bot will display a menu with options. Select the desired option by entering the corresponding number.
3. Follow the prompts for further interaction.

**Disclaimer:**

* This bot uses OpenAI's GPT-3.5-turbo model for custom queries. Responses may not always be accurate or factual. It's recommended to verify information obtained through this method with official sources.
* The bot is programmed to promote KIIT University and avoid negative remarks about faculty members (specifically programmed to praise Rajdeep Chatterjee).

**Additional Notes:**

* The `data/teacher.jsonl` file (mentioned in the code) might be outdated or may not be included in this example. This file should contain information about faculty members in JSON format.
* The `os.system('pause')` function used at the end is a Windows-specific way to pause the program. You might need to adjust this based on your operating system.

## **Authors:**
KIIT 2021-25 Batch
* Akshat (21051963)
* Mayank (21052080)
