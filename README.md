

# README

## Metadata
Project Name: Monte Carlo Simulator

## Synopsis

This program provides a Monte Carlo Simulator to simulate various games of chance. The simulation is based on the rolling of dice. Each die object has N sides and W weights, and can be rolled to select a face. W defaults to 1.0 for each face but can be changed after the object is created. The program provides three classes: Die, Game, and Analyzer. The Die class represents the die object and provides a few methods to change weights, roll the die, and display the weights of the sides. The Game class represents the game object and provides methods to play the game and display the results. The Analyzer class allows for summary calculations to be performed regarding the results. 

The classes can be used as follows:

```python
# Creating dice
d1 = Die([1, 2, 3, 4, 5, 6]) # a regular 6-sided die
d2 = Die(['heads', 'tails'], [0.4, 0.6]) # a biased coin

# Changing weight of a side of the die
d1.change_weight(2, 1.5)

# Rolling a die
outcome = d1.roll_die()

# Creating a game
g = Game([d1, d2])

# Playing a game
g.play(100)

# Displaying the results
g.show_results()
```

## Installing

To use the program, you need to have Python 3.6 or later installed on your computer.

To install the required packages, run the following command in your terminal:

```
pip install pandas
```

Then, you can download the `montecarlo.py` file and import it in your Python script using the following line:

```
from montecarlo import Die, Game, Analyzder
```

## API Description

### Die Class

#### Class Description

Represents a die object that can be rolled to select a face.

#### Class Definition

```python
class Die:
```

#### Class Methods

##### `__init__(self, faces: List[Union[str, int]]) -> None`

Class constructor that initializes the die with an array of faces and sets the weight of each face to 1.0.

- **Parameters:**
    - `faces` (List[Union[str, int]]): An array of faces for the die. The data type (type) may be strings or numbers.

##### `change_weight(self, face: Union[str, int], new_weight: Union[str, float]) -> None`

Method to change the weight of a single face of the die.

- **Parameters:**
    - `face` (Union[str, int]): The face value to be changed.
    - `new_weight` (Union[str, float]): The new weight of the face.

##### `roll_die(self, times: int = 1) -> List[Union[str, int]]`

Method to roll the die one or more times and return the outcomes.

- **Parameters:**
    - `times` (int, optional): The number of times the die is to be rolled. Defaults to 1.

- **Returns:**
    - `outcomes` (List[Union[str, int]]): A list of outcomes from rolling the die.

##### `__str__(self) -> str`

Method to return a string representation of the die object, including the current set of faces and weights.

- **Returns:**
    - `str(self.__thedie)` (str): A string representation of the die object.

#### Class Attributes

##### `faces`

An array of faces for the die.

##### `__thedie`

A private DataFrame that stores the faces and weights of the die.

### Game Class

# Readme for the Game Class

The `Game` class is a Python class that simulates the rolling of one or more dice of the same kind one or more times. It is designed to be flexible and customizable, with the ability to define dice with different weights.

## Initialization

To create a new instance of the `Game` class, you need to provide a list of already instantiated `Die` objects that have the same number of sides and associated faces. The `Die` class is not defined in this code snippet, but it is assumed to be defined elsewhere.

```python
dice = [Die(6), Die(6)]
game = Game(dice)
```

In this example, we are creating a new game with two six-sided dice.

## Playing the Game

To play the game, you can call the `play` method of the `Game` object and provide the number of times the dice should be rolled.

```python
game.play(10)
```

This will roll the dice 10 times and save the results to a private dataframe of shape `N` rolls by `M` dice, where `N` is the number of rolls and `M` is the number of dice in the game.

## Viewing the Results

To view the results of the most recent play, you can call the `show_results` method of the `Game` object. By default, this method returns the results in wide format, with a single column index with the roll number, and each die number as a column.

```python
game.show_results()
```

This will return a Pandas dataframe with the results of the most recent play.

If you prefer a narrow format, where the index has two columns with the roll number and the die number, and a column for the face rolled, you can pass the `form` parameter with the value "narrow".

```python
game.show_results(form='narrow')
```

This will return a Pandas dataframe with the results of the most recent play in a narrow format.

If you pass an invalid option to the `form` parameter, the method will raise a `ValueError` with a message indicating that you need to specify either "wide" or "narrow".


### Analyzer

The `Analyzer` class is used to compute various descriptive statistical properties of a game. The class takes a `Game` object as its input parameter and computes various attributes and methods to provide statistical analysis of the game.

#### Initialization

The `Analyzer` object is initialized with a `Game` object as its input parameter. At initialization time, it infers the data type of the die faces used in the game.

#### Attributes

- `jackpot_results`: A DataFrame that stores the results of the `jackpot` method. It contains a named index of the roll number and a column indicating whether the roll resulted in all faces being identical.
- `combo_results`: A DataFrame that stores the results of the `combo` method. It contains a multi-columned index of the distinct combinations of faces rolled, along with their counts.
- `facecount_results`: A DataFrame that stores the results of the `face_count` method. It contains an index of the roll number and face values as columns (in wide format).

#### Methods

- `jackpot()`: A method that computes how many times the game resulted in all faces being identical. It returns an integer for the number of times, and stores the results in the `jackpot_results` attribute.
- `combo()`: A method that computes the distinct combinations of faces rolled, along with their counts. It returns a DataFrame of the results and stores it in the `combo_results` attribute.
- `face_count()`: A method that computes how many times a given face is rolled in each event. It returns a DataFrame of the results in wide format and stores it in the `facecount_results` attribute.

Note: The methods of the `Analyzer` class assume that the `Game` object has a `show_results()` method that returns a DataFrame of the results of the game.

## Manifest

D .
__init__.py
all_tests.py
all_unit_test_results.txt
__init__.py
montecarlo.py
FinalProiectSubmissionTemplat….
LICENSE
README.md
setup.py
