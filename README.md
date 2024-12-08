## Tetris game in Python using PyGame library 🐍

[![](https://img.shields.io/badge/github(pygame)-blueviolet?style=for-the-badge)](https://github.com/pygame)
[![](https://img.shields.io/badge/book(pygame)-green?style=for-the-badge)](https://pygame-docs.website.yandexcloud.net/tut/PygameIntro.html)


$\normalsize{\textsf{\color{violet}I took the Future Code course on "Practical applications of Python in engineering and science activities" 2023-2024.}}$


> [!NOTE]
> The game "Tetris" was created by Soviet engineer Alexei Pazhitnov in 1984. He came up with this game while working on pattern recognition algorithms at the USSR Academy of Sciences. "Tetris" quickly became popular in the USSR and then conquered the world, becoming one of the best-selling video games in history.

🎮 The game "Tetris" is a well-known arcade video game in which the player controls falling geometric pieces called "tetrominoes", which are made up of four squares.

📝 The rules are simple:
The pieces fall from above, and the player can rotate them and move them left-right (using the keys). Lines filled with blocks disappear and the player gets points (+100). The game ends when the blocks reach the top of the playing field.

<img src="https://i.ibb.co/vqNHvJY/2024-11-03-035445-1.png" width="700" height="500">

## Instructions on how to connect to the Tetris game

| Download the repository |

* In the repository you selected, click the green 'Code' button and copy the URL.
* Then, in Visual Studio Code (or other code editor), open a terminal and type the command:
  
```python
  git clone [repository address]
```

| Create a virtual environment |

* Open a terminal (or command line) and navigate to the project directory.
* Create a virtual environment using the command:
  
```python
  python -m venv env (replace 'env' with the desired environment name)
```

* Activate the virtual environment in Windows: `env\Scripts\activate`
* Or activate the virtual environment in macOS/Linux: `source env/bin/activate`
  
| Install dependencies |

* After activating the virtual environment, install the required libraries from the `requirements.txt` file
 
```python
  pip install -r requirements.txt
```

| Start the game |

* Navigate to the directory containing the file (usually the root directory of the project) `main.py`
* Start the game using the command:
  
```python
  python main.py
```

| Additional Notes |
  
* Make sure you have the appropriate version of Python installed, as specified in `requirements.txt`
* And have all the necessary libraries `pip install pygame` installed
  
  (If you are using a different IDE or editor, you may need to configure the environment so that it can find the virtual environment and installed libraries)
