## Python Challenge Excercises

* Complete the 4 challenge excercies using any IDE or Text-Editor
* Research common solutions online to complete each task
  
### Exercise 1 - The Middle Average Algorithm:

```
Specification: Read in integers until the user enters -1. 
If there were at least 3 values, show the average excluding the biggest and smallest number. 
If there are less than 3 values, print nothing. Refer to the Sample I/O.

Sample I/O:

    Value: 2
    Value: 5
    Value: 6
    Value: 7
    Value: 8
    Value: 87
    Value: -1
    Middle average = 6.5

```

### Exercise 2 - The Longest Dry Spell Algorithm:

```
Read in rainfall until the user enters -1. Show the longest dry spell.
A dry spell is a period of days with no rain. Refer to the sample I/O 

Sample I/O:

    Rainfall: 9.7
    Rainfall: 0
    Rainfall: 0
    Rainfall: 11.2
    Rainfall: 0
    Rainfall: 0
    Rainfall: 0
    Rainfall: 0
    Rainfall: 16.7
    Rainfall: 0
    Rainfall: 0
    Rainfall: -1
    Longest dry spell = 4

```

### Exercise 3 - The Number to Words Algorithm:

```
Read in numbers between 0-999 until the user enters -1. Print out the number in words. When -1 is entered, print "Done".
Use Australian English grammar. Note the spelling of "four", "fourteen" and "forty". Refer to the Sample I/O.

Sample I/O:

    Number: 17
    seventeen
    Number: 103
    one hundred and three
    Number: 800
    eight hundred
    Number: 42
    forty two
    Number: -1
    Done

```

### Exercise 4 - The File Encryption Algorithm:

* For this excercise using the text file: demo.txt. 

```
Pass in a filename as an argument to the Python script. The script should do the following:
-   Check if the file exists, if not print out a flag message
-   Read in a pattern from STDIN (a pattern is a string we want to find in the file)
-   Read in a replacement string from STDIN
-   Find all pattern occurances in the file and replace it with the replacement string
-   Print the updated file contents

Sample I/O: (capture filename as first argument)

    Pattern: <pattern string>
    Replacement: <replacement string>
    <updated file contents should be printed below>

```

### Exercise 5 - The IPv4 to Binary Algorithm:

```
Read an IPv4 and a CIDR prefix n (0 <= n <= 32) from STDIN. The Python script should do the following:
-   Convert the IP to Binary and print it out formatted as  xxx.xxx.xxx.xxx
-   Determine the Network Address based on n and print the Network Address in binary and decimal
-   Determine the Network Mask based on n and print the Mask Address in binary and decimal
-   Calculate and print the number of usable subnets for a prefix = (32-n)/2
-   Based on the above subnets calculate and print the number of usable hosts

Sample I/O: 

    IPv4: <xxx.xxx.xxx.xxx>
    Prefix: <prefix value>
    Network Binary: <binary value>
    Network Decimal: <decimal value>
    Mask Binary: <binary value>
    Mask Decimal: <decimal value>
    Usable Subnets: <subnets value>
    Usable Hosts: <host value>

```

### Exercise 6 - The Binary Search Algorithm:

```
Generate a random list of size n (entered from STDIN). Read in a number from STDIN and determine if that number exists in the list using Binary Search Algorithm.
See The Pseudocode to further understand the Binary Search Process and see the reference link below.

Binary Search algorithm: https://en.wikipedia.org/wiki/Binary_search_algorithm

Pseudocode:

Function binary_search
   A ← sorted array
   n ← size of array
   x ← value to be searched

   Set lowerBound = 1
   Set upperBound = n 

   while x not found
      if upperBound < lowerBound 
         EXIT: x does not exists.
   
      set midPoint = lowerBound + ( upperBound - lowerBound ) / 2
      
      if A[midPoint] < x
         set lowerBound = midPoint + 1
         
      if A[midPoint] > x
         set upperBound = midPoint - 1 

      if A[midPoint] = x 
         EXIT: x found at location midPoint
   end while
   
end function

```

### Exercise 7 - The Stretch of 2-Vowels Algorithm:

* Complete this algorithm using functions. Design your code to be re-usable using parametric functions in Python.

```
Read sentences from the user until * is entered. Show the number of words in each sentence that contain a stretch of non-z characters with exactly 2 vowels. 
Definition of a stretch: A stretch starts from the start of the word or after a 'z'. A stretch terminates just before another 'z' or at the end of the word.
Refer to the Example and to the Sample I/O.

Examples:

Matching words: zoo, azozooza, GONZALEZ
Non-matching words: ozo, azoooza

The sentences contain no punctuation, the words are separated by one or more spaces, and the characters may be upper or lower case. 
Keep reading sentences until the user enters "*".

Sample I/O:

    Sentence: azoooza azooza zoo azoo
    Matching words = 3
    Sentence: GONZALEZ passes the ball to VAZQUEZ
    Matching words = 3
    Sentence: azozototzeti
    Matching words = 1
    Sentence: *
    Done

```

### Exercise 8 - The Shapes Algorithm:

* Complete this algorithm using functions. Design your code to be re-usable using parametric functions in Python.

```
Geometric Shapes are determined using sides and radius. Read from STDIN an integer radius and integer sides ( >= 3).
1 - Use the radius to calculate and print the following:
    - Circle area
    - Sphere Volume
2 - Use the sides to calculate and print the area of the shape:

Sample I/O:

    Radius = <STDIN>
    Sides  = <STDIN>
    Circle area = <area value>
    Sphere volume = <volume value>
    Shape area = <area value>

```

### Exercise 9 - The Cities Statistics Algorithm:

* For this excercise using the CSV file: worldcities.csv. The file contains cities and its population.
* Complete this algorithm using functions. Design your code to be re-usable using parametric functions in Python.

```
Map the worldcities.csv file to a Python dictionary and complete the following steps:
1 - Count the number of cities with population greater than 100000 (1 million).
2 - Determine and print out the Mean, Variance, and Standard Deviation of the cities' populations.

Sample I/O:

    Cities with population greater than 1 million: <output the value>
    Matching words = 3
    Mean = <mean value>
    Variance = <variance value>
    Standard Deviation = <standard deviation value>

```

### Exercise 10 - The Satellite Orbital Speed Algorithm:

* Complete this algorithm using functions. Design your code to be re-usable using parametric functions in Python.

```
Determine the speed (v) of a satellite at a position A(x,y) from the center of the Earth.[Refer to the Satellite Orbital Image Below]
Read in first the (x,y) position of the satelllite from STDIN and based on these values calculate and print the satelllite speed (v).

Given are the following constants:
Gravity value G = 9.807 m/s²
Earth mass    M = 5.9722 x 1024 kilograms
Earth radius  R = 6,371 km


Sample I/O:

    x = <value of x>
    y = <value of y>
    Satellite speed v = <speed value>

```
## Orbit Formula Overview:
![orbit](https://user-images.githubusercontent.com/21999135/159645984-45b785b0-adf4-4223-9638-b76f6e8736d2.jpg)

