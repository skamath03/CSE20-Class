#Shreya Kamath
#Assignment 10.1- Create your own class
#Practicing creating and working with class
#Create at least 1 class variable, 2 data variables, 2 get-set method, and 2 other methods
#Acknowledgments- Got help from TA in office hours, https://www.w3schools.com/java/java_encapsulation.asp, 

#creating the class named Friend
class Friend():
    #arguments are name, birth year, and height
    def __init__(self, name, birth_year, height):
        #creating variable to include arguments
        #initializing private variables
        self.name= name
        self.birth_year= birth_year
        self.height= height

    #get name function returns the name entered in the argument
    def get_name(self):
        return self.name

    #get birth year function returns the birth year entered in the argument
    def get_birth_year(self):
        return self.birth_year

    #get height funciton returns the height entered in the argument
    def get_height(self):
        return self.height
    
    #set name function allows name argument to be equal to anything
    def set_name(self, name):
        self.name= name

    #set birthday function allows birth year argument to be equal to anything
    def set_birthday(self, birth_year):
        self.birth_year = birth_year

    #set height function allows height argument to be equal to anything
    def set_height(self, height):
        self.height = height
    
    #find age function has argument birth year
    def find_age(self, birth_year):
        #to find age, subtract argument birth year from 2021
        year= 2021- int(birth_year)
        #returns calculated number in int form
        return year
    
    #compare heihgt function has argument name and height
    def compare_height(self, name, height):
        #Converting given height argument to integer form
        height= int(height)
        #if height is above 5
        if height >5:
            #print friend is taller than Shreya
            return("Friend, " + name + ", is taller than Shreya")
        else:
            #if not, return friend is shorter than Shreya
            return("Friend, " + name + ", is shorter than Shreya")
    

# main function where you list all functions
def main():
    Friend1= Friend("Bob", "1994", 5.10)
    Friend2= Friend("Sam", "2013", 4.11)
    Friend3= Friend("Anjali", "2002", 5.2)
    Friend4= Friend("Raj", "1982", 6.5)

    print("The friend's name is " + str(Friend1.get_name()))
    print("The friend was born in " + str(Friend2.get_birth_year()))
    print ("Friend is " + str(Friend3.get_height()) + ", (feet.inches), tall")
    print("Friend is " + str(Friend4.find_age(Friend4.get_birth_year())) + " years old" )
    print(str(Friend3.compare_height(Friend3.get_name(), Friend3.get_height())))


# call main function to execute functions listed under it
if __name__ == "__main__":
    main()
        

