from pprint import pprint
from common import client, model
import openai


class Chatbot:
    def __init__(self, api_key):
        self.context = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        self.client = openai.OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"

    def add_user_message(self, message):
        self.context.append({"role": "user", "content": message})

    def send_request(self):
        self.response = self.client.chat.completions.create(
            model=self.model,
            messages=self.context
        ).model_dump()

    def add_assistant_response(self):
        reply = self.response["choices"][0]["message"]
        self.context.append(reply)

    def get_last_response(self):
        content = self.response["choices"][0]["message"]["content"]
        print(content)
        return content

    def print_context(self):
        print("\n=== Current Chat Context ===")
        for i, message in enumerate(self.context):
            role = message["role"]
            content = message["content"]
            print(f"{i + 1:02d}. [{role.upper()}] {content}")
        print("============================\n")


if __name__ == "__main__":
    api_key = "-"
    bot = Chatbot(api_key)

    # 1차 질문
    bot.add_user_message("Who won the world series in 2020?")
    bot.send_request()
    bot.add_assistant_response()
    bot.get_last_response()
    bot.print_context()

    # 2차 질문
    bot.add_user_message("Where was it played?")
    bot.send_request()
    bot.add_assistant_response()
    bot.get_last_response()
    bot.print_context()