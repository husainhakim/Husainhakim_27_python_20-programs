
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display_question(self):
        print(self.question)
        shuffled_options = self.options[:]
        (shuffled_options)
        idx = 1
        for option in shuffled_options:
            print(f"{idx}. {option}")
            idx += 1

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self):
        score = 0
        print(f"Welcome to the {self.name} quiz!")
        for question in self.questions:
            question.display_question()
            user_answer = int(input("Enter your choice (1, 2, 3, etc.): "))
            if question.check_answer(user_answer):
                score += 1
        print(f"Your score for the {self.name} quiz is: {score}/{len(self.questions)}")


class User:
    def __init__(self, name):
        self.name = name

easy_questions = [
    Question("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra"], 3),
    Question("How many continents are there?", ["5", "6", "7"], 3),
    Question("Which is the largest ocean?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"], 3)
]

medium_questions = [
    Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Husain hakim", "Virat kohli"], 1),
    Question("What is the powerhouse of the cell?", ["Mitochondria", "Medulla oblongata", "Inegration"], 1),
    Question("Which planet is known as the 'Red Planet'?", ["Mars", "Jupiter", "Venus"], 1)
]

hard_questions = [
    Question("What is the boiling point of water in Celsius?", ["100°C", "0°C", "50°C"], 1),
    Question("Which composer wrote the 'Moonlight Sonata'?", ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach"], 1),
    Question("Which year did World War II end?", ["1945", "1939", "1950"], 1)
]

very_hard_questions = [
    Question("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei"], 2),
    Question("What is the chemical symbol for gold?", ["Au", "Ag", "G"], 1),
    Question("Which element has the atomic number 26?", ["Iron", "Copper", "Nickel"], 1)
]

impossible_questions = [
    Question("What is the square root of 576?", ["24", "23", "25"], 1),
    Question("Who is the greatest of all time?", ["Cristiano", "Lionel messi", "Darwin nunez"], 3),
    Question("What is the largest prime number less than 100?", ["97", "99", "101"], 1)
]

easy_quiz = Quiz("Easy", easy_questions)
medium_quiz = Quiz("Medium", medium_questions)
hard_quiz = Quiz("Hard", hard_questions)
very_hard_quiz = Quiz("Very Hard", very_hard_questions)
impossible_quiz = Quiz("Impossible", impossible_questions)

print("Choose a quiz difficulty:")
print("1. Easy\n2. Medium\n3. Hard\n4. Very Hard\n5. Impossible")
choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    user_name = input("Enter your name: ")
    user = User(user_name)
    easy_quiz.take_quiz()
elif choice == 2:
    user_name = input("Enter your name:-")
    user = User(user_name)
    medium_quiz.take_quiz()
elif choice == 3:
    user_name = input("Enter your name:-")
    user = User(user_name)
    hard_quiz.take_quiz()
elif choice == 4:
    user_name = input("Enter your name:-")
    user = User(user_name)
    very_hard_quiz.take_quiz()
elif choice == 5:
    user_name = input("Enter your name:-")
    user = User(user_name)
    impossible_quiz.take_quiz()
else:
    print("Invalid choice! Please select a number between 1 and 5.")
