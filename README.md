# DSPT12 Unit 3 - Sprint 1 Review

_Don't forget to create documentation for classes and methods!_

## Premise

You joined the startup FIRESTORM&trade; which aims to develop the next MMO.  Your task now is to help develop the character models.

## Coding: Part I - Classes

1. Make a file `review.py` which will contain all the code for the classes we are about to make.

2. In `review.py` create a class called BaseCharacter which takes one argument `name`.

    - In the constructor, use reflection to instantiate the `name` attribute and add the following fields:
        - intel = 3 (intellect)
        - stam = 3 (stamina)
        - strn = 3 (strength)
        - agi = 3 (agility)
        - level = 1 (starting level)

3. Add a method in the BaseCharacter class called `level_up` which will level up a character by a factor of `increment` which will represent an integer greather than or equal to 1.  Keep the default value of `increment` to 1.

    - Within the method, add a clause which will raise an `Exception` error message stating `'Parameter "increment" must be an integer greater than or equal to 1.'`

    - Create a variable called `stat_increase` which will be equal to `3 * increment`.  This will be how much each stat (besides level) will increase each time the character levels up.

    - Create a for loop that will iterate through the class attributes and increment the main stats `intel, stam, strn` and `agi` by `stat_increase` and the `level` by the value of `increment`.  This can be accomplished using a built-in Python function, and a dunder (__) method in the class object but, if this is too challenging, feel free to code out each attribute and increment them as mentioned in the previous statement.

    - Once that is done, print (don't return) a block of text (or multiple print statements) stating the following:

        - The name of the character and the level that they reached

        - Each stat has increased by `stat_increase` to whatever it is after leveling up

        - *_Be creative with this part!_*

4. Create another Python class representing a character type (like: Mage, Warrior, Thief) which will inherit from the BaseCharacter class.

    - In the constructor, instantiate the inherited attributes using the `super()` method or by referencing the parent class and `name` parameter.

    - In addition, increment other primary stats that would fit to the background of the character type (i.e. Mages would probably receive more intellect and stamina at creation than Warriors).

    - Lastly, create two new fields/attributes `health` and another of your choice which serves as that character's ability resource (i.e. Mages would use `mana`).

        - In some MMOs, health - and sometimes the ability resource - have a base amount that is modified by a primary stat like stamina.  Reflect this in your code!

5. Finally, create a method inside the new class called `display_stats` which only takes itself as the arguement.

    - This method should _print_ out three statements displaying the character's:
        
        - Name
        
        - Total amount of health

        - Total amount of character ability resource

## Coding: Part II - Testing

1. First thing is first!  We need to install the `pytest` package.

   - While in your environment, run `pip install pytest` to accomplish this.

2. Now, create a directory called `tests` which will reside on the same level as `review.py`.

   - In the `tests` directory, create a file called `conftest.py` which will house our `pytest` fixtures.
   
   - To read more about `pytest` fixtures, check out [this link](https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session).
   
3. In `conftest.py` import both the `pytest` package as well as your `BaseCharacter` and second character class - this can be done with a [relative import](https://realpython.com/absolute-vs-relative-python-imports/)

   - Instantiate a fixture for `BaseCharacter` with the name `'Template'`
   
   - Instantiate a second fixture for your other character class using any name you would like!
   
   - Now that we have made our pytest fixtures, let's make some tests!
   
4. Create a new file called `test_<something>.py` replacing the carats and content with something relevant to what you are testing.

   - Create at least **four** different tests total which will test both class attributes and methods you made in your source code.
   
5. When you are done, test it out!

   - Open a command line terminal and make sure you are at the base level of your repository.
   
   - Run the command `pytest` and your four tests should run.
   
   - If you receive any errors, change the code around to fix it up and try again!
   
## Congratulations!

That's all here - good luck on your Sprint Challenge!
