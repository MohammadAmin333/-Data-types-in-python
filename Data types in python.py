'''#Student Information System
Student_Name = input("Enter Student Name: ")
Student_Age = int(input("Enter Student Age: "))
Student_Class = input("Enter Student Class: ")
Student_Section = input("Enter Student Section: ")
Student_Roll_No = input("Enter Student Roll No: ")
Student_Class_Monitor = input("Is Student Class Monitor? (yes/no): ").lower()=="yes"
Science_Lab = input("Dose Science Lab Access ?  (yes/no): ").lower()=="yes"

print(Student_Name)
print(Student_Age)
print(Student_Class)
print(Student_Section)
print(Student_Roll_No)
print(Student_Class_Monitor)
print(Science_Lab)'''


# Football player and team details  
player="Messi"  
team="Barcelona"  
match_starts="8:00 PM"

print(f"Length of player name: {len(player)}")  
print(f"Length of team name: {len(team)}")  
print(f"Match starts at: {match_starts}")

#indexing  
print(f"First letter of the player name {player[0]}")  
print(f"Last letter of the player name {player[-1]}")
print(f"First letter of the team name {team[0]}")
print(f"Last letter of the team name {team[-1]}")

Str = "string"  
print(Str[:3])     
print(Str[0:1])  
print(Str[::-1])   

#slicing
print(f"First three letters of the player name {player[:3]}")
print(f"Last three Letters of the player name {player[-3:]}")

#reverse the string
text="Hello World"
revtext =text[::-3]