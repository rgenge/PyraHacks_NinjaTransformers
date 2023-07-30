class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the capital of France?\n(a) Paris\n(b) London\n(c) Berlin\n\n",
    "What is the capital of the United States?\n(a) New York\n(b) Washington D.C.\n(c) Los Angeles\n\n",
    "What is the capital of Canada?\n(a) Toronto\n(b) Ottawa\n(c) Vancouver\n\n",
    "What is the capital of Mexico?\n(a) Mexico City\n(b) Guadalajara\n(c) Cancun\n\n",
    "What is the capital of Brazil?\n(a) Rio de Janeiro\n(b) Sao Paulo\n(c) Brasilia\n\n",
    "What is the capital of Argentina?\n(a) Buenos Aires\n(b) Cordoba\n(c) Rosario\n\n",
    "What is the capital of Chile?\n(a) Santiago\n(b) Valparaiso\n(c) Vina del Mar\n\n",
    "What is the capital of Peru?\n(a) Lima\n(b) Cusco\n(c) Arequipa\n\n",
    "What is the capital of Colombia?\n(a) Bogota\n(b) Medellin\n(c) Cali\n\n",
    "What is the capital of Venezuela?\n(a) Caracas\n(b) Maracaibo\n(c) Valencia\n\n",
    "What is the capital of Ecuador?\n(a) Quito\n(b) Guayaquil\n(c) Cuenca\n\n",
    "What is the capital of Bolivia?\n(a) La Paz\n(b) Sucre\n(c) Cochabamba\n\n",
    "What is the capital of Paraguay?\n(a) Asuncion\n(b) Ciudad del Este\n(c) Encarnacion\n\n",
    "What is the capital of Uruguay?\n(a) Montevideo\n(b) Punta del Este\n(c) Colonia\n\n",
    "What is the capital of Guyana?\n(a) Georgetown\n(b) Linden\n(c) New Amsterdam\n\n",
    "What is the capital of Suriname?\n(a) Paramaribo\n(b) Nieuw Nickerie\n(c) Lelydorp\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "a"),
    Question(question_prompts[12], "a"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "a"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print(f"{score}/{len(questions)}")
    print(f"You got {score}/{len(questions)} correct!")

run_quiz(questions)
