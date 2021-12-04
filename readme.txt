Shreya Kamath
Assignment 10.1- Read me file
Explaining demo code and the class, data variables and methods included


#Friend Class:
The class i've created is called Friend class. When starting this assignment, I was thinking of all the real world instances I can think portray. 
The Friend class accounts for as many friends and their inormation as the user creates. 
With the use of other methods, the class is used to compare and contrast information of the friend and, in this case, my information. 
This friend class allowed me to bring out my creativity and combine it with the methods and techniques i've learned in this quarter. It was quite fun!

#Data variables- The friend class i've created has three variables.
The first variable is name. This is pretty self explanatory. This allows us to identify the name of the Friend that is being talked about. 
The second variable is birth year. I included this as it is pretty basic information. I thought about having the full birthday rather than just year. However, if someone were to come up to me in real life and ask me for my name, birthday and something else, I most likely would not give them my real birthday. However, if someone asked me the year I was born in, I would be more likely to tell them. 
The third variable is height. This is also information that isn't too sensitive and people would probably truly answer. It's fun to know how tall your friends are! :)

#Methods:
The first method I implemented was to find the age of the friend. This simply takes the inputed birth year of the frined and subtracts it from 2021. This allows us to figure out how old the friend is. 
The second method I implemented was to compare height. The compare height function simply sees if the person is taller than 5 feet. If the person is taller than 5 feet, the method returns that they are taller than Shreya, me. If not, it returns that the person is shorter than me. Essentially, the height of the friend and my height are the ones being comapred. 

#Demo Program:
My demo program simply creates the Friend class with the variables of name, birth year and height. Then it does the normal work a class would have of intializing and making the varible private with the self argument. After that, it simply uses the get and set methods.
The get mehtods are used with each variable to just return the information inputted as the argument. The set method, on the other hand, is used to allow the entered argument to equal anything else. It in a way, is like a renaming. 
After the get and set methods, my demo program goes onto the other two additional methods which are find age and compare heihgt. The find age finds the age of the friend asked about by subtracting their given birth year from 2021- the current year. 
The next method is used to compare the height of the friend and myself. If the friend is taller than five feet, they are taller than me!

#Instructions of running the demo program
In order to run the demo program, the user needs to first create a variable that calles the class "Friend" and has a name, birth year and height as arguments- each argument separated by commas. The name and birth year arguments are strings while the height argument should be an integer with decimals. 
For example, if the friend that is being talked about if 6 feet and 4 inches, enter the information as 6.4. This will allow the function to properly calculate the height of the friend and give the expected output. 
After creating variables for as many frineds wanted, with the proper information, it's time to call the function! We will be using the normal print method. Inside the paranthesis, have the string of what the output should say as well as the correct name and information for the friend that is being asked about. 
In my demo code, each method- get and set for each variable, find age, and compare height- all have their outputs set. In order to call the function for the specific friend, simply go to the print line for the given function and change the name of the variable. 
For example, line 67 is the printing out for the get name function. Line 68 is printing out the get birth year function. Line 69 is printing out the get height function. Line 70 is printing out the find age function. Line 71 is printing out the compare height function. 
This is a brief explanation of my code and how it works! 
