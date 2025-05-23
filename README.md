# 🎮 Python Hangman

Hangman is a word-guessing game where the player tries to figure out a hidden word by suggesting letters.

## 🧠 How it works

At the start, the player sees the word with all its letters replaced by underscores (_), so they only know how many letters are in the word.
In each round, the player guesses a letter: 


✅If the guessed letter is in the word, its position (or positions, if the letter is in multiple parts of the word) is revealed. 

❌ If the letter is not in the word, a mistake is counted.

🏆 The player wins when they correctly guess all the letters of the word.

Besides that, the player has a total of **6 chances** to guess the word before being "hanged". 
If the player makes six mistakes without guessing the word, they lose 👻!


## 🛠️ Technologies Used

- `Python`
- [`wonderwords`](https://pypi.org/project/wonderwords/) – for random word generation
- ANSI escape codes – for colorful terminal formatting

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/valgonz011/Python_Hangman.git
   cd Python_Hangman
3. Install dependencies:
   pip install -r requirements.txt
4. Run the game:
   python hangman.py


## 👩‍💻 Author
Created by [Valeria González](https://www.linkedin.com/in/valeria-gonzalez-vargas/)

Based in Berlin | BI & Data Analyst | Always learning 📚.
