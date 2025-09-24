import random
import asyncio

# Magic 8 Ball

# Allow the user to enter their question.
# Display an in progress message(i.e. "thinking").
# Create 20 responses, and show a random response.
# Allow the user to ask another question or quit.

answers = ["Yes, definitely.",
           "Without a doubt.",
           "You may rely on it.",
           "Signs point to yes.",
           "It is certain.",
           "Outlook good.",
           "Most likely.",
           "Yes.",
           "As I see it, yes.",
           "Very doubtful.",
           "My reply is no.",
           "Outlook not so good.",
           "Don’t count on it.",
           "My sources say no.",
           "Reply hazy, try again.",
           "Ask again later.",
           "Cannot predict now.",
           "Better not tell you now.",
           "Concentrate and ask again.",
           "Maybe."]

print("Welcome to the magic 8-ball.")
while True:
    question = input(
        f'\nType your question and press enter to shake the ball.\nTo quit, type "quit"\n\n')
    if question == "quit":
        break
    async def thinking():
        print("Thinking...")
        await asyncio.sleep(2)
    asyncio.run(thinking())
    print(random.choice(answers))