from difflib import get_close_matches
import json


def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches:
        return matches[0]


def get_response(message: str, knowledge: dict) -> str:
    # Finds the best match, otherwise returns None
    best_match: str | None = get_best_match(message, knowledge)

    # Gets the best match from the knowledge base
    if answer := knowledge.get(best_match):
        return answer
    else:
        return 'I don\'t understand... Could you try rephrasing that?'


def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)

# if __name__ == "__main__":
#     test_knowledge: dict = load_knowledge('knowledge.json')
#     test_response: str = get_response('hello', knowledge=test_knowledge)
#     print(test_response)
