import openai


class ChatBot:
    def __init__(self):
        # openai.api_key = "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"
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke on a birds.")
    print(response)