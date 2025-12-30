input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

# step 1 -  parse input into a list of lists of strings, where each string is a single character
input_split = input.split("\n")

symbols = []
for line in input_split:
    
    list_line = list(line)
    
    symbols.append(list_line)

t = 0

for line in symbols:
    for c in line:
        print(c)
        if "^" in c:
            t = t + 1
        
    print(t)


    
    # step 2 - simulate the spltting

"""if ^ exists add  to string and at end print string"""
    


# step 3 - count the number of splits