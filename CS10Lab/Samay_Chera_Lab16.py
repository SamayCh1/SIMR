from datetime import datetime

class Book:

    genres = {}
    

    def __init__(self: 'Book', genre: str, title: str, author: str, publication_year: int):
        """
        Initialize a Book object.

        Args:
            genre (str): The genre of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The publication year of the book.
	    
	    Examples:
	    >>> book1 = Book("Fiction", "Norwegian Wood", "Haruki Murakami", 1987)
	    >>> book1.genre == "Fiction"
	    True
	    >>> book1.title == "Norwegian Wood"
	    True
	    >>> book1.title = "Kafka on the Shore"
	    >>> book1.author.lower() == "haruki murakami"
	    True
	    >>> type(book1.publication_year) == int
	    True
	    >>> books = []
	    >>> for genre, title, author, publication_year in [\
                ["Manga", "Tomie", "Junji Ito", 2016], \
                ["Self-help", "Outliers", "Malcolm Gladwell", 2008], \
                ["Fiction", "1984", "George Orwell", 1961]]:
	    ... 	books.append(Book(genre, title, author, publication_year))
		>>> [x.genre for x in books] == ["Manga", "Self-help", "Fiction"]
		True
		>>> sum([y.publication_year for y in books]) == 5985
		True
		>>> [title.title for title in books] == ["Tomie", "Outliers", "1984"]
		True
		>>> books[1].author == "Malcolm Gladwell"
		True
        """
        self.genre = genre 
        self.title = title
        self.author = author
        self.publication_year = publication_year 


    def __str__(self: 'Book') -> str: 
        """
        Return the string representation of a Book object.
        Examples:
        >>> book1 = Book("Fiction", "Norwegian Wood", "Haruki Murakami", 1987)
        >>> print(book1)
        Book Title: Norwegian Wood | Genre: Fiction | Author: Haruki Murakami | Year: 1987
        """
        return f"Book Title: {self.title} | Genre: {self.genre} | Author: {self.author} | Year: {self.publication_year}"     


    def __repr__(self: 'Book') -> str:
        """
        Return a string representation that can be used to recreate the object.

        Returns:
            str: A string representation of the Book object.
        >>> dune = Book("Science Fiction", "Dune", "Frank Herbert", 1965)
        >>> dune
        Book('Science Fiction', 'Dune', 'Frank Herbert', 1965)
        """
        return f"Book('{self.genre}', '{self.title}', '{self.author}', {self.publication_year})" 
    

    def calculate_age(self: 'Book') -> int:
        """
        Calculate the age of the book by subtracting its publication year from the current year.

        Returns:
            int: The age of the book.
        >>> tokyo = Book("Mystery", "Tokyo Heist", "Diana Renn", 2013)
        >>> 10 <= tokyo.calculate_age() <= 15 #in 2023, tokyo.calculate_age() == 10
        True
        """
        return 2024 - self.publication_year


    def outdated(self: 'Book', old_age: int) -> int:
        """
        Determine if the book is outdated based on a specified age.

        Args:
            old_age (int): The maximum age threshold for considering the book outdated.

        Returns:
            bool: True if the book's age is greater than the specified old_age, False otherwise.
        >>> hunger_games = Book('Dystopian fiction', 'The Hunger Games', 'Suzanne Collins', 2008)
        >>> hunger_games.outdated(1)
        True
        >>> hunger_games.outdated(30)
        False
        >>> strange_book = Book('Science Fiction', 'Dune', 'Frank Herbert', 1965)
        >>> Book.outdated(strange_book, 45)
        True
        """
        return self.calculate_age() >= old_age  


    
    

    def add_to_genres(self: 'Book') -> None:
        """
        Add the book to the genres dictionary.

        If the book's genre isn't in the genres dictionary, add the genre and the book's information.
        Otherwise, make sure the book isn't already present in the genres dictionary before adding it.

        Returns:
            None
        >>> frankenstein = Book("Fiction", "Frankenstein", "Mary Shelley", 1818)
        >>> old_book = Book("Comic", "Calvin & Hobbes", "Bill Watterson", 1985)
        >>> strange_book = Book("Cooking", "How to Cook Water", "Yaxson Mang", 2016)
        >>> Book.add_to_genres(old_book)
        >>> Book.genres
        {'Comic': [['Calvin & Hobbes', 'Bill Watterson']]}
        >>> cooking_two = Book("Cooking", "Never Cook Slime", "Josh Hug", 2021)
        >>> Book.add_to_genres(frankenstein); Book.add_to_genres(strange_book); Book.add_to_genres(cooking_two)
        >>> Book.genres == {'Comic': [['Calvin & Hobbes', 'Bill Watterson']],
        ... 'Fiction': [['Frankenstein', 'Mary Shelley']], 
        ... 'Cooking': [['How to Cook Water', 'Yaxson Mang'], ["Never Cook Slime", "Josh Hug"]]}
        True
        """
        if self.genre in Book.genres.keys(): 
            Book.genres[self.genre].append([self.title, self.author]) 
        else:
            Book.genres.update({self.genre: [[self.title, self.author]]})


"""
The MooingBook class is optional.
Feel free to attempt this class if you want to learn about Python inheritance.
This concept will be covered in CS61A.
"""

# class MooingBook(Book):

#     def __repr__(self: 'MooingBook'):
#         """
#         Returns the string representation of a MooingBook object.
#         >>> sherlock = MooingBook("Mystery", "The Adventures of Sherlock Holmes", "Arthur Conan Doyle", 1892)
#         >>> print(sherlock) #string representation
#         Book Title: The Adventures of Sherlock Holmes | Genre: Mystery | Author: Arthur Conan Doyle | Year: 1892
#         >>> sherlock #overrided repr
#         MooingBook('Mystery', 'The Adventures of Sherlock Holmes', 'Arthur Conan Doyle', 1892)
#         """
#         pass

#     def moo(self: 'MooingBook'):
#         """
#         Produce a moo sound on behalf of the book's author.

#         Returns:
#             None
#         Examples:
#         >>> frankenstein = MooingBook("Fiction", "Frankenstein", "Mary Shelley", 1818)
#         >>> frankenstein.moo()
#         On behalf of Mary Shelley, I moo.
#         """
#         pass


"""-----------------------------------------------------------------------------------------"""

class TicTacToe:
    EMPTY = " "
    PLAYER_X = "X"
    PLAYER_O = "O"

    def __init__(self: 'TicTacToe'):
        """
        Initializes an empty Tic Tac Toe board.
        
        The board is represented as a 3x3 list of lists. Each cell in the board can be
        - EMPTY (" "), indicating the cell is unoccupied
        - PLAYER_X ("X"), indicating the cell is occupied by player X
        - PLAYER_O ("O"), indicating the cell is occupied by player O

        >>> game = TicTacToe()
        >>> game.board
        [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        """
        self.board = [[self.EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = self.PLAYER_X




    def __str__(self: 'TicTacToe') -> str:
        """
        Returns a string representation of the Tic Tac Toe board.
        
        Each cell in the board can be:
        - A space (" ") if it's unoccupied
        - "X" if it's occupied by player X
        - "O" if it's occupied by player O

        The rows are separated by lines of hyphens ("-----").
        """
        board_str = ""
        for row in self.board:
            row_str = " | ".join(cell for cell in row)
            board_str += row_str + "\n" + "-" * 5 + "\n"
        return board_str[:-6]


    def do_move(self: 'TicTacToe', x: int, y: int) -> bool:
        """
        Attempts to make a move on the board at the specified coordinates (x, y) for the current player.

        Parameters:
        - x (int): The row index (0-2) where the player wants to make a move.
        - y (int): The column index (0-2) where the player wants to make a move.

        Returns:
        - bool: True if the move is successfully made; False otherwise.

        >>> game = TicTacToe()
        >>> game.do_move(1, 1)  # center cell, should be successful for player X
        True
        >>> game.board[1][1]
        'X'
        >>> game.current_player = game.PLAYER_O
        >>> game.do_move(1, 1)  # center cell again, should fail since it's occupied
        False
        >>> game.do_move(3, 1)  # invalid coordinates, outside of the board
        False
        >>> game.do_move(0, 0)
        True
        >>> game.board[0][0]
        'O'
        """
        #FIXME: This code is buggy and does not pass the doctests.
        #HINT: First, implement the method TicTacToe.is_valid_move
        
        if self.is_valid_move(x, y) == True:
            self.board[x][y] = self.current_player
            return True
        else:
            return False


    def is_valid_move(self: 'TicTacToe', x: int, y: int) -> bool:
        """
        Checks if a move at the specified coordinates (x, y) is valid.

        Parameters:
        - x (int): The row index (0-2) where the player wants to check validity.
        - y (int): The column index (0-2) where the player wants to check validity.

        Returns:
        - bool: True if the move is valid (i.e., within the board bounds and the cell is unoccupied); False otherwise.

        >>> game = TicTacToe()
        >>> game.is_valid_move(1, 1)  # center cell, should be valid as it's unoccupied
        True
        >>> game.do_move(1, 1)  # occupy the center cell with player X
        True
        >>> game.is_valid_move(1, 1)  # center cell, should be invalid as it's now occupied
        False
        >>> game.is_valid_move(3, 1)  # invalid coordinates, outside of the board bounds
        False
        >>> game.is_valid_move(-1, 1)  # invalid coordinates, outside of the board bounds
        False
        """
        if 2 >= x >= 0 and 2 >= y >= 0: 
            if self.board[x][y] == self.EMPTY:
                return True
            else:
                return False
        else:
            return False

    def generate_moves(self: 'TicTacToe') -> list:
        """
        Generates a list of all valid moves available on the board.
        
        A valid move is represented by a tuple of coordinates (x, y) where the cell is unoccupied.

        Returns:
        - list of tuple: A list containing tuples representing the coordinates of valid moves.

        >>> game = TicTacToe()
        >>> sorted(game.generate_moves())  # Initially, all cells are unoccupied, so all moves are valid
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        >>> game.do_move(1, 1)  # occupy the center cell with player X
        True
        >>> sorted(game.generate_moves())  # Now, the center cell (1, 1) should be excluded from the list
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
        """
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.EMPTY:
                    moves.append((i, j))
        return moves


    def check_win(self: 'TicTacToe', player: str) -> bool:
        """
        Determines if the specified player has won the game.

        Parameters:
        - player (str): The player symbol ("X" or "O") to check for a win.

        Returns:
        - bool: True if the player has won, False otherwise.

        >>> game = TicTacToe()
        >>> game.check_win("X")  # Initially, no one has won
        False
        >>> game.do_move(0, 0)
        True
        >>> game.do_move(0, 1)
        True
        >>> game.do_move(0, 2)  # Player X occupies the top row
        True
        >>> game.check_win("X")
        True
        >>> game.check_win("O")  # Player O has not won yet
        False
        """
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # Rows
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # Columns
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]  # Diagonals
        ]
        for condition in win_conditions:
            win = True
            for x, y in condition:
                if self.board[x][y] != player:
                    win = False
                    break
            if win:
                return True
        return False


    def check_game_over(self) -> tuple:
        """
        Determines the status of the game.

        Parameters:
        - current_player (str): The player symbol ("X" or "O") for the current player.

        Returns:
        - tuple: A tuple (bool, str) where the bool indicates if the game is over and the str indicates the result 
                ("win", "lose", "tie", "ongoing").

        >>> game = TicTacToe()
        >>> game.check_game_over()  # Initially, the game is ongoing
        (False, 'ongoing')
        >>> game.current_player = "X"
        >>> [game.do_move(0, i) for i in range(3)] and game.check_game_over()
        (True, 'Player X wins!')
        >>> game = TicTacToe()
        >>> game.current_player = "O"
        >>> [game.do_move(0, i) for i in range(3)] and game.check_game_over()
        (True, 'Player O wins!')
        >>> game = TicTacToe()
        >>> game.board = [["O", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        >>> game.check_game_over()
        (True, "It's a tie!")
        """
        if self.check_win(self.PLAYER_X): #FIXME: Fill in the ellipses
            return True, "Player X wins!"
        elif self.check_win(self.PLAYER_O): #FIXME: Fill in the ellipses
            return True, "Player O wins!"
        elif not self.generate_moves():
            return True, "It's a tie!"
        return False, 'ongoing'


    def switch_player(self) -> None:
        """
        Switches to the opposite player.
        
        Parameters:
        - current_player (str): The player symbol ("X" or "O") of the current player.
        
        Returns:
            None

        >>> game = TicTacToe()
        >>> game.switch_player()  # If the current player is X, the opposite player is O
        >>> game.current_player
        'O'
        >>> game.switch_player()  # If the current player is O, the opposite player is X
        >>> game.current_player
        'X'
        """
        self.current_player = self.PLAYER_O if self.current_player == self.PLAYER_X else self.PLAYER_X


def play_game():
    """
    Play a game of TicTacToe!
    This is an example of what a final project may look like if you decide to use Python
    as your programming language.

    To make the play_game function work, please complete the TicTacToe Class.

    TODO Complete the following methods in the class TicTacToe:
    - TicTacToe.do_move
    - TicTacToe.is_valid_move
    - TicTacToe.check_game_over
    """
    game = TicTacToe()

    while True:
        print(game)
        print(f"It's {game.current_player}'s turn. Enter row and column (0-2) separated by space: ", end="")
        x, y = map(int, input().split())
        
        if game.do_move(x, y):
            game_over, message = game.check_game_over()
            if game_over:
                print(game)
                print(message)
                break
            game.switch_player()
        else:
            print("Invalid move. Try again.")
