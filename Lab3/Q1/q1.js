// Define quiz questions and options
const quizQuestions = [
    {
        question: "What is the capital of France?",
        options: ["Berlin", "Madrid", "Paris", "Lisbon"],
        correctAnswer: 2
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Earth", "Mars", "Jupiter", "Saturn"],
        correctAnswer: 1
    },
    {
        question: "Who wrote 'Hamlet'?",
        options: ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        correctAnswer: 0
    },
    {
        question: "What is the largest ocean on Earth?",
        options: ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        correctAnswer: 3
    }
];

// Function to display the quiz questions
function displayQuiz() {
    const quizContainer = document.getElementById("quiz");
    quizContainer.innerHTML = "";

    quizQuestions.forEach((question, index) => {
        const questionElement = document.createElement("div");
        questionElement.classList.add("question");

        const questionTitle = document.createElement("h3");
        questionTitle.textContent = `${index + 1}. ${question.question}`;
        questionElement.appendChild(questionTitle);

        const answersContainer = document.createElement("div");
        answersContainer.classList.add("answers");

        question.options.forEach((option, optionIndex) => {
            const label = document.createElement("label");
            const input = document.createElement("input");
            input.type = "radio";
            input.name = `question${index}`;
            input.value = optionIndex;
            label.appendChild(input);
            label.appendChild(document.createTextNode(option));
            answersContainer.appendChild(label);
        });

        questionElement.appendChild(answersContainer);
        quizContainer.appendChild(questionElement);
    });
}

// Function to calculate the score
function calculateScore() {
    let score = 0;

    quizQuestions.forEach((question, index) => {
        const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
        if (selectedOption && parseInt(selectedOption.value) === question.correctAnswer) {
            score++;
        }
    });

    const resultElement = document.getElementById("result");
    resultElement.textContent = `You scored ${score} out of ${quizQuestions.length}`;
    resultElement.style.display = "block";
}

// Initialize the quiz
displayQuiz();

// Add event listener to the submit button
document.getElementById("submit-btn").addEventListener("click", calculateScore);
