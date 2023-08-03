# holy-figures-ai-chat
Be able to chat with Holy Figures based on selected Holy Text, powered by ChatGPT's API.

### Features
- [x] Login with Clerk.com
- [x] Select Holy Text
- [x] Select Holy Figures
- [x] Chat with Holy Figures

## How to use
1. Clone this repository
2. Install the requirements: `pip install -r requirements.txt`
3. Set up MongoDB Atlas Free tier and create a database called `god_chat`
   1. You can set any name you want, but make sure you modify the `scripts/mongo_db.py` file.
   2. Collections used:
      1. `openai_responses`
      2. `questions`
      3. `users`
   3. Create a user in Atlas > Security > Database Access and add values in .env file.
4. Setup a Clerk.com free account and insert your publishable key to the `/static/vendors/clerk/script_SAMPLE.js` file and rename to `script.js`.
5. Create an OpenAI account and add your API key to the .env file.

### What is stored in MongoDB Atlas?
1. `openai_responses` - Stores the response object from OpenAI API, including the tokens used.
2. `questions` - Stores the questions asked, asking user, answer, date-time stamp.
3. `users` - Stores the user's Clerk.com ID, first name, last name, email, and questions remaining.