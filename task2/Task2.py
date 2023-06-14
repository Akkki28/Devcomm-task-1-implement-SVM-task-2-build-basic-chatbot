import openai
#generated API key 
openai.api_key = 'API_KEY'
def get_api_response(prompt: str) -> str | None:#creating a function that returns a string or none
    text: str | None = None
    #setting how the AI will behave using code provided at playgroung feature of openAI
    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,#randomness
            max_tokens=150,#maximum number of tokens that are to be generated
            top_p=1,#controls diversity
            frequency_penalty=0,#decreasing models capability to repeat topics
            presence_penalty=0.6,#increasing models capability to talk about new topics
            stop=[' You:', ' AI:']
        )

        choices: dict = response.get('choices')[0]#storing the response in a dictionary
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text

#creating a chat history by appending a list of strings with your and AI's messages
def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:#creating a function that returns a string
    p_message: str = f'\nYou: {message}'#assining  the formatted string to p_message
    update_list(p_message, pl)#updating the list pl with p_message
    prompt: str = ''.join(pl) # concentrating the elemnts of the list pl and assining it to prompt
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:#creating a function that returns a string
    prompt: str = create_prompt(message, pl)#assigning the prompt returned from create prompt to a variable prompt
    bot_response: str = get_api_response(prompt)

    if bot_response:#check is a response was generated 
        update_list(bot_response, pl)#updating list pl with the generated message
        pos: int = bot_response.find('\nAI: ')#assingning index of
        bot_response = bot_response[pos + 5:]#5 as we need the respose generated post '\nAI: '
    else:
        bot_response = 'error'

    return bot_response


def main():
    prompt_list: list[str] = ['',
                              '\nYou: What time is it?',
                              '\nAI: It is 6:30']#provinding training data for the bot

    while True:
        #taking input from the user 
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')


if __name__ == '__main__':

    main()


