import os
from openai import OpenAI
from dataclasses import dataclass


@dataclass(frozen=True)
class Model:
    basic: str = "gpt-4o-mini"
    advanced: str = "gpt-4o"


model = Model()
client = OpenAI(api_key="-", timeout=30, max_retries=1)