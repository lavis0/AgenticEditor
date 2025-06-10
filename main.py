import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from system_prompt import system_prompt
from call_function import available_functions

def main():
    load_dotenv()
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt>")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = 'gemini-2.0-flash-001'

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Call the model
    generate_content(client, model, messages, verbose)

def generate_content(client, model, messages, verbose):
    # Create configuration
    config = types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    response = client.models.generate_content(model=model,
                                              contents=messages,
                                              config=config)
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}\n'
              f'Response tokens: {response.usage_metadata.candidates_token_count}')

    if response.function_calls:
        print('Function calls:')
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print('Response:')
        print(response.text)

if __name__ == "__main__":
    main()