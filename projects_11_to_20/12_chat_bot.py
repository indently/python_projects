from difflib import get_close_matches


def get_best_match(user_question: str, questions: list[str]) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches:
        return matches[0]


def get_answer(question: str, knowledge_base: dict) -> str | None:
    """Loops through the knowledge base and returns an appropriate response"""

    for q in knowledge_base:
        # If there is a match, return the answer from that question
        if q == question:
            return knowledge_base[q]


def chatbot(knowledge: dict):
    """Chatbot"""

    while True:
        user_input: str = input('You: ')

        # Finds the best match, otherwise returns None
        best_match: str | None = get_best_match(user_input, [q for q in knowledge])

        if answer := get_answer(best_match, knowledge):
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand... Could you try rephrasing that?')


if __name__ == "__main__":
    brain: dict = {'hello': 'Hey there!',
                   'how are you?': 'I am good, thanks!',
                   'do you know what the time is?': 'Not at all!',
                   'what time is it?': 'No clue!',
                   'what can you do?': 'I can answer questions!',
                   'ok': 'Great.'}

    chatbot(knowledge=brain)
