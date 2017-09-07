#!/usr/bin/perl
# Above Line is called as Shebang line in Unix, which tells about the interpretor
# Interpreter name mentioned after the shebang Line.
#
#
# Ajay's First attempt to write a Perl script
# Author : Ajayaghosh VL
# Help : Self & Guide
#
#

#*************************************************************************************************************************************************
#																																				 #
#										 **** CHAPTER 1 ******																					 #	
#																																				 #
#*************************************************************************************************************************************************
#
use warnings; # This will trun on warnings
use strict;  # Running program in strict mode, for more details please see below.

# * Below line prints the message inside the quotes. *
# print "Hello This is My First Script\n";

# * Below is a block of statement *
# {
#   print "This is ";
#   print " a block";
#   print "  of statements\n";
# }

# * Blocks inside the blocks; for better programming practice. *
# print "Top level\n";
#     {
#     print "2nd Level\n";
#       {
#       print "3rd Level\n";
#       }
#     print "Where are we ?\n";
#     }

# * Using print function to handle multiple aruguments together. This makes things more clear & better programming practice *
# print ("This ", "was ", "printed ", "as ", "Multi ", "Argument ", "print ", "function ", "\n");

# * Below are are various Escape Sequance tests *
# print "Testing a new Line\n";      # new Line   	[ Escape Sequance ]
# print "Testing a back Space\b";    # back Space 	[ Escape Sequance ]
# print "Testing a Tab Space\tOK";   # Tab        	[ Escape Sequance ]
# print "Testing a Alarm bell \a";   # Alarm      	[ Escape Sequance ]
# print "Retun\r"; 	     	     # Carriage return  [ Escape Sequance ]
#
# * What is "white Space" ? *
# White space is the name given for the space & tabs which we used infront of function, like the alingment diffrence between if, then, fi

# * How to debugg a programm *
# perl -d <program_name> # This way you can debugg your programm

# * Excercise one * 
# print "\nThis is my first Excercise\n"

#*************************************************************************************************************************************************
#																																				 #
#											*** CHAPTER 2 ****																					 #
#																																				 #		
#*************************************************************************************************************************************************
#
#
# * Types of Data in perl *
# Literal  - Literal is a value which never changes, for example number - 5, floating point number - 25.347, Sting Like - "hello all, how are you"
# Variable - Variable holds a value in memory & it can be changed.

# * Using number system in Perl - Perl detects numbers in different systems such as decimel, binery, octal & hexadecimel *
# Numbers are normally called as literal in perl
# Decimel Numbers - Normal numbers which we use & they don't have any Prefix
# Binary Numbers  - Binary numbers will starts with prefix "0b (zero b)", example - 0b11111111
# Octal Numbers   - Octal numbers will start with prefix 0 (zero not oh), example - 0377
# Hexadecimel     - Hexadecimal numbers will start with prefix 0x (zero x), example - 0xFF
# NOTE : Always make sure when we use octal, binary & hexa what we uses fall under the limit, for example octal must  be only from (0 - 7),  can't use 8 there`
# print 255,        "\n"; # Decimal,         output printed will be decimal - 255
# print 0377,       "\n"; # Octal(0),        output printed will be decimal - 255
# print 0b11111111, "\n"; # Binary(0b),      output printed will be decimal - 255
# print 0xFF,       "\n"; # Hexadecimal(0x), output printed will be decimal - 255

# * Printing numbers in perl *
# print 24, " ", "-4\n"; # This will print a line like "24 -4" & will insert a new line

# * Using number chunkings to represent larger numbers *
# print 10_000_000, "\n"; # This will provide output as 10000000 which doesn't cause confusion while reading program
# print (10_000_000, " ", "-4\n"); # Can be used in this way print as "10000000 -4"

# * Using floating point numbers *
# print ("Appromate Value is ", 24.56188888, "\n") # output will be "Appromate Value is 24.56188888"

# * Single quoted & double qouated strings *
# Single quoted strings will take everything to just print, that is even escape sequance also, like \t, \n etc
# Double quoted strings will process strings completely including their escape sequance
# print '\t This is a single quoted string\n'; # This will print output as "\t This is a single quoted string\n"
# print "\t This is a single quoted string\n"; # This will print output as "         This is a single quoted string" 
# print "Hey It's easy to use to Single quote to print\n"; # This is the way to print Single qoute in a string  
# print 'hellow "world" can you see double quote' # This is one way to print double quote in a string
# print "hellow \"world\" Can you see double quote" # This is another way to print double quote in a string

#  * using qq/ and q/ quotes *
# qq/ - This represent double quote
# q/  - This represent single quote
# print (qq/ This line using qq escape sequance \n/); # here we are using qq/ / inplace of " " 
# print (q/ This line using "q" escape sequance \n/); # here we are using q/ / inplace of ' '

# * using alternate delimeter along with qq or q *
# Perl supports any alphanumeric charater as alternate delimeter (i.e, rather than qq\ ... \, we can use qq< ... > or qq# ... # etc)
# print qq|'"Hi," said Jack. "Have you read /. today?"'\n|; # here we are using qq|...| inplace of qq/.../
# print qq#'"Hi," said Jack. "Have you read /. today?"'\n#; # here we are using qq#...# inplace of qq/.../
# print qq('"Hi," said Jack. "Have you read /. today?"'\n); # here we are using qq(...) inplace of qq/.../
# print qq<'"Hi," said Jack. "Have you read /. today?"'\n>; # here we are using qq<...> inplace if qq/.../

# * Here documents - Printing paragraph or long strings *
# Here document works just like double quated strings, here we are marking strings with the help of labels, there are mainly two types of labels
# EOT - End of text 
# EOF - End of File
# To use here document there should be print function followed by <<EOT; or <<EOF;, there shouldn't be any space between "<<" and label. 
# even though ";" is specified in the starting line it will cover for the complete print statement
# so the syntax should be print <<EOF; string EOF
#
# print <<EOF;
#
# Hello all, This is a here Document which is priting.
# This can be used with the syntax given.
#
# EOF

# * Arithametic Operators - Arithaeatic operators are the normal operators used to perform various arithametic operations *
# +  - Addition
# -  - Substraction
# *  - Multiplication
# /  - Division 
# ** - Exponential Operator
# %  - Remainder or Modular Operator
#
# print (725 + 86, "\n"); # This is  how you add two numbers in perl
# print (725 - 86, "\n"); # This is how you substract two numbers in perl
# print (725 * 86, "\n"); # This is how you multiply two numbers
# print (725 / 86, "\n"); # This is how you perform division in perl
#
# Operator precedence - This  means the priority of the operators which perl give "* & /" has more priority than "+ & -".
# So when you want to use there opearators together then you need to use paranthesis ( ).
# Example
# print "Value of 2 + 8 * 10 is = ", ((2 + 8) * 10), "\n"; # here the answer is 100, if we didn't used the () then it was 82
#
# Exponential Operator (**) - This operator is used to increase the power of a given number
# print 2**4, " ", 3**3, " ", -2*4, "\n"; # This is equal to "2*2*2*2", "3*3*3", "-2*-2*-2*-2"i & output printed will be "16 27 -8"
# But for above example -2*4 should be 8 rather than -8, this is because of the precence so when we are using -ve  we need mention this as unary operator.
#
# Remainder or Modular Operator (%) - This operator used to find the remainder value which comes out of two numbers division
# print "15 devided by 2 is = ", (15 / 2), "\n";
# print "Remainder Value is = ", (15 % 2), "\n";

# * Bitwise operator - These are used to handle with binary & mostly used in low level file handling *
# &   - AND operator
# |   - OR  Operator
# ^:  - XOR operator
# ~   - NOT operator

# * Truth and Falsehood in perl - it is important to know that how to represent true & false in perl *
# FALSE - 0 (zero) is represented as "false", it is also represented as " " (none) or undefined or empty list
# TRUE  - 1 (one)  is represented as "true"
# This will be used in many occasions where we need to test some condition or compare two numbers etc ...
# print "True or False, 2 and 3 are equal ", 2 == 3, "\n"; # Output which result this will be none since this is false
# print "True or False, 2 and 2 are equal ", 2 == 2, "\n"; # Out of this will be 1 Since it is true 

# * Comparing Numbers *
# ==  - Two equal signs are used to compare two operands for equality, it will tell perl to return true if two numbers are equal & false if not.
# !=  - Using "!" infront of "=" sign will act as not equal to operator, here if two numbers are not equal that tell perl as true & false if yes.
# >   - This operator is used to check whether a number is greater than an another number, if this is greater then return true & false if not.
# <   - This operator is used to check whether a number is less than anotehr number, here if the number is less then return true & false if not.
# Few examples 
#
# print "Five is greater than 6 ", (5 > 6), "\n"; 		# here the result printed will be none / empty, i.e false
# print "Five is less than 6 ", (5 < 6), "\n";    		# here the result printed will be 1, i.e true
# print "Five is eqaul to 6 ", (5 == 6), "\n";    		# here the result printed will be none / empty, i.e false
# print "Five is not equalto 6 ", (5 != 6), "\n"; 	        # here the result printed will be 1, i.e true
# print "Five is greater than or equal to 6 ", (5 >= 6), "\n";  # here the result printed will be none / empty, i.e false
# print "Five is less than or equal to 6 ", (5 <= 6), "\n";     # here the result printed will be 1, i.e true
# print "Five is less than or equal to 5 ", (5 <= 5), "\n";	# here the result printed will be 1, i.e true

# * Boolean Operators *
# boolean operators are used to evaluate multiple statements of true & falsehood.
# && - This will become true if both conditions are true, else false
# || - This will become true if any of the condition is true

# * String Operator *
# strings operators are used to handle strings, various ways of handling strings are explained below.
# print "Print ", "several ", "strings ", "here", "\n"; # Here we are printing single statement as multiple strings
# print "Print " . "one ". "string " . "here" . "\n"; 	# This is another way of printing the statement using multiple string
# print "print Several Strings together here", "\n";	# Here we are printing a statement as complete single string
# 
# When we join a number to a string, then number will be evaluated & then converted, see an example below 
# print "3 raise to 2 is equal to ", 3**2, "\n"; # Here string will be processed & number will also be evaluated while printing
#
# Repetetion Operator
# x - repetetion operator is represented by "x", repetetion operator is used to multiply a string with given number & then print.
# print "printing Five Times > ", ("Go!! " x 5), "\n"; # Output will be "printing Five Times > Go!! Go!! Go!! Go!! Go!!"

# * String Comparison *
# Will study this chapter later

# * Variables *
# Variable is a storage for scalars, Also variable can store data of various types. 
# scalar varable start with "$" sign, for example $name
# scalar is assigned to a variable using an "=" operator, Single equal operator used for assignment.
# example 
#
# $name = "self";
# print "My name is $name", "\n";
# print qq|$name is my best friend\n|;
#
# To Modify a value stored in a variable simply assign another value to the same variable, see an example below 
# $kid_name = "Vaiga";
# print "My first kid name is $kid_name\n";
# $kid_name = "Rishi";
# print qq|My second kid name is $kid_name\n|; 
#
# we can also do calculations & assign values to variable, see few examples below 
# $sum=(4 +3);
# print "Sum of 4+3 = $sum \n";
#
# $muiltiplied_value=(4*3);
# print "Multiplied value of 4*3=$muiltiplied_value \n";
#
# $devided_value=(4/3);
# print "Devided value of 4/3=$devided_value \n";
#
# Also we can perform calculations using variables once after the value is assigned
# $a=5;
# $b=($a+10);
# print "Sum is $b \n";
#
# $a=5;
# $b=10;
# $c=($a+$b);
# print qq|Total Sum = $c \n|;
#
# Auto-Incriment & Auto-decrement in variables
# There are some special operator used to perform auto-increment & auto-decrement in variables.
# ++ : Performs auto-increment
# -- : Performs auto-decrement
# 
# Post-increment - using this method value of the variable will be increased only after the assignment.
# 		 - That means when a varaible gets assigned to another variable its current value will be passwd to new variable & after the assignment it will get incremented. 
# 		 - Looking at below example when $a gets assigned to $c, $c gets the value of 5 which is the orginal value of $a & after assigment $a becomes 6 which happens as post increment.
# Examples 
# $a=5;
# $b=10;
# $c=$a++;
# print "Printing Variables $a, $b, $c \n"; # Output is - "Printing Variables 6, 10, 5"
# 
# Pre-increment - using this method value of a variable will be incremented well before the assignment itself.
# 		- looking at below example when $a gets assigned to $c, then firstly $a will get incremented & the incremented value will be assigned to $c. So both $a & $c are 6 here. 
# $a=5;
# $b=10; 
# $c=++$a;
# print "Printing Variables $a, $b, $c \n"; # Output is : "Printing Variables 6, 10, 6"
#
# Post-decrement - Using this method value of a variable will be decerementing only after the assignment
# 		 - Here value of $a will be assigned to $c & then $a will go for an increment. So value of $c will be 5 (Current value of $a) & $a will get decremented to 4 after that.
# Example 
# $a=5;
# $b=10;
# $c=$a--;
# print "Printng values of $a, $b, $c \n"; # Output is : Printng values of 4, 10, 5
#
# Pre-decrement - Using this method variable will be decremented well before the assignement
# 		- Here value of $a will get decremented & it will get assigned to $b, so as a result of that $a & $b will have the same value. 
# $a=5;
# $b=10;
# $c=--$a;
# print "printing values of $a, $b, $c \n"; # Output is - "printing values of 4, 10, 4"
#
# Multiple assignments - Using "=" operator we can assign value to any varable as seen below 
# 		       - Here all varables will have the same value 1, first C will get assign with the value, then c will pass the same b & then b to a.
# $a = $b = $c = 1;
# print "$a \n"; # Output is - "1"
 
# * Scope *
# When we start creating large programs it will be a challenge to declare variables, especially when we uses sub-routines. Because may be multiple sub-routes may need
# Same variable for some specific operation, but when we uses the same variable names which used above it can carry the same values which we stored before.
# To avoid these circumstances we can declare variables with in the scope of a specific block. This is called as scoping
#
# What are the methods of scoping described below.
#
# * Lexican Varibale *
# Lexican variables are used to define a variable with in the block. When a lexican variable is assigned to a block it will avaiable to any block which comes with in
# same block. if you declare lexican variable outside a block then it will be available to the entire program in the file.
# Lexican variable can be represented using "my $variable"
#
# Lexican variable assigned with in the block is no way related to the global variable assigned in the program. lexican variable expires when the block ends. 
#
# Example
#
# $record=7;
# print "Value Record Ouside the block is, $record \n"; 			# Here output printed is "Value Record Ouside the block is, 7"
#
#	{
#	my $record=4;    												# If you want to test whether this works or not, then remove "my" here & execte the script
#	print "Value of Record Inside the block is, $record \n"; 		# Here output printes is "Value of Record Inside the block is, 4"``
#	}
#
# print "Again printing the value outside the clock, $record \n";	# Here output printed is "7" when we used lexical variable else it was "4"
  
# * "use strict;" or Writing program in strict mode *
# In order to make our program more clear we will request perl to be more strict.
# One of the benifit out of using "use strict" statement is it make sure all variables are declared as lexican variables.
# 
# Also strict is capable to understand spelling mistakes upto an extend.
#
# Example
#
# use strict;
#
# my $record=7;																	# without my() Error - "Global symbol "$record" requires explicit package"
# print "Value of Reocord Outside the block is $record \n";
#  
#	{
#	my $record=5;
#	print "Value of Record inside the block is $record \n";
#	}
#
# print "Again priniting the value of Record outside the block $record \n";
 
# * How to call Variables *
# scalar variables should start with a "$" symbol & next to follow is a character strictly not a number.
# once after the "$" & then chareter, then you can use number, "_" etc.
# Few examples of variables can be used & can't be used are given below.
# 
# $user 	- Permitted
# $User 	- Permitted
# $USER 	- Permitted 
# NOTE : perl is case sensitive & if you declare above three variables in the same program it consider it as three different variables.
#
# $user_1	- Permitted
# $Test1	- Permitted
# $user_id  - Permitted
# $I_am_a_long_variable_name - Permitted
# 
# $1user	- Not permitted # a numeric value followed by "$" is not supported.
# $10c		- Not permitted
# $user-id	- "-" symbol is not permitted,instead you can use "_".
#
# Special Variable ($_)
# Perl provides a internal default variable for usage that is used as "$_" more details about this variable will be given later.
#
# Interpolation or representation of variable in a statement
# Few methods of interpolating variables are described below 
#
# use warnings;
# use strict;
#
# my $name="Tony";
# print "You are $name \n"; # output will be "You are Tony"
# print 'You are $name \n'; # output will be "You are $name" , also there won't be any new space
#
# my $name="Shuppu";
# my $salutation="Dear $name";
# print "$salutation \n";   # Output printed will be "Dear Shuppu"
#
# my $name="Tuplu";
# my $number=2;
# print "Dear $name is our $number nd baby \n";  # here output will be "Tuplu is our 2 nd baby", this can be expressed in a better way below
# print "Dear $name is our ${number}nd baby \n"; # here output will be "Dear Tuplu is out 2nd baby". curl braces "{ }" will help to distungush variable & statement.
 
 
# * How to read "standard input" /  "<STDIN>" to a script *
# Perl reads standard input from keyboard using "<STDIN>".
# When it reads the value, it reads along with the newline. So there is no need of an extra newline.
# We can read a standard input using below method.
#
# print "Hey Enter some value to read : ";
# my $value=<STDIN>;
# print "\nValue which you are entered is : $value \n";
#
# Example Program
#
# use warnings;
# use strict;
#
# print "Please enter todays exchange rate for INR : ";
# my $exchange_rate=<STDIN>;
# print "Total amount in SGD : ";
# my $sgd_amount=<STDIN>;
# print "SGD amount $sgd_amount is equal to ", ($sgd_amount*$exchange_rate), " Indian Rupees\n"; # Output printed in two lines using the new line of "$sgd_amount"
 
# * "chomp() & chop()" functions *
# chomp() & chop() are used to remove the last line of a string, how they differ explained below
#
# chomp() - This function will remove the last character only if the last character is a "new line". chomp() can be used as follows.
# $read_variable=<STDIN>; 			# Here variable is geting read from standard input
# chomp($read_variable);  			# Here last new line charector is removed using chomp
# chomp ($read_variable=<STDIN>);   # Here reading variable & removing the new line is done on the same line itself
#
# Example : # This is an example which we did above, on above program output printed in two lines due to the newline in the standard input read from keyboard.
#
# use warnings;
# use strict;
#
# print "Please enter todays exchange rate for INR : ";
# chomp (my $exchange_rate=<STDIN>);
# print "Total amount in SGD : ";
# chomp (my $sgd_amount=<STDIN>);
# print "SGD amount $sgd_amount is equal to ", ($sgd_amount*$exchange_rate), " Indian Rupees\n"; # This print in single line since chomp() removed newline from "SIDIN"

# chop()  - This function will remove any last character regardless any character. How to use chop() is given below
#
# Example
# 
# use warnings;
# use strict;
# my $string="serail number 1, 2, 3";
# chop ($string);
# print "Printing $string \n"; # Here last letter of the string "3" is removed from the output
 
# * "exit() & die()" functions 
#
# * exit() - in shell normally exit function will exit the program & return the value to shell in any argument is provided 
# Normally in shell "0" value for a exit code means normal & everything is good. Any "non-zero" value is considared as failed.
# Also in shell we can used "echo $?" to understand about the exit or return code of a last executed command.
#
# Example :
#
# use warnings;
# use strict;
#
# print "Enter dummy exit code you want to check : ";
# chomp (my $value=<STDIN>);
# exit($value) ; 		# use "echo $?" from shell to understand about the retrun code
#
# * die() - This is a permenant solution to handle errors in perl. 
# Whenever there is a statement or string is passed to " die() " function, it automatically print it as "standard output" & terminate the program
# Also when it exit the program it tell with the name of the program & line number where it is called
# More over when " die() " is called, it terminate the program with a non-zero exit code & append a newline "\n" also.
# using all above function "die()" can be used the permenant solution to exit on false condition & it will be very useful to debug the program.
#
# Example
#
# use warnings;
# use strict;
#
# print "Enter Someting to print along with die function for testing :";
# chomp(my $error_message=<STDIN>);
# die($error_message);													  # Program will terminate here wthe message on "$error_message" & return code will be non-zero
# print "This message will not be printed since die used above\n";        # This line not printed since "die()" used above
#
#
# ** Function learned in CHAPTER 2 **
#
# chop 	: To remove the new line charector from a variable, only new line will be removed
# chomp	: To remove the last element of a variable, any element will be removed 
# exit 	: To exit from a program by passing exit code to the shell
# die	: This will terminate the program, will give the error message which is defined & the return code will be non-zero
#
#


#*************************************************************************************************************************************************
#																																				 #
#								***** Chapter 3 - Controll flow constructions *****																 #
#																																				 #
#*************************************************************************************************************************************************
# 
#
# * "if" statement *
# In programming language "if" statement is used to test a condition & if the condition is true take some action
#
# Syntax :
#
# if (condition) {
#	  statement(s)
#	  )
#
# Note : here conditions are tested inside the paranthesis() & statements are given inside the curl braces{}.
#
# Example : Create a program to read a number & devide  if the given number is not zero.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
#	print "Please enter number : ";
#	chomp(my $number = <STDIN>);
#	my $result=0;
#	if ($number !=  0) {                # This will help to execute below statements if the $number is not zero
#	$result=(100/$number);				# Result will be stored in $result once after the calculatiions are done
#	print "Result is : $result \n";     # here result will be printed
#	}
#
# Note : When you are programming with perl using "if" statement please note that it uses the "Boolean logic" to determine a condition is true or flse.
#        Also you need to be remaind about these mentioned below
#		 * An empty string "" is false.
#		 * A number "0" or string "0" is false.
#		 * An empty list () is false
# 		 * Then undefined value is false
#		 * Everything else is true.
#
 
# * Comparing numbers *
# We can test two numbers which is stored in a variable "$x" & "$y" using below operators
#
# $x == $y  : This is to test if both number has same value or not.
# $x > $y   : This is to test if $x is greater than $y 
# $x < $y 	: This is to test if $x is smaller than $y
# $x >= $y	: This is to test if $x is greater than or qaual to $y
# $x <= $y 	: This is to test if $x is smaller than or equal to $y
# $x != $y 	: This is to test if $x is not equal to $y
#
# Note : when we we are comparing numbers make sure we are using "==" sign. Else perl may think we are trying to assign the value of $x to $y with "=" sign.
#
# Example : Below example is used to compare a target number which defined in script & a guess number which gievn as <STDIN>
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
#	my $target=15;
#	print "Now you can guess a number & see that is correcti\n";
#	print "Please enter your guess :";
#	chomp(my $guess=<STDIN>);
#
#	if ($target == $guess) {
#	print "Your guess is correct & the target number is also $guess\n";
#	}
#
#	if ($guess > $target) {
#	print "You have entered a value which is greater than the target value\n";
#	}
#
#	if ($guess < $target) {
#	print "You have entered a value which is less than the target value\n";
#	}
# }
#
 
# * Comparing strings *
# We can test two strings using below operators 
#
# $x gt $y	: This is to test if string $x is greater than $y
# $x lt $y	: This is to test if string $x is less than $y
# $x ge $y 	: This is to test if string $x is greater than or equal to $y
# $x le $y 	: This is to test if string $x is less than or equal to $y
# $x eq $y 	: This is to test if string $x is equal to $y 
# $x ne $y 	: This is to test if string $x is not equal to $y
#
# Example : Below example is to verify the user password
#
# #!/user/bin/perl
# use warnings;
# use strict;
#
#{
#	my $master_passwd="Tuplu";
#	print "Please enter your password :";
#	chomp(my $user_passwd=<STDIN>);
#	
#	if ( $master_passwd eq $user_passwd ) {
#	print "success : You have entered correct password !!!\n";
#	}
#
#	if ( $master_passwd ne $user_passwd ) {
#	print "failed : You have entered an incorrect password\n";
#	}
#}
 
# * defined() Function *
# defined() function is used to to check a variable is defined or it is undefined. What is the definition of defined & undefined is given below.
# defined 	: means there is some value allocated to that varable.
# undefined	: means there is some no value allocated to that variable. 
#
# Example : Below example gives an idea about how & when to use the defined function
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
#{
#	my ($var1, $var2);
#	$var1=23;
#
#	if ( defined $var1 ) {							# here this will print the result since the statement is true
#	print "variable 1 is defined with a value.\n";
#	}
#
#	if ( defined $var2 ) {							# here this will not print any result since the statement is false.
#	print "variable 2 is defined with a value.\n";
#	}
#}
 
# * Logical operators *
# Below are the list of logical operators available in perl
# 
# $x && $y 
# $x and $y   True if both $x and &y are true
# 
# $x || $y
# $x or $y  True if either $x or $y is true. Or if both are true
#
# ! $x
# not $x	True if $x is not true
#

# Test Meaning ( for if)
# Below test conditions can be used along with 'if' to test various conditions 
# 
# Test			Meaning
# -e 			True if the file exist
# -f 			True if the file is a plane file not directory
# -d 			True if the directory exist
# -z			True if the file has zero size
# -s			True if the file is non-zero size, size taken in bytes
# -r			True if the file is readable by you
# -x 			True if the file is executable by you
# -w 			True if the file is not writable by you
# -o			True if the file is owned by you
#
# Example : Below example will tell us about test condition 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# {
#	my $ls_cmd = "/bin/ls";
#	if ( -x $ls_cmd ) {
#		print "Command : $ls_cmd exist \n";
#		}
# }
 	
# * if .. else * statement
# "if..else" is used to perform both testing,i.e test whether the condition is true of false. If true what to do & if false what to do
#
# syntax : 
# 			if (condition) {
# 				 action } ;
# 			else {
#				alternate action } ;
#		
# Example : In blow example we are verifying the password. 
# 
# #!/usr/bin/perl
# use warnings;
# use strict;
#
#{	
#	my $master_password="test";
#	print "Please enter your password to login :";
#	chomp(my $user_password=<STDIN>);
#	
#	if ( $master_password eq $user_password ) 
#		{
#		print "Success : You entered correct password & Login successful\n"; 
#		}
#	else 
#		{
#		die "Incorrect password"; 	
#		}
#		
#}
 
# * if .. elseif .. else * statement
# This statement is used to test multiple conditions in the same if statement. Sometimes we will have occassions where if one condition is true 
# we need to make sure another condition is also true to take the correct action. This can be achieved by "if .. elseif .. else" statement
#
# for example using "if .. elseif .. else" we convert a complex condition to simple as below
#
# Complex method : 
#
# 	if ( condition 1 ) 
#	{
#	action 1
#	} 
#	else 
#		{
#		if ( condition 2) 
#		{
#		action 2
#		} 
#		else 
#			{
#			if (condition 3) 
#			{
#			action 3
#			} 
#			else 
#				{
#				action 4
#				}
#			}			
#		}
#
# above statement is bit messy due many conditions and also with the more usage of curl{} braces. It can be written on more simplified method as below
#
#	if ( condition 1 ) 
#		{
#		action 1 ;
#		} 
#	elsif ( condition 2 ) 
#		{
#		action 2 ;
#		} 
#	elsif ( condition 3 ) 
#		{
#		action 3 ;
#		} 
#	else 
#		{
#		action 4 ;
#		}
#
# Example : Below program is to check the username & password for various users 
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#	{
#	print "Please enter user name to login :";
#	chomp(my $username=<STDIN>);
#	print "Please enter password for $username :";
#	chomp(my $password=<STDIN>);
#		if ( $username eq "ajay" )
#			{
#			if ( $password eq "ajay123" )
#				{
#				print "You are successfully logged in as $username\n";
#				}
#			else
#				{
#				die "Login Failed" ;
#				}
#			}
#		elsif ( $username eq "appu" )
#            {
#            if ( $password eq "appu123" )
#                {
#                print "You are successfully logged in as $username\n";
#                }
#            else
#                {
#                die "Login Failed" ;
#                }
#			}
#        elsif ( $username eq "shuppu" )
#            {
#            if ( $password eq "shuppu123" )
#                {
#                print "You are successfully logged in as $username\n";
#                }
#            else
#                {
#                die "Login Failed" ;
#                }	
#			}
#       elsif ($username eq "tuplu" )
#            {
#            if ( $password eq "tuplu123" )
#                {
#                print "You are successfully logged in as $username\n";
#                }
#            else
#                {
#                die "Login Failed" ;
#                }
#			}
#		else
#			{
#			die "invalid username";
#			}
#	}	# End of program

# * unless * statement
# This is another way of saying "if" statement. "if" normally deals when it is 'true', but unless will process the condition is false
# Syntax :
#
#	unless ($a) {
# 	print "$a is not true\n";
#	}
#
# Note : here the physichology is different but the effect is same, this a feature if perl which gives flexibility with someones thought.
#

#	** Looping constructs **
# Now we are okay with checking everything once. But in some occassion we need to perform various checks & conditions in loop. 
# there are two types of loops 
# Definite loop - in these loops we know how many times this loop is going to repeat
# indefinete loop - here program should check the condition & verify that whether the loop should continue or not

# * while * loop
# This can be used as a definite & indefinite loop. It keep doing something when the condition is true.
# Syntax :
#
# while ( condition ) { action }
#
# Example : Below is an example to print the numbers while the condition is true
#
# #!/usr.bin/perl
# use warnings;
# use strict;
#
# my $counter=0;
# while ( $counter <= 5 ) 
#	{
#	print "Counter value is $counter \n"; # This will print the value of $counter till the value become 5.
#	$counter++ ;
#	}
#
# * Reading <STDIN> in whileloop & using magical variable "$_"  *
# We can read the standard input "<STDIN>" using following methods.
#
# while ($variable_name=<STDIN>) { print "$variable_name; } # Here STDIN will be stored into a variable & we will use that later to print.
# 															# Above loop will call STDIN until the end of file since this is called inside the () of while loop.
#
# while (<STDIN>) { print "$_"; }							# We are using "$_" here because any line of input will be magically assigned to magical variable "$_"
#															# This statement is exactly similar to the above, but here we used magical variable "$_" to achieve.
#
# while (<STDIN>) { print; }									# here we are not using any variable while reading & print. Because print funtion by default prints "$_"
#															# here STDIN gets assigned to "$_" when reading & print will print "$_" as the dafult variable.
#
# NOTE : here "End of File" means using the "^ D" or ctrl+D in unix keyboard
#
# Example : Below example will read a STDIN & it will print until the end of file
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# while (<STDIN>) 
#	{
#	print "You have entered valuei : ";
#	print ;									# This will print the values which read by the STDIN in the while loop.
#	}
#
# NOTE : The magic variable "$_" is very useful & it is the default variable for many functions such as "chomp()" etc..
#        For example, below a program is given which can be written using the advantages of magic variable "$_"
#
# while ( $input = <STDIN> ) { chomp($input) ; action; } # Here program is written in a way where it stored in a defined variable & then process using that.
# while ( <STDIN> ) { chomp; action; }					 # Here the variable was stored in magical variable "$_" & processed using that, but can't see that defined :)
#
# * Infinite loop using while loop *
# If the condition we are testing is always true then it is going to create program which will run in infinite loop
# 
# Example : This program is to list numbers & it never stops until we break this one.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# my $counter=1;
# while ($counter > 0)
#	{
#	print "$counter \n";
#	$counter++;
#	}

# * until () loop *
# Like the opposite of "if" is "unless" the same way "until" act as the opposite for "while" loop. 
# until () will process only if the condition is 'fasle', upon true it will ignore.
#
# Example : In below program even though we defined to print until the counter is greater than $5, so it prints from 1 .. 5, Exactly opposite to what while does.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# my $counter=1;
# until ($counter > 5)
#	{
#	print "$counter \n";
#	$counter++;
#	}

# * for * loop
# "for" loop in perl is an alternate way to use "while" loop, syntax is as follows
#
# Synatx : for ( init_expression; test_expression; step_expression ) { action }
#
# init_expression - it is done first & only at once.
# test_expression - this will test the condition is true or false, if it is true then will execute the action. Then do step_expression & so on.
# step_expression - this will used to step up / down the values as requested 
# 
# Example : Below example is to print the numbers until 5. 
#
##!/usr/bin/perl
# use warnings;
# use strict;
#
# for ( my $i=0; $i < 5 ; $i++ ) 
#	{
#	print "Current value is below 'five' & it is : $i \n";
#	}

# * foreach * loop
# This loop will help to list through lists and arrays.
#
# Example : Below is an example for "foreach" loop processing through arrays, this will print numbers from 1 - 10.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# my $number;
# foreach $number ( 1 .. 10 )
#	{
#	print "Current number is : $number \n";
#	}
#
# Above program can be re-written as below, which gives 2 more advantages. One we are declaring variable as lexican inside the loop, which satisfies "strict"
# Second advantage is since "$number" is written inside the loop it applies only to the loop not outside.
#
# foreach my $number ( 1 .. 10 )
#	{
#	print "Current number is : $number \n";
#	}

# * "do .. while" & "do .. until"
# usage of "do .. while" & "do .. until" are body of the program gets executed atlease once, then only condition is getting tested. 
# These loops can be used where you feel body or text need to be displayed atlease once before testing your condition.
#
# Syntax : do { action } while ( condition ) ;
#		 : do { action } until ( condition ) ; 
#
# Example : Testing "do .. while"
#
# #!/usr/bin/perl
# use warnings;
# use strict;
# {
# my $number=0;
# print "Testing \"do .. while\" loop \n";
# do {
#	print "current \$number is : $number \n";
#	$number++;
#	}
# while ( $number < 6 );
# }
#
# Example : Testing "do .. unitl" loop
# 
# #!/usr/bin/perl
# use warnings;
# use strict;
# {
# my $number=0;
# print "Testing \"do .. until\" loop : \n";
# do
#	{	
#	print " Value of \$number is : $number \n";
#	$number++;
#	}
# until ( $number > 6 );
# }

# * Expression modifying *
# we can modify the while & until expression as we see below, which gives bit interesting way of programming. 
#
# while ( condition ) { statement } ; # This is normal way of writing while loop, this can be modified as below
# statement  whille  condition ;	  # This is the modified form. 
#
# until ( condition ) { statement } ; # This is the normal way of writing until loop, this can be modified as below
# statement until condition ; 		  # Modifiled form
#
# Example :
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# { print "You have entred value as : $_ " while <STDIN>; } # This read the value & will print the same.

# * Loop Control Constructs *
# Perl provides loop control constructs which will help to breakout of the loop, next iteration of the loop & re-execute the loop.
#
# * last - To Break out from loop * 
# When you use "last" keyword in a loop it immeditely exit from that loop (without executing any further steps in that loop) & continue with remaining steps in script.
# "last" keyword can be used with "while, until, for & foreach" loops, but it doesn't work with "do .. while" or "do .. until" loops.
#
# NOTE : last keyword will help to exit only from the loop not from statements like "if" or "unless".
#
# Example : below program will check for the input till 5 times & if gets the right match it will exit from the loop
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
# my $counter=0;
# while ( $counter < 5 )											# You have 5 attemps to test
#	{
#	print "You have [", (5 - $counter), "] attempts left, ";
#	print "Please enter your keyword : ";
#	chomp(my $key_word=<STDIN>);
#	if ( $key_word eq "test" )
#		{
#		print "Success : You have enterd a correct keyword \n";
#		last													# This will exit from the loop.
#		}
#	else
#		{
#		print "Failed : You have entered a wrong keyword, Try again \n";
#		}
#	$counter++;
#	}
# }
#
 
# * next - To go to next iteration of the program *
# If you want to skip the rest of the processing of the body on the current iteration, but don.t want to exit the loop, you can use next to immediately go
# execute the next iteration of the loop by testing the expression.
#
# Example : below program will use next, when next gets executed it will skip executing remaing portion of the loop re-itreate it from current loop.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
# my $counter=0;
# while ( $counter < 5 )                                      	        # You have 5 attemps to test
#	{
#	print "You have [", (5 - $counter), "] attempts left, ";
#	print "Please enter your keyword : ";
#	chomp(my $key_word=<STDIN>);
#	if ( $key_word eq "" )
#		{
#		print "Warning : You didn't given any entry \n";
#		next;															# This will re-iterate the loop if the user entry is blank, [Check counter to see the diff]
#		print "This line will not be printing since next re-iterate the loop";
#		}
#	elsif ( $key_word eq "test" )
#        {
#        print "Success : You have enterd a correct keyword \n";
#        last;                                                           # here when the condition meets it re-itreate the program from current counter
#        print "This will not be displayed, since last will terminate the loop";
#        }
#	else
#    	{
#    	print "Failed : You have entered a wrong keyword, Try again \n";
#    	}
#	$counter++;
#	}
# }
#

# * redo - reexecuting the loop *
# On rare occasions, you.ll want to go back to the top of the loop, but without testing the condition (in the case of a for or while loop) or getting 
# the next element in the list (as in a for or while loop). If you feel you need to do this, the keyword to use is redo
#
# Example : below example will re-execute the loop when the condition failed
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
# my $counter=0;
# while ( $counter < 5 )                                                # You have 5 attemps to test
#   {
#   print "You have [", (5 - $counter), "] attempts left, ";
#   print "Please enter your keyword : ";
#   chomp(my $key_word=<STDIN>);
#   if ( $key_word eq "" )
#       {
#       print "Warning : You didn't given any entry \n";
#       #next;                                                           # This will re-iterate the loop if the user entry is blank, [Check counter to see the diff]
#       #print "This line will not be printing since next re-iterate the loop";
#       }
#   elsif ( $key_word eq "test" )
#        {
#        print "Success : You have enterd a correct keyword \n";
#        last;                                                           # here when the condition meets it re-itreate the program from current counter
#        print "This will not be displayed, since last will terminate the loop";
#        }
#   else
#       {
#       print "Failed : You have entered a wrong keyword, Try again \n";
#       redo;															# This will re-execute the loop if the entry is failed
#	   print "This line will not be printed \n";						# This line will not be printed.
#       }
#   $counter++;
#   }
# }
#
# * NOTE : The big difference between next and redo is that next will advance to the next iteration, but redo will redo the current iteration *

# * Labelling loops *
# By default last, next & redo operates only on the inntermost loop. To overcome this incase you have to skip from parent loop there is mechanism called as 
# "labelling". Using this method you can call the last together with the label to escape from that parent loop itself. "Label" can be defined by any name follows ":"
# Like say we take name as master then while start of the loop we should mention as "MASTER:" and later when you are calling along with keywords use name without ":"
# See below example for more details.
#
# Example : Below example shows we label the "for" loop using "PARENT:" & it will be called later using "last PARENT" which will help to terminate the for loop itself.
#		  : In case you didn't use the lebelling here this will re-iterate the for loop till satisfies the condition inside "for" loop.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# PARENT: for (my $i=0; $i < 5; $i++)						# here defined a label for "for" loop with name "PARENT:"
#	{
#	my $j=10;
#	while ( $j > 5 )
#		{
#		print "Value of \$i=$i \n value of \$j=$j \n";		# Terminating "for" loop itself by calling label along with last as "last PARENT", here ":" not used.
#		last PARENT if $j == 7;
#		$j--;
#		}
#	} 

# ** Functions learned in CHAPTER 3 **
#
# defined : This function is used to to check a variable is defined or it is undefined
# next 	  : This takes the loop into its next iteration
# redo	  : This re-itrerate the current loop 
# last 	  : This will break out of the loop
#
#


#*************************************************************************************************************************************************
#																																				 #
#											*** CHAPTER 4 - Lists and Array ***																	 #
#																																				 #
#*************************************************************************************************************************************************
#
#
# In this chapter we will discuss more about lists & array, also how this can be used in perl for various purpose.
#

# * List * 
# It is considared as single unit even though it is made up of sevaral number of values. 
# in perl values inside list are considared as scalars rather than strings. They stored in the order as they appear in the list
# List is denoted as elements inside closed paranthesis like, ( element0, elements1, element2, etc.. )
# as like any programming langauage perl start counting the element from 0 (zero) in a list
# Below are examples of "lists"
#
# () 				- This is a simple list. Simple list that doesn't contain any elements in the list.
# (42) 				- This list has only one element which is a number "43"
# (MILK)			- This list has only one element which is a string "MILK"
# (43, MILK)		- This list consisit of two elements one is numaric "43" and another element is string "MILK"
#
# NOTE : print() function treats its arguments as list & the magic about "print ()" is if needed we can omit paranthesis ().
#	   : See below example to understand what it means.
#
# Example : Below statements are equal & both will print the result as '43, MILK'
#
# print "43, MILK \n";
# print ("43, MILK \n");		# here 0th element is 43, 1st element is MILK & second element is "\n"
#
# Example : Below statement will print elemnts without any spaces because perl will print as it sees. 
#
# print (123, 456, 789);		# here output seen is "123456789" & this is how perl reads a list
# print ("123, 456, 789");		# here output seen is "123, 456, 789", Since it is marked in double qouates.


# * More Complex list 
# Single list can hod both numbers, strings & variables together, see below example for more details
#
# Example : Below program contains number, string & variables.
#
# #!/usr/bin/perl
# use warnings;
# use strict; 
#
# my $brand="Fair price";
# print ("I am going to Super Market in (Pasirris), To get (2 Litres) of Milk 
#		& its brand is $brand \n");
#
# NOTE : Like this when we have long strings we can print that in multiple lines of the same list


# * Using () in list 
# When you use any number of paranthesis() inside a list all those list coming inside will losses its identity & only outermost list will taken in account
# That means if you write lists with any number if () inside all are same single outermost list 
#
# Example : All below list are treated as same 
#
# print (3, 4, 5, 6);		# Given result "3456"
# print ((3, 4), 5 ,6);		# Given result "3456"
# print (3, 4, (5, 6));		# Given result "3456"
# print ((3, 4), (5, 6));	# Given result "3456"
#
# print ('one', 'two', 'three', 'four');	# Gives result "onetwothreefour"
# print (('one', 'two', 'three', 'four'));	# Gives result "onetwothreefour"
# print ('one', ('two', 'three'), 'four');	# Gives result "onetwothreefour"
# print (('one','two'), ('three', 'four'));	# Gives result "onetwothreefour"
#
# * Creating list easily with "qw//" *
# "qw//" is similar to "qq or q" as learn before. "qw" stands for 'quote word'
# "qw//" will help to easily create a list. This wll take all items which comes in between the slashes incldung the whitespace, which doesn't happen with ().
#
# Example : Here one list is written with "qw//" & also shows another example with how this normally written with paranthesis.
#
# print qw/This is very easy/;	# This creates ('This ' 'is ' 'very ' 'easy)


# * Ranges 
# we can use list to simplify a perticular group of elements which follows a pattern, for example serial number, english alphabets etc...
# using ranges rather than wring (1, 2, 3, 4, 5) we can write the list as (1 .. 5)
# also we can write (a, b, c, d, e, f, g, h) as (a .. h)
#
# Examples : Here is few examples of list using ranges 
#
# print (1 .. 10);			# This will print numbers from 1 to 10 as 12345678910
# print (-5 .. +5);			# This will print numbers from -5 to +5 as "-5-4-3-2-1012345"
# print ('a' .. 'h');		# This will print letters as abcdefgh
#
# NOTE : While printing letters please ranges as mentioned above, quotes as must for letters


# * Accessing values inside a list
# we have seen many ways to build up a list, but not sure how access one particular element in a list
# You can access one particular element in an array using calling the number of that element with in square bracket, like [no]
#
# Example : below example calls an element with in an array 
#
# #!/usr/bin/perl
# use warnings;
# use strict;
# {
# print ((1 ..10) [5]);		# here output printed will be 6, wonder ?. because perl calculates the counter from 0 so here the element comes in 5th place is 6
# print (qw/SALT VINAGER SUGAR SPINACH POTOTO/ [3], "\n");		# Here "SPINACH" is the one listed, we used "qw//" simplify the loop 
# }
#
# Example : Below is another example is to list month, here we are calling a variable using standard input.
#
# #!/usr/bin/perl
# use warnings;
# use strict;
# {
# print "which month you want to print : ";
# chomp(my $month_number=<STDIN>);
# print (qw(January February March April May June July August September October November December)[$month_number]);
# }	
# 

# * Array *
# Variable which used to store a list is called as an array. if the variable is represented by "$" then an array is represented by a "@" symbol
# Like scalars arrays must be declared with "my ()" if we are using strict. 
# The same rule of variable applies for array also in naming conventions, it should start with a alphabet or undersquare followed by more alphabets or numerics or undersquare.
#
# For example : Here we are listing the members of an array. 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# my @house_members;
# @house_members = qw(ajay appu shuppu Tuplu);
# print "@house_members[0..3] \n";			# Here result printed will be "ajay appu shuppu Tuplu"
#
# Note : Setting up a array variable with @ (@house_members) and scalar variable ($house_members) are different
#		 We can see below example & understand what we mean by this.
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# my @house_members;
# my $house_members;
# @house_members = qw(Ajay, Appu, Shuppu, Tuplu); 
# $house_members = 10; 
# print (@house_members, "\n");						# This will print the result as "Ajay,Appu,Shuppu,Tuplu"
# print ($house_members, "\n");						# This will print the result as "10", since we declared this as a scalar variable 
# print ($#house_members, "\n");					# This will print the position of the last variable.

# * Finding total number of elements in an array 
# When you assign a array into scalar variable it stores the total number of elements in that array. 
# That means if you print @week_days from below example that will give the names of the days in a week. 
# If you assign arry  @week_days to a variable $total_days that will give the total number of element in an array, i.e is "7"
# You can get the total number of elements in an array by priting array with a function scalar, i.e print (scalar @week_days, \n); will give the result as 7
# There is another menthod for getting position of the last element in an array i.e $#week_days, it will print the result as 6, since the elements starts from "0".
#
# Example : Here we are going to create couple of array & assign them to a variable, lets see what it gives 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#	{
#	my @week_days;
#	my $total_days;
#	@week_days=qw(Sunday Monday Tuesday Wednesday Thursday Firday Saturday);				# This will store the elements in an array
#	$total_days=@week_days;																	# This will store the number of elements (count) in an array
#	print "\n Days in a week are - @week_days \n Total number of days is $total_days \n";
#	print (scalar @week_days, "\n");														# This is another way to print the total elements in an array
#	}
#
#	{
#	my @food;
#	my $total_food;
#	@food=qw(Breakfast Lunch Snacks Dinner);												# This will store the elements in an array
#	$total_food=@food;																		# This will store the number of elements (count) in an array
#	print "\n Food I have in a day is @food \n Total food I have is $total_food \n";	
#	print (scalar @food, "\n");																# This is another way to print the total elements in an array
#	}
#
# Note : When you assign an array inside double quotes " " then print command will read the spaces also used while declaring the array. 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict; 
#
#	{
#	no warnings;									# This is to remove the warnings created in the following line.
#	my @car_models;
#	@car_models = qw(nissan, volvo, tata, honda);
#	print (@car_models, "\n");						# This will not read spaces betwwen elements & prints output as "nissan,volvo,tata,honda"
#	print "@car_models, \n";						# This will read spaces between elements & prints output as "nissan, volvo, tata, honda"
#	}

# * Adding to an Array *
# To add an element to an array one method we can use is flattering the array, also there are various other built in functions available to do this task. which we will see later.
# Flattering the array will treat the arry only as a list & it is not the best way to add elements into the array.
#
# Example : Below example add elements to array using the flattering an array method.
#
# #/usr/bin/perl
# 
# use warnings;
# use strict; 
#
#	{
#	my @array_one;
#	my @array_two;
#	my @array_three;
#	@array_one = (1, 2, 3, 4, 5);						# Here we are assiging elements to array one, make sure we are not using "qw ()" when we are doing this.
#	@array_two = (@array_one, 6, 7, 8, 9, 10);			# Here we adding the elements of "@array_one" into @array_two
#	@array_three = @array_two;							# Here we are doing an multiple assignement by assigning all elements of "@array_two" to "@array_three"
#	print "Array one is : @array_one \n";
#	print "Array two is : @array_two \n";
#	print "Array three is : @array_three \n";
#	}

# * Accessing single element in an array * 
# We can access the a value of an array using "array name" & followed by the by the position of the element in square bracket.
# i.e if you want to call the 3rd element of an array, then you should call as $array_name[3]
# Note : When we are calling single element in an array then we won't use "@" symbol with array, intead of that we uses "$" symbol
#	   : More over over as we said above @array_name & $array_name are considared to be two different variables in perl, $array_name[x] will consider as part of the array. 
#	   : If you don't use the square bracket & call the element then it makes a different sense in using it.
#
# Example :  Below example tell us about how to call single elements in an array
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#	{
#	my @days_in_week;
#	@days_in_week=qw(Sunday Monday Tuesday Wednesday Thursday Friday Saturday);
#	print "Holidays in a week are $days_in_week[6] & $days_in_week[0] \n";			# This will print the result as "Holidays in a week are Saturday & Sunday"
#	print "Total days in a week are "; 
#	print (scalar @days_in_week, "\n");												# Together above two lines will print the o/p as "Total days in a week are 7"
#	}

# * $# array * (Page 99) 
# For any given array, if you want to get the index value of the the last element in an array then you can use "$#array_name"
# i.e, if the array name is @test_array then you can get the index of the last element by "$#test_array".
# Note : This can give you only the index of the last element in an array, not the value. To get the value of the last element you can use "$test_array[$#test_array]".
#
# Example : Below program will print both the index number and value of the last element in an array. 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#	{
#	my @week_days;
#	@week_days=qw(Monday Tuesday Wednesday Thursday Friday);
#	print ("Index of the last element in array is : ", $#week_days, "\n");				# Here output is "Index of the last element in array is : 4"
#	print ("Value of the last element in array is : ", $week_days[$#week_days], "\n");	# Here output is "Value of the last element in array is : Friday"
#	}

# * Looping through multiple elements in an array *
# When you know the first index of the array is "0" and the last index of the element is "$#", then you can loop through complete array. 
# This looping can be used for various tasks associed with the values of that array. 
# Looping can be done using for, while & foreach loops.
#
# Example : Below example goes through the array using while loop.
#
# #!/usr/bin/perl
# 
# use warnings;
# use strict;
#
#	{
#	my @array_input;
#	@array_input=qw(Ajay Appu Shuppu Tuplu);
#	my $array_index=0;
#	my $array_length=$#array_input;
#	while ( $array_index <= $#array_input )
#		{
#		print "array Index is : $array_index & ";
#		print "value on this Index is : $array_input[$array_index] \n";  # This print output as "array Index is : 0 & value on this Index is : Ajay", this will continue till last element. 
#		$array_index++;
#		}
#	}
#
# Example : Same program written above is re-written using "for loop"
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#	{
#	my @array_input;
#	@array_input=qw(Ajay1 Appu Shuppu Tuplu);
#	my $array_length=$#array_input;
#	for ( my $array_index=0; $array_index <= $array_length ; $array_index++ )
#		{	
#		print "array Index is : $array_index & ";
#		print "value on this Index is : $array_input[$array_index] \n"; #  This print output as "array Index is : 0 & value on this Index is : Ajay", this will continue till last element.
#		}
#	}
 
# * Accessing multiple elements in an array * 
# We are access mutiple elements in array with the "array slice" concept.
# Using this concept we can access the values of the array using multiple index numbers separated by commas or using ranges. 
# Note : when we uses multiple elements in an array we need to use "@array[x..y]" as array name instead of "$array[x]" which we used to access single element of an array.
# 
# Example : Below example gives us an idea about array slicing
#
# #!/usr/bin/perl
#
# use warnigs;
# use strict;
#
#	{
#	my @week=qw(Sunday Monday Tuesday Wednesday Thursday Firday Saturday);
#	print "Working days in a week are @week[1..5] \n";						# here output is "Working days in a week are Monday Tuesday Wednesday Thursday Firday"
#	print "Weekends are @week[0,6] \n";										# here output is "Weekends are Sunday Saturday"
#	print "Church Day is $week[0] \n";										# here output is "Church Day is Sunday"
#	}
#
# Note : On above example we used "@week[..]" for printing multiple elements & "$week[.]" to print single element.

# * foreach - loop in array *
# In case we want to process a certain list of commands or body of logics / commands then we can use "foreach" loop to achieve the same. 
# foeach will help us to process through every element or array 
#
# Syntax : foreach scalar_variable (@array / list) 
#				{ 
#				body of the loop 
#				}
# 
# Example : Below is an example to use array with foreach loop
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#	{
#	my @week;
#	my $day;
#	my $count = 1;
#	@week = qw(Sunday Monday Tuesday Wednesday Thursday Firday Saturday);
#	foreach $day (@week)
#		{
#		print "Day $count is : $day \n";
#		$count++;
#		}
#	} 	
#
# Note : Same program can be modified as shorter below
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#	{
#	my $count = 1;
#	my @week = qw(Sunday Monday Tuesday Wednesday Thursday Firday Saturday);
#	foreach my $day (@week)
#		{
#		print "Day $count is : $day \n";
#		$count++;
#		}
#	}
#
# Note : We can modify the program even shorter as below.
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#	{
#	my $count = 1;
#	foreach my $day qw(Sunday Monday Tuesday Wednesday Thursday Firday Saturday)
#		{
#		print "Day $count is : $day \n";
#      	$count++;
#      	}
#   }
#
# * Expression modifier for "foreach" loop *
# we can write foreach loop using expression modifier as follows. 
# 
# Syntax : statement foreach (list / Array)
#
# Example : See an example written using 'expression modifier' for foreach
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#	{
#	my @week = qw(Sunday Monday Tuesday Wednesday Thursday Firday Saturday) ;
#	print "[$_] \n" foreach @week  ;											# here we are using the default variable as scalar variable & which helps in expression modification.
#	}

# * Array Functions *
# Array functions are set of builtin finctions which we can use in an array. There are few function explained below.
# 
# * reverse () function * 
# Reverse function is used to count the numbers in reverse order, this function can be used in both arrays & lists.
#
# Example : Below example count the elements of an array in reverse order and printing it.
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my @purchase_list = qw(
#			rice
#			vegitables
#			fish
#			grocery
#			juice
#			chocolates
#			yogurt
#		);
#	foreach my $puchase_item ( reverse(@purchase_list[0..3]) ) {		# Here we are reading only first 4 elements of the array 
#		print "Item to purchase is : $puchase_item \n";					# Result printed will be : grocery fish vegitables rice
#		}
# }

# * pop () & push () functions
# We already came to know about to how to add an element to an array in a straight forward method & method is as follows. 
# Syntax -  @array = (@array, $scalar)   # for a stright formward method with any array
# using this method we can keep elements into an array. pop () & push () are the methods used to achieve the same but in a more smarter way. 
# 
# Note :  stack (meaning : a pile of objects, typically one that is neatly arranged in a storage), for example : peper tray
#
# pop  () - This function is used to take out the last element of an array stack, the one taken out will be the last element in an array
# Syntax :  pop (@array)
#
# push () - This function is used to insert an element into array stack, the one inserted will be the last element
# Syntax : push (@array, $element_to_add1, element_to_add2)
#
# When an element is added or removed  in an array that will be permenantly removed from the array stack while execution.
# When you can take out an element then you can store that element into a scalar variable for further usage if needed.
# Incase you don't want the elements to be stored then you can overwrite that value with another (simple concept of scalar)
#
# Note : incase you want to insert or remove the first element then use the reverse function along with it.
#
# Example : An example exaplins about push () & pop ().
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {	
#	my $right_hand;
#	my $left_hand;
#	my @paper_tray = qw(
#			study_book
#			offer_letter
#			utility_bill
#			braodband_bill
#			notepad
#		);
#	$right_hand = pop (@paper_tray);																		# last element 'notepad' will be taken out & will be stored in $right_hand
#	print "Taking the last element [$right_hand]  of stack in right_hand using pop () & the value is  : $right_hand \n";  	# here output printed will be 'notepad'
#	print "Current array elements available are \"Paper tray\" : [ @paper_tray ] \n\n";						# here output printed will be [ study_book offer_letter utility_bill braodband_bill ]
#
#	$right_hand = pop (@paper_tray);																		# here $right_hand overwritten by new element & value 'notepad' lost for ever. 
#	print "Taking the last element of stack in right_hand using pop () & the value is  : $right_hand \n";	# here the last element removed & printed is : braodband_bill
#	print "Current array elements available are \"Paper tray\" : [ @paper_tray ] \n\n";						# here output printed will be [ study_book offer_letter utility_bill ]
#	
#	$left_hand = pop (@paper_tray);																			# here $left_hand will store 'utility_bill' & no element will be lost since new sclar variable used.
#	print "Taking the another element from an array in left_hand  using pop () & value is : $left_hand \n";	# here the last element removed & printed is : 'utility_bill'
#	print "Current array elements available are \"Paper tray\" : [ @paper_tray ] \n\n"; 					# Current array elements are [ study_book offer_letter ]
#
#	push (@paper_tray, $right_hand,  $left_hand);															# here 'braodband_bill' & 'utility_bill' will stored back in array stack.
#	print "Element in right_hand & left_hand are kept it back, current tray is : [ @paper_tray ] \n\n";     # output is [ study_book offer_letter braodband_bill utility_bill ]
# }

# * shift() and unshift() functions 
# When pop & push functions deal with the last element in a stcak or an array, these shift & unshift works with the bottom / starting of a stack or an array.
# This works exactly same as pop & push at the bottom layer.
# 
# shift  : This function is used to take out the first element of an array stack, the one taken out will be the first element in an array
# Syntax : shift (@array_name)
#
# unshift : This function is used to insert an element into array stack, element inserted will be the first element in the array
# syntax  : unshift (@array_name, $element_to_add1, element_to_add2)
# 
# Example : An example explains about the shift and unshift in an array
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $right_hand;
#	my $left_hand;
#	my @paper_tray= qw (
#			study_book
#			offer_letter
#			utility_bill
#			braodband_bill
#			notepad
#		);
#	$left_hand = shift (@paper_tray);																		# First element 'study_book' will be taken out & will be stored in $left_hand
#	print "Taking the first element [$left_hand]  out of the stack in left hand using shift () & the value is $left_hand \n";
#	print "Current array elements available are \"Paper tray\" : [ @paper_tray ] \n\n";						# here output printed will be [ offer_letter utility_bill braodband_bill notepad ]
#
#	$left_hand = shift (@paper_tray);																		# here $left_hand overwritten by new element & value 'study_book'  lost for ever.
#	print "Taking the first element out of the stack in left hand using shift () & the value is $left_hand \n";
#	print "Current array elements available are \"Paper tray\" : [ @paper_tray ] \n\n";						# here output printed will be [ utility_bill braodband_bill notepad ]
#
#	$right_hand = shift (@paper_tray);																		# here $right_hand will store  utility_bill & no element will be lost since new sclar variable used.
#	print "Taking the first element out of the stack in right hand using shift () & the value is $right_hand \n";
#	print "Current array elements available are \"Paper tray\" : [ @paper_tray ] \n\n";						# Current array elements are [ study_book offer_letter ]
#
#	unshift (@paper_tray, $left_hand, $right_hand);															# here 'offer_letter' and 'utility_bill' will stored back in array stack.
#	print "Element in right_hand & left_hand are kept it back, current tray is : [ @paper_tray ] \n\n"; 	# output is [ offer_letter utility_bill braodband_bill notepad ]
# }

# * sort () function (Page : 113) 
# Sort function used to sort elements in an array. 
# sorting primerly used for alphabetical and string sorting, how ever perl provides the functionality to sort numerics with the help of sort defualt variables & special operator.
# $a and $b are the default variables used in sort which will help us for numeric sorting. Special operator used is '<=>' 
#
# METHOD 1 : Alphabet or string sorting 
# Alphabets or string can be sorted via the sort function as explained in the example 
#
# Example : Below example shows the aphabetical sorting
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {	
#	my @unsorted_array = qw (
#			zeebra
#			ball
#			orange
#			grapes
#			ice
#			van
#			apple
#			x_ray
#		);
#	my @sorted_array = sort @unsorted_array;
#	print "Elements before sortning array is [@unsorted_array] \n";			# here output printed will be [zebra ball orange grapes ice van apple x_ray]
#	print "Elements after sorting array is [@sorted_array] \n";				# here output printed will be [apple ball grapes ice orange van x_ray zebra]
# }	

# METHOD 2 : Numeric sort
# Since 'perl' does the 'ASCII' sort by dafualt it gives it can't sort the numerical values only with the 'sort' function
# So we will use two special variable called '$a' & '$b' with the help of special operator '<=>'
#
# Syntax : sort { $a <=> $b } @array_name 	--> Ascending 
#		 : sort { $b <=> $a } @array_name   --> Descending 
#
# NOTE :  Here $a & $b are the inbuild variables provided by Perl sort () finction
#
# Example : sorting numerical vlue & explains various sort
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my @unsorted_array = qw ( 22 98 51 6 8 1 3 );
#	my @ascii_sort = sort @unsorted_array;
#	my @ascending_array = sort { $a <=> $b } @unsorted_array;
#	my @descending_array = sort {$b <=> $a } @unsorted_array;
#	print "String or ASCII sorted array [ @ascii_sort ] \n";				# here output printed will be [ 1 22 3 51 6 8 98 ]
#	print "Ascending sort array [ @ascending_array ] \n";					# here output printed will be [ 1 3 6 8 22 51 98 ]
#	print "Descending sort array [ @descending_array ] \n";					# here output printed will be [ 98 51 22 8 6 3 1 ]
# }
#
# * delete () function *
# This function can be used to delete one value from any part of the array using the 'index number'
# 
# Syntax :  delete $array_name[indx_no];
#
#
# * exist () function *
# This function will return a value if the condition is true
# i.e. if a value exist in an array it will print the result which we are looking for else it won't
#
# Syntax : if exist($array_name[index_number]);
#
# Example : An example showing the usage for both delete()
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my @hotel_list = qw(
#			KFC
#			SUBWAY
#			TEXAS
#			MCDonald
#			ANJAPPAR
#			);																		# Defining an array 

#	my $total_hotel = $#hotel_list;													# getting the last index number for that array
#	for (my $i=0; $i <= $total_hotel; $i++)
#		{
#		print "$i. $hotel_list[$i] \n";
#		};																			# Prinitng array elements till the last index number
#	print "Enter which Hotel You want to remove from the list [0..$total_hotel] : ";
#	chomp(my $user_selection=<STDIN>);												# reading a user selection as input
#	if ( $user_selection > $total_hotel)
#		{
#		die "Wrong Selection : You can select only between [0..$total_hotel]";		# die with an error message
#		}
#	print "\nYou have selcted $hotel_list[$user_selection]!!!\n\n";					# Showing the selection
#	delete ($hotel_list[$user_selection]);											# deleting selected element
#	my $return_value = qx(echo $?);													# reading the return value
#	if ( $return_value == 0 )
#		{
#		print "Success : Selected Item removed !!!\n";
#		}	
#	else
#		{
#		die "Failed to remove selected Item !!!";
#		};																			# printing according to the retun code
#	print "\nDo You want to re-check the item is removed or not (Y / N) : ";		# an option option to re-check the delected element
#	chomp(my $verify = <STDIN>);													
#	if ( $verify eq "Y" )
#		{
#		if (exists ($hotel_list[$user_selection]))									# Checking the existance of that element using 'exists' function
#			{
#			print "\nItem is not removed!!!\n";
#			}
#		else
#			{
#			print "\nItem is removed already!!!\n";
#			}
#		}			
# }

# **  Function Learned in Chapter 4** 
#
# reverse	: For converting an array into reverse order 
# push 		: For inserting a last element in an array
# pop		: For Removing a last lest element in an array
# shift		: For removing first element in an array
# unshift	: For removing last element in an array
# sort		: For sorting elements in an array 
# delete	: For deleting array content using index number
#
# ** Spciale Operator learned **
#
# <=> 		: This is used to sort the numerical values with the help of sort function.
#


#*************************************************************************************************************************************************
#																																				 #
#							***** Chapter 5 - Hash Variables *****																				 #			
#																																				 #
#*************************************************************************************************************************************************
#
#
# * Hash variables * 
# Hash variables are pair of data which is not regularly arranged & it is scattered around the hash.
# In case of hash variable there will be a 'key/name' or a 'value' will be associated with it.
# Scalar varabale represented with '$scalar', array represnted with '@array' like that a hash variable is represented with '%hash'
# Phone book can be normally termed as hash variable, where names are the key and number associated it will be value.

# * How to declare a hash variable 
# Hash variables are in pairs and they has two part, one which comes in the 'left' hand side is the 'key' and the one which comes in 'right' hand side is 'value'
# Hash variable can be represented in two methods, one is with special operator '=>' which we will use later and another one is without operator
# '=>' operator normally replaces one comma(,) and quotes(" ") of the key which comes in the left hand side,
#
# Note : hash key must be unique and there shouldn't be any duplicate for it, in case any exist second will overwrite the first value
#	   : For the values there can be duplicate & no issues with it.
#
# Example : Below is an example for a hash variable (without operator)
#
# {
#	my %home_location (
#			"Ajay"		, "Pasirris",					# here key value is represented as "ajay", which can be wrtitten as ajay => with operator
#			"Anu"		, "Telok Blangah",
#			"Bharatt"	, "Hougang",
#			"Sanil"		, "Pasir Panjang"
#		);
# }
#
# Example : More advanced way of representing it with '=>' operator
#
# {
#	my %home_location (
#			Ajay		=> "Pasirris",					# here with operator no double quotes or comma used for key ajay
#			Anu			=> "Telok Blangah",
#			Bharatt		=> "Hougang",
#			Sanil 		=> "Pasir Panjang"
#		);
# }

# * Converting an 'array to hash' & 'hash to array' 
# Since represeting a hash is also similar to how we represent array (list based method), we can easily convert an array to hash and hash to array. 
#
# Note : when an array is coverting to hash it should have even number of elements in it.
#
# Syntax (array assigned to hash) : %hash = @array;
# Syntax (hash assigned to array) : @array = %hash;
#
# Example : Converting an array to hash 
# 
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my @test_array = qw (
#		"Ajay"      , "Pasirris", 
#        "Anu"       , "Telok Blangah",
#        "Bharatt"   , "Hougang",
#        "Sanil"     , "Pasir Panjang"
#		);
#	print "Element of [test_array] : \{  @test_array \} \n";
#	
#	print ('Converting test_array to %hash_variable', "\n");
#	my %test_hash = @test_array ;
#	print ('converted hash variable [test_hash] is :', %test_hash, "\n");
# }
#
# Note 	: Be careful when converting an array to hash variable, because hash variables don't have a specific order it will place the values anywhere. 
# 		: When converting an array to hash the ordering will not be guaranteed.
#		: But assigning one hash to another hash can be done & it will provide proper oerdering, i.e %hash1 = %hash2;

# * Working with hash values
# To lookup a value in hash we something similar to array index, here we uses a name {key} instead of index number and curl braces {} instead of []. 
#
# Syntax : $hash_variable{hash_key}		# Like we seen in array for getting single value we uses scalar variable sign '$'.
#
# Example : How to call values for few keys in hash variable. 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict; 
#
# {
#	my %location_details = (
#		Ajay	=> "Pasir Ris",
#		Anu 	=> "Telok Blangah",
#		Bharatt	=> "Hougang",
#		Sanil	=> "Pasir Panjang"
#		);
#	print ("Mr : Ajay lives in One of the town called \t\t: ", $location_details{Ajay}, "\n");
#	print ("Mr : Sanil lives in one of the Main City called \t: ", $location_details{Sanil}, "\n");
#	print ("Mr : Bharatt lives in a very distant place called \t: ", $location_details{Bharatt}, "\n");
#	print ("Mr : Anu lives in a very beautiful place called \t: ", $location_details{Anu}, "\n");
# }

# * Adding removing and modifying values to hash variable 
# 
# Adding  	: To add a value into hash variable you can just assign a key & it curresponding value. 
# Syntax  	: $hash_variable_name{key} = "Value";
# Example 	: $location_details{Ramesh} = "Bukit Merah";
#
# Removing 	: To remove a value from hash variable you can just use a function called 'delete()'
# Syntax 	: delete ($hash_variable_name{key});
# Example	: delete ($location_details{Sanil});
#
# Modifying : To modify a values in an existing hash variable just update the key with the new value 
# Syntax 	: $hash_variable_name{key} = "new_value";
# Example	: $location_details{Anu} = "Changi";
#
# Example : An example which explains about add, remove & modify in a hash variable
#
# #!/usr/bin/perl
# 
# use warings;
# use strict;
#
# {
#  my %location_details = (
#       Ajay    => "Pasir Ris",
#       Anu     => "Telok Blangah",
#       Bharatt => "Hougang",
#       Sanil   => "Pasir Panjang"
#       );
#	
#	# Modifying hash variable values below 
#	delete $location_details{Ajay};					# Removed Ajay from location
#	$location_details{Ramesh} = "Bukit Merah";  	# Adding Ramesh to hash variable "%location_details"
#	$location_details{Anu} = "Changi";				# Reassigned the value for "Anu"
#
#	# printing Modified hash variable values below
#	print "Ajay is removed from the [loation_details]\nCurrent available data is \n",  %location_details, "\n";
#	print "New memeber Ramesh's Location is : ", $location_details{Ramesh}, "\n";
#	print "Anu now relocated to \t\t : ", $location_details{Anu}, "\n";
# }
#
#
# * Functions in hash *
# There are various functions provided in hash such as keys(), values(), each(), delete() & exists(). We need to use them according to the usage. 
# Each function is exaplained in detail below

# * Keys () Function 
# This function is used to get the list of key values in a hash variable, When you are getting the result it may not be order since hashes don't guarentee any order. 
#
# Syntax : keys (%hash-name);
#
# Example : An example to print the key values in a hash variable 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my %location_details = (
#		Ajay	=> "Pasir Ris",
#		Anu		=> "Hrbr Frnt",
#		Bharatt	=> "Hougang",
#		Ramesh	=> "Bukit Merah"
#		);
#	print ("Keys in a Hash variable \%location_details are ", keys(%location_details), "\n"); # Here the result printed will be 'AnuBharattAjayRamesh'
#	
#	# printing details using foreach 
#	
#	foreach my $key_name (keys (%location_details))
#		{
#		print "Mr : $key_name Lives in \t:\t", $location_details{$key_name}, "\n"; # This gives a result like 'Mr : Anu Lives in       :       Hrbr Frnt' & other keys and values similarly
#		}
# }
#
 
# * values () Function *
# Like Keys function values() will help us to get the values in a hash variable. 
#
# Note 	: using values () function in various controll statements & loop is not a good pratcice since there can be multiple values with the same name for various keys. 
#		: This is always a good practive that use keys() when we use hash with the control statements and loops.	
#
# Syntax :  values (%hash-name);
#
# Example : Below example demonstrate the usage of values () 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# {
#	my %location_details = (
#		Ajay    => "Pasir Ris",
#		Anu     => "Hrbr Frnt",
#		Bharatt => "Hougang",
#		Ramesh  => "Bukit Merah"
#		);
#	print ("Values in hash variable \%location_details are : ", values (%location_details), "\n");
#	
#	foreach (values (%location_details))
#		{
#		print ("Someone Lives in \t:\t $_ \n");
#		}
# }

# * each () Function * (page 123)
# This function helps to fetch the values as each (key, value) pair from a hash variable. To understand how it fetches, please look at the synatx 
#
# Syntax : ($a, $b) = each (%hash_variable);
#
# Example : Below example illustrates about the usage of each () function
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
#	my ($a, $b);
#	my %location_details = (
#		Ajay	=>	"Pasir Ris",
#		Anu		=>	"Telok Blangah",
#		Bharatt	=>	"Hougang",
#		Ramesh	=>	"Bukit Mehra",
#		Sanil	=>	"Pasir Panjang"
#		);
#
#	while (($a, $b) = each (%location_details))
#		{
#		print  "Mr : $a lives in a place called $b \n";		# This will print result like below "Mr : Anu lives in a place called Telok Blangah" & rest of the entries
#		}
# }

# * delete() function * (Page : 123)
# This function will delete one pair of key/value in a hash variable. 
# 
# Syntax : delete $hash_name{key};
#
# Example : Below example tells us about how to delete a pair from a hash variable
#
# #!/usr/bin/perl
# 
# use warnings;
# use strict;
#
# {	
# 	my %location_details = (
# 		Ajay		=> "Pasir Ris",
#		Anu			=> "Telok Blangah",
#		Bharatt		=> "Hougang Central",
#		Sanil		=> "Pasir Panjang",
#		Ramesh		=> "Bukit Mehra"	
#		);
#	delete ($location_details{Ajay});			# This will delete the pair for Ajay from the variable
#	my $exit_status = qx(echo $?);
#	if ($exit_status != 0)	
#		{
#		print "Data Removed for \"Ajay\" successfully from hash variable \%location_details \n\n";
#		}
#	else
#		{
#		die "There is an error encounter while deleting Ajay from hash variable \%location_details \n\n";	
#		}
#	print "Current available data is \n";
#	foreach my $key_name (keys (%location_details)) 
#		{
#		print ("Mr : $key_name lives in ", values(%location_details), "\n");	
#		}
# }
#

# * exists () - function *
# This function will help to return the result if the condition exist or f it is a true value, 
# i.e if the value exist in a hash variable then it return true else false.
#
# syntax : if exists (%hash_name{key_name});
#
# Example : Below example shows about the usage of exist () function
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my %location_details = (
#			Ajay	=>	"Pasir Ris",
#			Saravan => 	"Telok Blangah"
#			);
#	print "Data for Ajay is available in \%location_details\n", if exists ($location_details{Ajay});		# This o/p will be printed since it is true 
#	print "Data for Sunil is available in  \%location_details\n", if exists ($location_details{Sunil});		$ This won't be printing since it is not true 
# }
#

# ** Functions learned ** 
#
# Keys ()		: This function is used to get the list of key values in a hash variable 
# values ()		: This will help us to get the values in a hash variable
# delete () 	: This function can be used to delete the keys & values from a hash variable
# each ()		: This function can be used to get the pair of values, need to use two variable while using this function [Syntax : ($a, $b) = each (%hash_variable);]
# exists ()		: This function will retrun the result if the value is true
#



# ** Special operator learned **
#
# => 		: This is used to pair between the key and value in a hash variable, also this automatically assigns " ", for the key which placed in the left side.


#*************************************************************************************************************************************************
#																																				 #
#							***** Chapter 6 - Functions OR Subroutines *****																	 #			
#																																				 #
#*************************************************************************************************************************************************
#
# * Functions or Subroutines *
# Function or subroutine both means the same, this normally called as functions or subroutine or subs, all means the same
# It is used to define a set of process with enough logic & use the same program again & again when needed.
# This is similar to we use the perl inbuilt functions to do certian tasks. Likewise we can create a function & call it any time needed.
#
# Advantages :
# There are various advantages by using functions to write program, such as easy management & will be easy to locate & fix script globally
# By using functions effectievely we can reduce the number of lines of programs.
# same functions can be reused for various similar tasks
#
# When to use :
# According to the application we can use functions any where, few example are given below 
# 1. Same data need to be processed every time 
# 2. In case you need to verify the return code of set of commands in a program
# 3. Check some specific file or DIR in complete program
# 4. Printing similar header or footer on the same program
# 5. etc .... end less applications :)
# 
# * How to define a subroutine *
# See below example to understand about how to define a sub-routine
#
# 	sub example_function {
#    	"insert some code with logic & commands"
#	}
#
# There are three main areas for defining a function or sub-routine
# 1) Keyword 'sub' 
# 2) Name we are going to give for this function or sub-routine [naming rules are similar to what we seen for variables)
# 3) List of program enclosed within curl braces {} 
#
# Note 	: In perl program language $variable, @variable, %variable & variable() all has different meaning according to their usage.
#		: There is no hard and fast rule for defining a function name, you can choose the name as effective one according to its usage. 
#		: There is no need to mention semi-colon once after the function is defined.
# 
# Example : Few examples of naming a function or sub-routine
# 			currency_converter()
#			retrun_code_check()
#			check_files()
#			copy_files()
#			download_files()

# * How to invoke or call a function *
# Lets say as we define a subroute as "sub example_function { ..... }" , Then it can be called as below 
# 
# example_function;											# This way you cab call a subroutine but only after defining it.
# example_function();										# This way you can call a function before or after defining it. 
# example_function(argument1, argument2, argument3, ...)	# This way you can call a function in case there are aruments need to be paased. 
#
# Note	: Incase we need to pass argument along with the function then that neeed to be closed with in the 'paranthesis()'.
#		: When you invoke or call a function you need to mention 'semi-colon;' after that
#
# Example : Below example will tell us how to define and call a function
#
# #!/usr/bin/perl
# 
# use warnings;
# use strict;
#
# {
#	sub version {
#		chomp (my $perl_version = qx(perl -v|awk '/This is perl/ {print \$4}'));
#		print "From here we are starting $perl_version with \[function support\]. \n";
#		}																					# Defining a subroutine				
#
#	print "Do you want to Print the current version of Perl (y/n) : ";						# Taking an input to match the condition
#	chomp(my $option = <STDIN>);
#	version() if ($option eq "y"  or  $option eq "yes");									# executing the subroutine once after the condition met, used expr modifier.
#	print "Hello world. \n";
# }
#
# * order of declaring subroutines & invoking them * 
# There are multiple method you can call a function,
# i.e. before defining them or after defining them, but there are slight difference in using it which explained below
 
# * METHOD 1 : Call first & define later [ with paranthesis () ]
# Using this method a function can be called intially before defining it, in this case you must use 'paranthesis()' along with function when you are calling.
# 
# Example : Here we are calling a function before it actually defined. 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# 
# {
# family();																# Calling subroutine named 'family' with paranthesis before defining it
#																		 
# sub family {															# defining the subroutine or function here 
#	my @family_memebrs = qw (
#		TUPLU
#		SHUPPU
#		APPU
#		AJAY
#		);
#	my $total_members = @family_memebrs;
#	my $i=1;
#	while ( $i <= $total_members ) {									# using a while loop to print
#		print "$i Memeber of the family is : $family_memebrs[($i-1)] \n";
#		$i++;
#		}
#	hello_wrold ();														# Calling another subroutine within subroutine or function wth () since defined later.
#	}
#
#	sub hello_wrold () {
#		print "\nHello world !!!\n";
#	}
# }
#
# Note : when called function 'without paranthesis()', it is given an error as "Bareword "family" not allowed while "strict subs" in use at begin.pl line 2153."

# * METHOD 2 : Define first & call later [ without paranthesis() ]
# This method allows you more flexibility since you don't need to use paranthesis after defining this the function.
# 
# Example : Below example will tell you how to call function after defining it.
#
# #!/usr/bin/perl
# 
# use warings;
# use strict;
#
# {
# sub hello_world {													# definig function 'hello_world'
#	print "\nHello World !!!\n";
#	}
#
# sub family {														# defining function 'family'
#	my @family_members = qw(
#		TUPLU
#		SHUPPU
#		APPU
#		AJAY
#		);
#	my $memeber_no=1;
#	foreach my $memeber (@family_members) {							# using foreach to print the function
#		print "$memeber_no memeber of the family is : $memeber\n";
#		$memeber_no++;
#		}
#	hello_world;													# calling another function with in the function without (), since it defined earlier.
#	}
#
# family															# calling subroutine with out 'paranthesis()' since it defined earlier
# }

# * METHOD 3 - Using keyword 'sub' and [ without using paranthesis() ]
# Using this method you can define a function with key word 'sub' followed by function & semicolon, i.e. "sub example_function;".
# Once you define this in the very begining then perl knows this is a function which may be explained below. 
# Another advantage of this method is when you call this function any part of the program, you don't need to use 'paranthesis()' along wit it.
#
# Example : Below example explains about defining a function with keyword 'sub'
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
# sub hello_world;													# Defining The functions in beginning with 'sub' so you don't need to use 'paranthesis()'
# sub family;														# ^
#
# family;															# Calling a function without 'paranthsisi()'
#
# sub family {														# Defining function only after calling it
#  my @family_members = qw(
#       TUPLU
#       SHUPPU
#       APPU
#       );
#	push (@family_members, "AJAY");
#	my $total_memebrs=$#family_members;
#	for (my $i=0; $i <= $total_memebrs; $i++) {
#		print "$i memeber of the family is : $family_members[$i]\n";
#		}
#	hello_world;
#	}
#
# sub hello_world {													# Defining function only after calling it 
#	print "\nHellow World !!!\n";
#	}
# }

# * Passing argument to functions * 
# We can passs argument to a function, this is just like passing argument to a perl buit in function. 
# using this method you passs any number of variable to a function & you can achive the result according to what written in the program. 
#
# Syntax : function_name (arg1, arg2, arg3, arg3, etc..)
#
# Example : Below example tells us how to pass arguments to a function.
# 
# #!/usr/bin/perl
#
# use warnings;
# use strict; 
#	{
#	calculation (10, 100, 1000, 10000);					# Calling function with defined arguments
#	calculation (1 .. 1000);							# Calling function with a range of arguments 
#	
#	sub calculation {									# defining a function
#		my $total=0;
#		foreach $_ (@_) {								# reading element of array using special variable to store, also argument is stored in special array variable
#			$total=$total + $_;							# Calculating the complete value through 'foreach' loop for complete list of arguments
#			}
#		print "Total value calculated is : $total \n";	# Pritning the total array value.
#		}
#	}

# * Method to pass argument to an array
# It is always depend which method to be used to passs argument to a function, according to our requirement we can use several method
#
# Method 1 : Calling using 'foreach' or similar loops 
# This method can be used according to usages such as we seen above, normally applicable to where a range of arguments are passed.
# also like in situations where same operations need to be performed in all arguents passed.
#
# Example : See the last example mentioned, which tell us about how to call arguments using 'foreach' function
#
# Method 2 : Calling values using shift() or pop() like function
# This is applicable when there is a definte number of elements are passed & also the input is very limites. 
# This can be used even with huge number of arguments, but there it will be bit tedeus.
#
# Example : Below example tells us how to call arguments passed to a function using shift().
# 
# #!/usr/bin/perl
# 
# use warnings;
# use strict;
#
# {
#	add (10, 9);								# Passing two arguments to a function named 'add' & it is called outside the group
#	
#	{
#	sub add {									# defining subrotine named 'add'
#		my $arg1 - shift @_;					# storing left most value (now 10) stored in special array vaiable '@_' to variable '$arg1'
#		my $arg2 = shift;						# storing left most value (now  9) stored in special array variable '@_' to variable '$arg2'
#		my $total = $arg1 + $arg2;
#		print "Total Value is : $total \n";
#		}
#	}
# }
#
# Method 3 : Assigning arguments directly to variable 
# This can be used when you are already aware how many arguments are going to be passed & to which variable that will be stored. 
# 
# Example : Below example is reading the arguments directly into variable 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	add (10, 15);								# Passing two arguments to function add
#	{
#		sub add {
#			my ($arg1, $arg2) = @_;				# Storing (arg1 & arg2) with the values stored default array variable '@_', makesure use '()' when defining variable
#			my $total = $arg1 + $arg2;
#			print "Total value is : $total \n";
#			}
#	}
# }	
#
#
# * Returning a value *
# < This chapter is pending for Study>

#
# * Tips from this chapter *

# "version() if ($option eq "y"  or  $option eq "yes");" 	-	 An expression modifier to call a sub-routine "version()" along with if condition, also note 'or'
# "shift" & "shift @_" - These two are same, this means it will take out the last element of the special array variable, @_ can be used to store input to a function

# * Functions learned in this chapter *
#


#*************************************************************************************************************************************************
#																																				 #
#										 **** CHAPTER 7 - Regular Expressions (Regex) ******															 #	
#																																				 #
#*************************************************************************************************************************************************
#
# * What is Regular expressions * 
# The term regular expressions refers to a perticular 'pattern', a pattern can be a word or sequance of charectors follwing a set of rules or syntax.
# Rules and syntax are explained more below. 'regex' is not only limited with perl shell utilities such as sed & egrep also uses uses certain rules for patterns.
# So far we know how to check for a value against a scalar variable or an element in an array or a value / key in a hash table. 
# But 'regular expression' will help us in checking a certian pattern in our complete data. 
# For example we can say check whether all sentences are starting with Capital letter, or how many times a specific word is repeated in a complete data etc. 
# These kind of analysis can be performed by 'Regular expression'.
#
# Regular expression is a very big chapter & it is devided again into various other small portions.
#
# 1. Basic Patterns
# 2. Special Charectors to use
# 3. Quantifiers, anchors & memorizing patterns.
# 4. Matching, substituting and transforming text using patterns
# 5. Backtracking
# 6. Quick looks at some simple pitfalls 

# * 1. Basic Patterns *
# Simplest pattern is a word, or a simple sequance of charectors, how to process a pattern is explained in below example 
#
# * How to  check - Match a pattern 
# To match a pattern you can use regex as '/<pattern>/', i.e any pattern to find must be enclosed with in slashes "/ /" and checked with an if condition
# Synax :  	if ($scalar =~ /pattern/) { body }  		# If the sclar variable is not the default one
# 			if ($_ =~ /pattern/) { body } 				# Along with the default variable
# 			if (/pattern/) { body } 					# Default variable will understood by perl without mentioning the true operator
#
# See below examples to understand how to use this.
#
# Example 1 : (Non regex method to find) Below example search for a pttern in a sentece with help of split function & then provides result if the pattern is found 
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
#	my $counter=0;
#	$_ = "Hellow every one our family members are Appu, Shuppu and Tuplu";
#	foreach my $word (split) {
#		#print "$word \n";
#		if ($word eq "family") {
#			$counter = 1;
#			last;
#		}
#	}
#
#	if ($counter) {
#		print "SUCCESS : We found word \"family\" on the given statement\n";
#	}
# }
#
# Note : The above method is a normal method & it is too messy this can be rewritten with the help of regex as below 
#
# Example 2 : (Regex method) Below example will help to find a pattern with the help of regex
#
# #!/usr/bin/perl
#
#  use warings;
#  use strict;
#
# {
#	$_ = "Hellow every one our family members are Appu, Shuppu and Tuplu";			# Reading the satement into a scalar variable (default variable)
#		if ($_ =~ /family/ ) {														# Find a word within default variable, '/family/' is the regex used to find & operator '=~' will return '1' if it is successful
#			print "SUCCESS : We found word \"family\" on the given statement\n";
#		}
# }
#
# Note 	: Any word to find will be placed inside the slashes, i.e for above example ' /family/ ' is the regex used to find a word in scalar variable
#		: Also the operator used above is "=~", this will retun a value of '1' if the find is successful.
#
# Example 3 : (Regex method with 'advantage' of 'default variable') This will give an example of how to shorten a program with regex & default variable
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="Hellow every one our family members are Appu, Shuppu and Tuplu";
#	if (/family/) {																# Finding pattern using regex '/family/', '=~' didn't mentioned since it is deault variable & perl knows this is expected
#		print "SUCCESS : We found word \"family\" on the given statement\n";
#	}	
# }
#
# Note : If you are looking for a pettern with in the default variable '$_', then you don't have to use '=~' to check, perl knows this by dafult & it will check via regex & return true value if matches.

# * How to check - not mataching a pttern  (page : 155)
# To Check whether a pattern is not matching, then you can either use 'unless' or 'if' along with 'slash enclosed pattern' i.e. '/<pattern>/', See details below
#
#
# unless :  if you are using 'unless' to check pattern then use ' =~ ' as operator, if the variable is stored in default vaiable $_, then you can use it as 
# Syntax :  unless (/patten/) { body }  				# Along with the default variable
# 			unless ($scalar =~ /pattern/) { body } 		# when we are using a specific scalar variable
#
#
# if 	 : Incase you using 'if' condition to validate whether the pattern is not matching then you need to use ' ~! ' as operator 
# syntax : if ($scalar !~ /pattern/) { body }			# Here operator ' ~! ' will help to execute the body of the condition if the condition goes false	
#		   if ($_ !~ /pattern/)	{ body }				# In case not macthing, even with default variable you need operator ' ~! '
#
#
# Example 1 : (default variable method) Below example will check & print if the pattern is not found
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {	
#	$_="Hellow every one our family members are Appu, Shuppu and Tuplu";
#	unless (/Nakshatra/) {													# Default variable doesn't neeed oprator "=~"
#		print "Information : Nakshatra is not part of family \n";
#	}
# }
#
# Example 2 : Reading a scalar variable 
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	user_check () ;																	# Calling it as a subroutine
#	
# 	{
#	sub user_check {																# Defining subroutine
#		print "Please Enter user name to check database [username] :";
#		chomp (my $user_name = <STDIN>);											
#		my $user_db = "ajay, appu, shuppu, tuplu";									
#		unless ($user_db =~ /$user_name/) {											# This will provide true value if the condition is not true
#			print "Not found :  user : $user_name not found in the database \n";
#			};
#		}
#	}
# }
#
#
# if		: if you are using 'if' to check the pattern then use ' !~ ' as operator, this give value '1' or true value if it can't find the pattern 
# Syntax 	: if ($scalar !~ /pattern/) { body }
#
# Exampe : Below Example will check for a pattern & print if not macthing 
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="Hellow every one our family members are Appu, Shuppu and Tuplu";
#	if ($_ !~ /Nakshatra/) {
#		print "Information : Nakshatra is not part of family \n";
#		}
# }
#
# Page 156
#
# Note : When you search for a pattern with multiple words or spaces or commas then make sure you are using the complete pattern 
#
# Example : Below example tells about how to search for a much more complex pattern
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
# $_="Hello Mr:Ajay, You are trying to test a pattern here ?";					# Reading a sentence into default variable 
#	{
#		if (/Mr:Ajay,/) {														# Trying to find for a pattern "Mr:Ajay," , this will be true 
#			print "Yes, we found Mr:Ajay in the given senetence\n";
#			}
#		else
#	 		{
#			print "No, Unable to find Mr:Ajay in the given senetence\n";
#			}
#		if (/ trying/) {
#			print "Yes :we found \" trying\" in the given sentence\n";
#			}
#		else
#			{
#			print "No : we didn't find \" trying\" in the given sentence\n";	
#			}
#		if (/ Ajay/) {															# Trying to find a pattern " Ajay", this will be false only "Ajay" is there not " Ajay"
#			print "Yes, we found \"Ajay\"in the given senetence\n";
#			}
#		else
#			{
#			print "No, Unable to find \"Ajay\"in the given senetence\n";
#			}
#	
#		if (/you/i) {															# Trying to find a pattern "you" in the sentence & it wil pick "You" since the search is used with 'i'	
#			print "Yes, we found \"You\" in the given senetence\n";
#			}
#		else
#			{
#			print "No, Unable to find \"You\" in the given senetence\n";
#			}
#	}	
# }

# * What is the difference between (/patten/) & (/pattern/i)
# (/patten/)	-	This will search for only case sensitive pattern, ie if you serach for /test/, it can't pick 'Test' since it is case senisitive
# (/pattern/i)	-	This search is non case insensitive, it need to only match the word or string case can be any, i.e if you look for '(/test/i)' it can pick Test, tEst, TEST, TESt etc..

# * Interpolation 
# This means we can store a pattern or a set f patterns in a variable & exactly what get matched will execute the program, pattern you don't have to hard coded
#
# Example : Below example exaplains interpolation, i.e it reads the data from user input & matches the data 
# 
# #!/usr/bin/perl
# 
# use warnings;
# use strict;
# 
# {
#	print "Please Enter the search pattern : ";
#	chomp(my $pattern = <STDIN>);										# Reading the pattern to search from the user input
#	$_="Good morning, today was good day & able to study something";	# Here we are storing a sentence in to variable & later it will be used to search
#	if (/$pattern/i) {													# checking for pattern & it goes to true if it matches the condition, if false it follows the else condition
#		print "Success : Able to match [$pattern] in [$_] \n";
#	} else {
#		print "Sorry : Couldn't find the [pattern] in [ $_ ]";
#	}
# }

# * Metacharectors and Escape sequences
# There will be cases when we will search for strings with the special charectors, on those occassions we need to use the escape sequance to turn off the special meaning of those charectors. 
# By default perl assumes below spcial charectors with their special meaning, those charectors with special meaning is called 'metacharectors'
# Those special charectors (metacharectors) are : ' $ # { } & % ^ ~ ( ) \ . ? * +' 
# To trunoff the special meaning of these metacharectors we need to use the 'escape sequance', see below syntax to understand about the usage 
#
# Note : Except the above mentioned metacharectors all other charectors doesn't require any escape sequance, they will be treated literally
# 
# Syntax : /\<meta charetcor>/   or   /\Q$pattern\E/  || example : /\Q$input\E/
# here 	 : Two formward slash ' / /' are used to check for the pattern 
# 		 : \Q will switch off the special meaning of the pattern if it contains any metacharectors & it will contniue till it gets closed with \E.
#
# Example : Below example will give an idea about how to turn off the metacharectors with their special meaning
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# { 
#	$_=q(Hello, I was studying in +2 during 2010 - 2012);
#	if (/\Q+2\E during/) {													# Here + will treated as literal with any special meaning since we used '/\Q+2\E/', this could also written as '/\+2/'
#		print "Success : able to match [+2 during] under [$_] \n";
#	} else {
#		print "Sorry : Couldn't match [+2 during] under [$_] \n";
#	}
# }
#
 
# * Anchors 
# Anchors are used to help us to search for a pattern if it is at the begin of a statement or at the end of the statement.
# This will be useful in situation where you are looking for a pattern only at the begin of the string or at the end of the string & no need to search throughout the string.
# There are two main 'anchors' used 
#
# ^	: This will help to search for a pattern at the begin of the string 
# syntax : if /^begin_pattern/		# This will help to find the pattern at the begin of the string
#
# $ : This will help to search for a pattern at the end of the string
# syntax : if /end_pattern$/ 		# This will look for a pattern at the end of the string
#
# Example 1 : Below program illustrate the usage of anchors
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="\*Our family is beautiful & we are 4 members :";
#
#	if (/^\*our/i) {
#		print "Success : we found the word [Our] at the begin of statement\n";				# This will be true condition here 
#	} else {
#		print "Failed : Unable to find the word [Our] at the begin of statementi\n";
#	}
#	
#	if (/:$/i) {
#		print "Success : we are able to find smily [:)] at the end of statement\n";			# This will be the true condition here 
#	} else {
#
#		print "Failed : we are unable to find simley [:)] at the end of statement\n";
#	}
#
#
#    if (/"\*our$/i) {
#        print "Success : we found the word [Our] at the begin of statement\n";
#    } else {
#        print "Failed : Unable to find the word [Our] at the begin of statementi\n";		# This will be the true condition here 
#    }
#
#    if (/^:/i) {
#        print "Success : we are able to find smily [:)] at the end of statement\n";
#    } else {
#        print "Failed : we are unable to find simley [:)] at the end of statement\n";		# This will be the true condition here 
#    }
#
# }
#
# Example 2 : Another program illustrate about anchors reading from file
#
# #!/usr/bin/perl
#
# use warnings;
# use atrict;
#
# {
#	my $syllable = "Aum";				# This pattern we are going to use for search
#	
#	while (<>) {						# This '<>' will look for a input file which passed along with script, else will ask for standard input
#		if (/^$syllable/) {
#			print "$_ ";				# This will be printed if the condition is true
#		}
#	}	
# }
#
# NOTE : For above program we may need to give an imput file like "perl begin.pl /tmp/pattern" or standard input to process
#
# * Shortcuts and options *
# These are some tricks which we can use to search for a pattern in a string, rather than just directly search for the pattern, see below for more understanding.

# * character classes *
# When you want to search for a pattern with set of charectors or range of characters rather then just an individual character, then you can use 'character classes'
# To use 'character classes' you need to mention the pattern with in a square bracket, i.e [abc] or [a-z] or [0-9] etc.
#
# Eample : Below example explains about the charector classes
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="New Jurasic park movie is getting released & it is Jurasic World Version 4.0";
#	
#	if (/^N[eo]w/i) {																		# This will look for pattern 'New | Now' in given string
#		print "Success : we are able to find [New|Now] at begin of string [ $_ ] \n";		# True condition here 
#	} else {
#		print "Failed : we are unable to find [New|Now] at begin of string [ $_ ] \n";
#	}
#
#	if (/[A-Z]urasic/) {																					# This will match with 'Jurasic' from the string
#		print "Success : we are able to find a word similar to i( [A-Z]urasic ) in string  [ $_ ] \n";		# True condition here 
#	} else {
#		print "failed : we are unble to find a word similar to i( [A-Z]urasic ) in string  [ $_ ] \n";
#	}
#
#	if (/[1-9].1$/) {																		# This will look for version like 1.1 or 2.1 or 3.1 or 4.1 .... 9.1
#		print "Success : we are able to find version at the end of the string [$_] \n";
#	} else {
#		print "Failed : we are unable to match version at the end of the string [$_] \n";   # True condition since the version of the string is 4.0
#	}
# }
#
# NOTE : Some character classes are going to come up again and again: digits, word characters, and the various types of whitespace. Perl provides some neat shortcuts for these. 

# * Shortcuts
# Below are the shortcuts available in perl
#
# Below table lists the most common shortcuts and what they represent
# Shortcut		Expansion		Description
#	\d			  [0-9]			Digits 0 to 9
#	\w		   [0-9A-Za-z_]		A “word” character (allowable, for example, in a Perl variable name
#	\s 		   [ \t\n\r\f] 		A whitespace character—that is, a space, tab, newline, carriage return
#
# Below table lists the corresponding negative forms of the shortcuts
# Shortcut		Expansion		Description
#  \D 			 [^0-9] 		Any nondigit
#  \W 		  [^0-9A-Za-z_] 	Any non“word” character
#  \S 		  [^ \t\n\r\f] 		Any non-whitespace character
#
# Example : below example explains the usage of shortcuts
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
#	my $item = "diaper";
#	my $price = "50 \$";
#	my $advertisement = "4 $item is only 50 \$";
#
#	if ( $item =~ /\w\w\w\w\w\w/ ) {														# This condition will match with a 5 letter word 'diaper'
#		print "Found : We are able to locate an item in store & it is [$item] \n";		
#		}
#	
#	if ( $price =~ /\$$/ ) {
#		print "Doller : Item price is mentioned in the dollers [\$] \n";					# This will make sure last latter is ending with '$'
#		}
#
#	if ( $advertisement =~ /^\d/ ) {
#		print "Quatnity : Yes the quantity is mentioned in the advertisement \n";			# This will chck for first letter of the statement starts with a digit'
#		} 
#
#	if ( $advertisement =! /\w$/ ) {														# This will check whether the last condition is not ending with a word character.
#		print "Info : advertise is not ending with [INR] \n";
#		}
# }

# * Word Bounadries 
# 
# 1. How to match word or letters which comes in first, last, middle or followed by metacharectors
#
# Words or charectors are not always comes between two spaces, but there will be scenarios wuch as a word or a charector can come at the start or at end or in middle followed by some metacharector etc..
# To match those patterns perl provides something called as 'word boundaries' or '\b'. 
# 
# Syntax : /\b<word or charector>\b/
# 
# Example : Below example will help to match a pattern which is followed by a metacharector
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="***I am Tony' is good new Malayalam movie***";				# here "I" will be matching by eliminating the ' *** ' which is infront of it with the help of word boundaries
#	if (/\b\w\b/) {
#		print "able to match Single letter in : $_\n";
#	}	
#
#	$_="We can see (Cars | Bikes) in showroom";
#	if (/\b\w\w\w\w\b/) {											# here cars will be matching by eleminating metacharector ' ( ' which is infront of cars with help of boundaries
#		print "able to match four letter word in : $_ \n";
#	}
# }
#
# 2. How to match word or letters which follows a certain pettern (See second example on page 163)
#
# ====> Update here 
#
# * Alternatives 
# To validate either or condition while matching a pttern per regex provides a special metacharector  " | "
#
# 1. To match two patterns you can use below syntax & example for referance
# 
# Syntax : /<pattern_1> | <pattern_2>/
#
# Example : Below example check for eithr 'Orange' or 'Apple' or 'Plum' in a provided array
#
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
#	my @fruit_basket = qw (	
#		Apple
#		Grapes
#		Orange 
#		Carrot
#		Cocunut
#		Pear
#		Plum
#		);																# An array @fruit_basket containing friuts as its elements
#	my $iteration=0;
#	my $array_length=@fruit_basket;										# calculating the array length 
#	while ( $iteration < $array_length ) {
#		if ($fruit_basket[$iteration] =~ /apple|orange|plum/i) {		# matching for either apple or orange or plum for the currebt element picked from array (@fruit_basket[$iteration])
#			print "Matched : Match found as either [Apple | Orange | plum] The Result matched is \: \[$fruit_basket[$iteration]\] \n";
#		} else {
#			print "No match found & current fruit name is : \[$fruit_basket[$iteration]\] \n";
#		}
#	$iteration++;
#	}
#  }
#
# Note : With the help of regex on above example we saved lot of lines & extra work, else we could have written '3 if condition' or '1 if with two else condition' was required to satisfy the match.
#
# 2. To match two patterns which has something in common, use below syntax & example for reference
#
# Syntax :  common_pattern(Remaining_pattern1|Remaining_pattern2)
#
# Example : Below example matches a few patterns which are common and remaining different
#
# #!/usr/bin/perl
#
# use warnings;
# use strict
#
# {
#	my @pro_verbs = qw(
#			where_there_is_a_will_there_is_a_way
#			The_pen_is_mightier_than_the_sword
#			When_in_Rome_do_as_the_Romans
#			Better_late_than_never
#			Falling_down_is_not_defeat_defeat_is_not_when_you_are_getting_up
#			);
#	foreach my $statement (@pro_verbs) {
#			if ($statement =~ /whe(re|n)/i) {							# here regex used as /whe(re|n)/, this exactly seach for 'where or 'when', here paranthesis is the key
#				print "Match Found [Where|When] : \"$statement\" \n";
#			} else {
#				print "No Match for [Where|When]: \"$statement\" \n";
#			}
#	}
# }
#
# Note  : In case of pattern which has few similar pattern, then their remaining pattern must kept with in ' ( )'  with the '|' opertaor 
#	 	: In case you didn't used the (re|n), then perl might have though this as 'where|n', which is not the one we exepcted.

# 3. More complex patterns 
# 
# Few complex possible patterns are given below 
#
# Example : Few complex petterns to understand the capability of pattern
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# { 
# 	match_text ();									# Running with a subroutine
# 
#	sub match_text {
#		my %dictionary = (							# declaring a hash variable called 'dictionary'
#				when  => "time",
#				where => "place",
#				who	  => "person",
#				what  => "object",
#				job   => "work",
#			   'jo '   => "name",
#				jos  => "person"
#				);	
#		my ($key_name, $value_name);				i										# dealaring variable to use the 'each' function
#		while (($key_name, $value_name) = each (%dictionary)) {								# Calling each key & values in that hash 
#				if ( $key_name =~ /wh[a-z]|jo(\s|[a-z])/i ) {								# complex search pattern includes almost almost all key in the hash
#					print "Dictionary refers \"$key_name\"\t\=\>\t$value_name \n";
#				} else {
#					print "Given key $key_name is not part if the search patten \n";
#				}
#			}	
#		}
# }
#

# * Repetition with Quantifiers 
# < Note :  Study this later with the help of Bharatt (To do) >
#	
# ****** Regex metacharector Summary table ********
#
# Below Summary table explains what metacharector can be used aginst various regular expression operations.
#
#--------------------------------------------------------------------------------------------------------------------------------------------
# Metacharector 					Description
#------------------------------------------------------------------------------------------------------------------------------------------
# 	[abc]			-		Any one of the charector a, b or c 
#   [^abc]			-		Any one charector other than a, b or c 
#   [a-z]			-		Any one ascii lower case character from lower case a to z
#   \d \D			-		a digit, a non digit
#   \w \W			-		a word character, a non word character
#	\s \S			-		a white space character, a on white space character 
#	\b				-		boundary between a word character and non word character
#	.				-		any character except new line
#	(abc)			-		The phrase abc as a group
# 	?				-		The preceeding character or group may or may not be present (may be present 0 or 1 time)
#	+				-		The preceeding character or group may be present 1 or more than one time
#	*				-		Preceeding character or group may be present 0 or more time
# 	(x, y}			-		Preceeding character or group must be between 'x' and 'y' times (i.e minimum 'x' time & maximum 'y' times)
# 	{x,}			-		Preceeding character or group must be minimum x times (atleast 'x' time)
# 	{x}				-		Precceding character or group must be present 'x' times
#--------------------------------------------------------------------------------------------------------------------------------------------
#
# Note :  Go through the example on Page 168 (To do)

# * How regular expression engine works * on Page 169 (To do)

# * Working with regex * 
# So far we learned how searh for a pattern or match a pattern etc, but we didn't gone through what action we can perform based on the advantages of 'regular expression'
# There are three main usage of regex explained below 
#
# 1. Match a regular expression (equal to grep) - m/<search_filed>/
# 2. Substitution (Seach & replace) 			- s/<search_field>/<replace_field>/
# 3. Transliterate Regular Expression 			- tr/<search_filed/<transalte_field>/
#
# To understand more about this we need to know about the '$number' variable (i.e $1, $2, $3, $4 ... etc ) provided by perl regex & also how to "search for a pttern" (i.e =~ or !~)
#
# * Search for a pattern - as we learned earlier we can perform the action based on the match was successful
# To perform an operation when search is true syntax is 	: if ($string_var =~ /search_pattern/) { action }
# To perform an operation when search is not true syntax is : if ($string_var !~ //search_pattern/) { action }
#
# * '$number' variable (i.e $1, $2, $3, $4 etc) provided by perl regex - These variables are used to store the last successful regular expression.
# i.e when perl is able to match one regex in a set of string, then the first match will be stored in $1, second match will store $2, third match will store in $3 & go on.
#
# Example : below example tell us about the combined usage of 'search pattern' & 'number variable' usage 
#
# #!/usr/bin/perl
# 
# use warnings;
# use strict;
#
# {
#    my $text = "the quick brown fox jumps over the lazy dog.";
#    $text =~ m/ ((\w{5})?) /;
#    print "$1 \n";                                                  # output is "quick"
#
# }

# * 1. Match a regular expression (equal to grep) *
# This is a way to match a regular expression when we are processing a string, this can be 
#
# Example : This will example will explain the usage of matching regular expression
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# {
#	my $text = "the quick brown fox jumps over the lazy dog.";
#	$text =~ m/ ((\w{5})?) /;				
# 	print "$1 \n";													# output is "quick"
# }

# * 2. Substitution (Seach & replace) *
# This is the way to search & replace any charector in perl.
# To do this you need to search for a pattern first & then it can be replaced with desired word or number or string etc. 
# Substitution has mainly three parts, i.e  /s/<search_field>/<replace_field>/, here search filed is the place where we can mention our regex & it will be replaed when it gets matched.
# When we do substitution there are various way to do it, please see the examples below
#
# non-global : In this method search & replace will be done on the very first occurence & will not be performed on the every occurence.
#
# Syntax : s/<search_field>/<replace_field>/
#
# Example : Below example will tell us about how to serach & replac the first occurence 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="Apple tree is a very good play school, but there is no tree as Apple";			# storing a sentence into default variable
#	s/\w{5}/Orange/;																	# replacing a '\w{5}' (i.e word which has five letters) which is Apple here & will be replaced with it first occurence
#	print "$_ \n";																		# Output printed will be : "Orange tree is a very good play school, but there is no tree as Apple"
# }
#
# global  : In this method 'search & replace' will be done for the 'search field' on its 'every occurence'. 
#
# Syntax : s/<search_field>/<replace_field>/g
#
# Example : Below example will tell us about how to match & replace a word in its every occurence 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$_="Apple tree is a very good play school, but there is no tree as Apple";	# storing a sentence into default variable
#	s/([A-Z][a-z]+)/Orange/g; 	# replacing '([A-Z][a-z]+)' (i.e word starts with capital letter & followed by small letter)i.e Apple will replace with Orange in every occurence wich we used '\g\' 
#	print "$_ \n";																# output will be : "Orange tree is a very good play school, but there is no tree as Orange"
# }

# * 3. Transliterate Regular Expression (To do later) *
#
# < Note : This is note covred in book, need to study later > 

# * Changing delimeters *
# As like we used 'q// and qq//' here also we can use laternate delimeters when processing regular expression. 
# There are certails rulues we need to followed for that, please see those rules for both 'mathing' & 'substituting' a pattern below 
#
# 1. Matching pattern - For mathing pattern we can change the syntax from "/<$string variable> =~ <search pattern>/" can be rewritten as "m//<$string variable> =~ <search pattern>/"
# 					 Here we can use any other non-word delimeter also for use when we use 'm' to declare, so perl will understand following is a regular expression.
# Few examples 	1 :	 m{<$string variable> =~ <search pattern>}
#				2 :	 m#<$string variable> =~ <search pattern>#
#				3 :	 m$<$string variable> =~ <search pattern>$
#				4 :	 m[<$string variable> =~ <search pattern>]
#
# Example : Following example will help us to understand about alternate delimeter usage for matching a regular expresion
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
#	my $school_register = "Vaiga, Nandu, Eenu";
#	#print "$1 is in classroom \n"	if ($school_register =~ m#(\s[A-F][a-z]+)#); 				 		# Here we are using '#' as delimeter to find 'Eenu'; from above list
#	$school_register =~ m#(\s[A-F][a-z]+)#;
#	print "$1 is in classroom \n";
# }
# 
# 2. Substitution Pattern - When you perform substitution with modified delimeters you need to make sure you are coverung the search & replace pattern (no need of 'm' here)
# Few examples  1 : s{search_pattern}{replace_patternx}g;
#				2 : s{search_pattern}
#				     {replace_pattern}g;	
#
# Example : Below example will tell us about aubstitution with alternate delimeter
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
#	my $inspiring_quote="Falling down is not defeat, defeat is when you are not trying to get up";
#	$inspiring_quote =~ s{(\s[d]\w{5})}{ failure}g;							# here we are substitutig '(\s[d]\w{5})' (i.e defeat) with ' failure'
#	print "$inspiring_quote \n" ;
#
#	my $script_path="/dev/test/testing";
#	$script_path =~ s{\/dev\/test\/testing}{\/dev\/tester\/tested}g; 		# if we don't use '{}' here, it will be too messy
#	print "$script_path \n"; 
# }
#		

# * Modifiers *
# There are few modifier which can be used for string processing in regular expression
#
# /m - This modifier will treat the string as multiple lines, here you can process a string with multiple lines. (new line charector will be accepted when we use /m)
# /s - This modifier will treat the string as single line & it will ignore the new line charector, i.e you can process the string which is in single line only
# /i - This modifier will treat the string as case insensitive
# /g - This modifier will treat changes to the string globally when you perform substitution
# /x - This modifier will allow to use the comments and white spaces within the match.
#
# Example : An example to read a string in a log file which is created with a format 'date time [hostname]' 
#
# #!/usr/bin/perl

# use warnings;
# use strict;
#
# Method 1 : This is the regular expression which we write without any modifiers
# {
#	# #/^([0-2]\d:[0-5]\d:[0-5]\d)\s+\[([^\]]+)\]\s+(.*)$/		
# }
#
# Method 2 :  This regular expression is modified into below format using '\x' modifier, here we are using white space and comments 
# {
#	/
#	^ # Match at the beginning of the string
#	( # First group: time
#		[0-2]\d
#		:
#		[0-5]\d
#		:
#		[0-5]\d
#	)
#	\s+
#	\[ # Square bracket
#		(  # Second group: machine name
#			[^\]]+ # Anything that isn't a square bracket
#		)		
#	\] # End square bracket
#	\s+
#	( # Third group: everything else
#		.*
#	)
#	$ # Finally, match the end of the string
#	/x
# }
#
# Method 3 : Another way to tidy this up is to put each of the groups into variables and interpolate them:
# {
#	my $time_re = '([0-2]\d:[0-5]\d:[0-5]\d)';
#	my $host_re = '\[([^\]]+)\]';
#	my $mess_re = '(.*)';
#	/^$time_re\s+$host_re\s+$mess_re$/;
# }
#

# * split() & join() functions *
#
# * split() - This function is used to 'break up' a string into list of words using the given delimeter
#			 delimeters are purely defined via regular expression & it is mentioned as 'split /regex/, $string_var'
#			 Incase if we don't give any delimeter it will pick 'white spece (\s)' as the default delimeter
#
# Syntax : split /<delimeter>/, $string_var
#		 : split		# This is when use with default variable & white space, it is a modified form of "split /\s/, $_"
#
# Example : Below example will help to split a user field into many parts
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $user_details="vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin";
#	my @user_details= split /:/, $user_details;
#	print "Login name : $user_details[0] \n";
#	print "Login ID   : $user_details[2] \n";
#	print "Login Path : $user_details[5] \n";
# }
#
# * join () - This function is basically the reverse of 'split()' function, here join() will help to 'gluing' the elements of an array with the help of a given delimeter
#
# Syntax : join /<delimeter>/ @array_var
#
# Example : Below example will help to join an array which is already split up.
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $user_details="vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin";
#	my @user_fields= split /:/, $user_details;
#	{	
#		print "Login name : $user_fields[0] \n";
#		print "Login ID   : $user_fields[2] \n";
#		print "Login Path : $user_fields[5] \n";
# 	}
#	{	
#		my $joined_user_details = join '#', @user_fields;
#		print "orginal entry : $user_details\n";
#		print "current entry : $joined_user_details \n";	
#	}
# }
#
#
#------------------------------------------------------------------------------------------------------------------------------------------
#
# * Functions learned in this chapter *
#
# split () - This function will split a sentence or group words into a list & it keeps all 'punctation'. Eg : "Hello how are you?", will be treated as list (hello, how, are, you?), each word will be an element
#
# * special operator *
#
# =~                - This operator retunrs value as "1" if the pattern match is successful.
# !~                - This operator return the value as "1" or true value if pattern not matched.
# while (<>) { .. } - This '<>' will look for a input file which passed along with script, else will ask for standard input, example :  "perl begin.pl /tmp/pattern". here content of '/tmp/pattern, will process.
#
#
#*************************************************************************************************************************************************
#                                                                                                                                                #
#                                        **** CHAPTER 8 - Files and Data ******                                                                  #
#                                                                                                                                                #
#*************************************************************************************************************************************************
#
# We are starting to write real programs now, till now we learn about only reading a user input using '<STDID>' and results are 'pritning' it out on the console 
# Now we will start read from files which stored in a hrd drive and write into files stored in a hard drive with the help of 'filehandlers'

# * Filehandler *
# Filehandler is a variable which is associated with a file, There are mainly two ways of handling file one is an open() function and another one is the close() function.
# File will be used for read or write dependends how we call them.

# * open() function *
# open functions are normally used to open a file to perform an action. When we are opening a file we need to associate that file into a special variable called filehandle.
# 'filehandle' will be always declared in capital letters so that it can get distingushed from keywords.
# 'filehandle' will have maninly three parts which is exaplained below 
# 
# Syntax : open (filehandler, mode, filename); # See below description
# 		   filehandler   - This is the special variable used to associate a file
#		   mode 		 - This means which mode you are trying to access the file, there mainly three modes which explained below read, write & append
#		   filename 	 - This will be the filename you will be accesing to perform some actions.
#
# Example : open (INPUTFILE, < , messages.log);		# This will read 'messages.log' file using filehandler 'INPUTFILE'
#
# Note : There is one more modified way to call a 'open()' function, i.e see below syntax 
#
# Syntax : open (filehandler, 'filename_with_mode');
#
# Example : open (INPUTFILE, '< messages.log');    #  This will read 'messages.log' file using filehandler 'INPUTFILE', but here we used 'read & filename' together 
 
# * Makig 'filehandler or open()' more secure to use
# filehandler will return a true when it is able to access the file & perform the necessory action, else it may return false. 
# Any condition where a file is failed to open & it proceed in executing the remaining steps it will seviour issues, to overcome such scenarios we can use 'die ()' function with special variable '$!'
# 
# Syntax : open (filehandler, 'filename_with_mode') or die "some statement $!";
#
# This wil help to exit the program from the point where 'open ()' function gets failed. 
# '$!' is the special variable which is offered by perl, what it does is it will pass an error message from the system why the file was unable to open 
# most common messages we can expect from '$!' is 'filename not found' or 'permission denied' etc ..
# 
# Example : open(FH, '< address.txt') or die "problem in locating address.txt : $!"
#
# * Three modes of open() function  or opening a file * 
# Filehandler is mainly used for three modes of operation in a file such as read or write or append, details are explained below. 
#
# * Read mode * 
# This is the default mode in perl, this can be used without an operator also. This will help us to read the data from an external program such as file. 
# If it is not able to locate the file or if you don't have permission to open the file then the open() function will fail.
# 
# Syntax : There are mainly three ways to call the filehandler in read mode 
#		 : open(FLE_HANDLER, filename);
#		 : open(FLE_HANDLER, '<', filename);
#		 : open(FLE_HANDLER, '<filename');

# * How process a line which is open with read 
# To process the data which read from a scalar context you can store that into a scalar variable directly or through a while { } loop according the data is single line or multi line
# 
# syntax 1 : $line = $FILE_HANDLER  		[ This method can be applied only when your file has only one line
#
# syntax 2 : while (<$FILE_HANDLER>) {		[ This method can be used when your input file has multiple lines
# 		 		process_the_line
# 		 		}
#
# Example : Below example will try to list the mount points in the system using the read mode & while loop of processing the data from filehandler
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# {
#	my $fstab_file = '/etc/fstab';
#	my $FSTAB;
#	open ($FSTAB, '<', $fstab_file) or die "$fstab_file : $!";	# Here we aee reading '/etc/fstab' with a filehandler $FSTAB
#	while (<$FSTAB>) {											# reading each entry 
#		my @mount_entry = split;								# Splitting each entry with 'space' which stored in $_
#		foreach my $mount_point (@mount_entry) {				# processing the array of entries
#			if ($mount_point =~ /^\/.+/) {						# checking & printing those lines which starts with '^/'
#				print "$mount_point \n";
#				}
#			}
#		}
#	close $FSTAB;												# closing file handler
# }

# * Diamond operator -  Alternate method to read a file from standard input or data as standard input
# using 'diamond operator' combining with a 'while loop' will help you to 'read a file' or 'data(directly)' as standard input 
#
# Syntax : while (<>) {
# 			process_line 
# 			}
#
# Example : below example will tell us how to handle standard input with the help of diamond operator 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	while (<>) {
#		print "Line read is : $_";				# This will print according to the input given either filename or direct input
#		}
# }

# * Write mode *
# if we want to write some data to a file, then we need to open that file in the write mode. 
#
# Note 	: When you open a file in the write mode any content with in the file will be overwritten with new content, that means it starts everying as new 
# 		: So be careful with its usage
#
# syntax : there are two ways to call the open function
#		 : open (FLE_HANDLER, '>', filename)
#		 : open (FLE_HANDLER, '>filename')
#
# Example : Below example will help us to understand about performing write operation using filehandler 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $test_file = '/tmp/test_perl';
#	my $TESTFILE;
#	open ($TESTFILE, '>', $test_file) or die "$test_file : $!";					# Opening filehandler to 'write' into the file 
#	my %family_details = (														# Declaring a hash for testing
#			Father 		=>	"Ajay",
#			Mother		=>	"Aparna",
#			Daughter	=>	"Vaiga",
#			Son			=>	"Rishi"
#			);
#	foreach my $key_name (keys (%family_details)) {								# reacding each keyname in the hash 
#		print $TESTFILE "$key_name\t\t\=>	$family_details{$key_name} \n";		# Writing the output to the file 
#		}
#	close $TESTFILE;															# Closing filehandler
# }

# * Append mode *
# To keep the content of the file remaining & write some new data into the file you need to use the append mode to file handler, this can be done using '>>' 
# 
# syntax : open (FILE_HANDLER, '>>', file_name)
# 		 : open (FILE_HANLDER, '>>file_name)
#
# Example : Below example help us to understand how an append mode will work
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
#   my $test_file = '/tmp/test_perl';
#   my $TESTFILE;
#   open ($TESTFILE, '>>', $test_file) or die "$test_file : $!";                # Opening filehandler to 'append' into the file
#   my %family_details = (                                                      # Declaring a hash for testing
#           Father      =>  "Ajay",
#           Mother      =>  "Aparna",
#           Daughter    =>  "Vaiga",
#           Son         =>  "Rishi"
#           );
#   foreach my $key_name (keys (%family_details)) {                             # reacding each keyname in the hash
#       print $TESTFILE "$key_name\t\t\=>   $family_details{$key_name} \n";     # Writing the output to the file
#       }
#   close $TESTFILE;                                                            # Closing filehandler
# }

# * close () function *
# When you performed all opertaion on the file using open() and filehandler, then it is always a best practice that you can close that filehandler. 
# If don't close there won't be much difference, but perl will perform a auto closure for that file, but it is always considare as a better programming style to 'close () the filehandler' after usage.
#
# Example : below example will show how to open & close a file which is existing & doesn't exitsing.
#
# # !/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
# file_exist();
# file_not_exist();
#
#	sub file_exist {
#		open(RD_MSG, '< /var/log/messages') or die "/var/log/messages : $!";				# This will be a Successful operation since the file exist
#		print "Success : able to read \'/var/log/messages\' \n";
#		close (RD_MSG);
#	}
#
#	sub file_not_exist {
#		open(RD_MSG, '< /var/adm/messages') or die "/var/adm/messages: $!";					# Thsi will give an error message saying the "o such file or directory at begin.pl line 3240."
#		print "Success : able to read \'/var/log/messages\' \n"; 
#		close (RD_MSG);
#		}
# }
#	

# * @ARGV(Magic Array)
# When you are running a script along with few parameters passed into it, then those parameters are stored in special array called '@ARGV'
# When you are using '@ARGV' you don't need to use 'my ' even though you are running script in the 'strict mode', if you use you will loose the magic of this array
#
# Correct Usage 	: @ARGV
# Incorrect Usage 	: my $ARGB (This is wrong)
#
# White space is consider to differentiate between elements in the array when we pass arguments to the script
# We can access the elements in the array using its 'index number' or using 'shift()' function. 
# 'shift(@ARGV)' is the most common method used to access the first elements, every time you do 'shift' it will take out first element at that perticular time.
# 'shift(@ARGV)' can be better written as 'shift', both means same 
#
# synatx : shift(@ARGV)		# This will take out the first element in that array
#		 : shift			# This exactly same as 'shift(@ARGV)' & take out the first element of the array
#
# Example : simple program to print the input given to script 
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
#	my $zeroth_element = shift @ARGV;
#	my $first_element  = shift;
#	my $second_element = shift;
#														# Here when you give input the same input will be printed as output
#	print "zeroth_element is : $zeroth_element \n";
#	print "First element is : $first_element \n";
#	print "Second element is : $second_element \n";
#		
# }

# * @ARGV and <> (Magic array & Diamond operator) *
# @ARGV & <> has a functional relation ship, below explained how this really works
#
# 1. When there is a content in, the n all elements will shift & read until the @ARGV array is empty
# 2. When there is a file input given it will go through the file until the end.  
#
# Note : When you declare @ARGV with in the script, then the content input via command line will be lost
#
# Example : Below is an example which explanins the relation between @ARGV and <> 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	@ARGV = qw(/etc/fstab /etc/sysctl.conf); 		# Here all line will be processed one by one with <> & any input to the script will be ignore 
#	while (<>) {
#		print "Current Entry is $_ \n";
#		}
# }
#
# * $ARGV - how we can use this 
# When every element of the @ARGV is executed via <>, then $ARGV will hold the information which file is currently used 
#
# Example : Below example will help us to understand about $ARGV
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	@ARGV = qw(/etc/fstab /etc/sysctl.conf);
#	while (<>) {
#		print "Current Entry from File $ARGV is : $_ \n";			# Here this will show the filename from which it read the conecnt & then conent as mentioned in print statement.
#		}
# }

# * Buffering (Variable - $|) *
# Before we start explaning this, we will start with a program which will help you in explaining what is this
#
# Example : Below program expected to print 20 lines in 20 seconds
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	foreach (1..20) {				# Here all "."  will be printed together after 20 seonds
#		print ".";
#		sleep 1;
#		}
#	print "\n";
# }
#
# Note : On above example we are expecting to print "." for another 20 seconds leaving an interval of one second, but it doesn't happen in that way & looks like an exception.
# The reason for it doesn't happen in that way is 'Operating system won't often read or write things to the file handler" until the end of line charecter is detected'.
# This is to reduce the short repetetion operations. Instead of that OS will keep everything thi in queue & will access file handler only once to pass the data, this is called "buffering".
#
# But perl can override this feature by telling operating system using a special variale $|
# When $| is set to 0 then perl tell Operating system to buffer the standard IO if possible.
# When $| is set to 1 beffering will be turned off automatically
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	$| = 1;
#	foreach (1..30) {			# Here each "." will be printed in one second interval for another 20 seconds
#		print ".";
#		sleep 1;
#		}
#	print "\n";
# }

# * using pipes (|)
# pipes(|) is something which connects two filehandlers together, that means it can send an output of one program to another program
# Perl will support using pipes to read from a program or a command & then use it, to read from or write to a program then you need open a file handler 
#
# There are mainly two  mode pipes used along with filehandlers 
# -|  This pipe will read the content from another program as an input to the script 
# |-  This pipe will send outout to a program which read from the script
#
# Synatx : open ($File_handler, "<pipe_mode", <command or program)
#		 : open ($file_handler, "-|", $some_cmd)						# This will read inpout from a command or a program
#		 : open ($file_handler, "|-", $some_program)					# This will send output to a command or a program
#
# Example : Below example will show how to read from a command using pipe 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# {
#	my $df_cmd = "/bin/df -Ph";
#	open (my $DF_FH, "-|", $df_cmd);
#	while (<$DF_FH>) {
#		chomp;
#		if ($_) {
#			my @df_split_array = split;
#			if ($df_split_array[5] =~ /^\/.+/) {
#				print "Mount point name is : $df_split_array[5] \n";
#				}
#			}
#		}
# }

# ** Function learned in CHAPTER 8 **
# lc() - This finction will treat all input given as lowercase 
# uc() - This function will treat all input given as upper case
#
# Example : An example will show us the usage of lc & uc 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
# {
#	print "Please Enter Your Previous company name : ";
#	chomp (my $company_name = <STDIN>);
#	print "Please Enter Your designation : ";
#	chomp (my $job_role = <STDIN>);
#	print ("\nMr : Ajay worked in ", uc($company_name), " as a ", lc($job_role), "\n"); # here $company_name will display in capital & $job_role will shown in small
# }
#


#*************************************************************************************************************************************************
#                                                                                                                                                #
#                                        **** CHAPTER 9 - String Processing ******                                                               #
#                                                                                                                                                #
#*************************************************************************************************************************************************
# Perl was created to be a text processing language & it is one of the most powerful text processing language around. 
# It shows its power of text processing using regular expression & also with its few of the build in modules. 
# more details explained below

# * Charector Position *
# This means the numeric position of a charector within a string & it is called as index, perl is a 'zero' based language & so the position or index starts from 'zero'. 
# Perl can access the charectors using its 'index value'
# Each of this position is called 'index', Index number for string "hellow How are you" can be mentioned as below 
# 
# String 		Index Value (Charector Position)
#   H				0
#   e				1
#   l				2
#   l				3
#   o				4
#   w				5
#   				6
#   H				7
#   o				8
#   w				9
#					10
#   a				11
#   r				12
#   e				13
#					14
#   Y				15
#   o				16
#   u				17
#
# Note : There is an alternate method also available to access the charector in a string using the 'negative Index' number, see an example below for a string "Apple is good'
#
# string		Negative Index
# 	d				-13
# 	o				-12
# 	o				-11
# 	g				-10
#					-9
#	s				-8
#	i				-7
#					-6
#	e				-5
#	l				-4
#	p				-3
#	p				-2
#	A				-1
#

# * String Functions *
# Perl has several builtin functions available for string processsing, this topic discuss more about those functios
#
# * Function - length()
# This function will help to identify the length of a string 
# Note : if there is no string passed along with the length function, then it will check the length of the default variable "$_", i.e length($_)
#
# Syntax : length($string) 
#
# Example : Below example will tell us the usage about lengthfunction
#
# #!/usr/bin/perl
#
# use warings;
# use strict;
#
# {
#	my $fix_string = "Welcome to Ooty, Nice meeting you";
#	print "Please enter an input string to process : ";
#	chomp(my $input_string = <STDIN>);
#	print ("Length of Fixed String : $fix_string is ---> ", length($fix_string), "\n");				# This will give the length as 33
#	print ("Lenth of Input string  : $input_string  is --->", length($input_string), "\n");			# This will give the length depend on the input string
# }
#
# * Function - index() 
# This function is used to determine the starting index of a substring within a string.
# It always start searching from the Index value "zero", but this can be altered by giving a index from which you need to start your search
# This always perform search for the index number of a sub string from "left to right"
# 
# Note : If index() function can't find any string then it returns "-1".
#
# Syntax : index($string, $sub_string)								# This will search for the location of the sub string from the starting of the string
# 		 : index($string, $sub_string, $index_value)				# This will search for the location of the sub string with in string from a location starting from given index number
#
# Example : Below Example give us the details of how it works 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#  {
#	my $string_location;
#	print "Please Enter Your [string] :";
#	chomp(my $string = <STDIN>);
#	print "Please Enter Your [sub string] :";
#	chomp(my $sub_string = <STDIN>);
#	print "Do you have any [index or Charector Position] from the search should start ? :";
#	chomp(my $index_value = <STDIN>);
#
#	if ($index_value =~ /\d/) {
#		$string_location = index($string, $sub_string, $index_value);
#		print "Starting Index number for your substring [$sub_string] is : $string_location \n";	# This will start search ing from a locatin where $index_value given
#		}
#	else
#		{
#		$string_location = index($string, $sub_string);
#		print "Starting Index number for your substring [$sub_string] is : $string_location \n";	# This will search from zero index value 
#		}
# }
# 
# * Function - rindex()
# This function is also similar to index() function but only difference is it start searching the position of a sub-string from "right to left"
# If the function is able to find the string then it will return the value of "0" else it will rettun "-1"
#
# Note : Eventhough rindex() perform the search from right to left, the zeroth charector is considared to be the leftmost charector.
#
# Syntax : rindex ($string, $sub-string)					# This will search for the sub-string from the zeroth index number 
# 		   rindex ($string, $sub-string, $index_Value)		# This will perform search from the given index number
#
# Example : Below example will explain about the rindex() 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $string_location;
#	print "Please Enter your string : ";
#	chomp(my $string=<STDIN>);
#	print "Please enter your sub-string to search in the above string : ";
#	chomp(my $sub_string=<STDIN>);
#	print "Do you have any specific index number from which search should start : ";
#	chomp(my $index_value=<STDIN>);
#	if ($index_value =~ /\d/) {
#		$string_location=rindex($string, $sub_string, $index_value);
#		print "Starting index number of the given string \"$string\" is $string_location \n";
#		}
#	elsif ($index_value =~ /\D/) {
#		die "Error : You can only give a numerical index number !!!";
#		}
#	else {
#		$string_location = rindex($string, $sub_string);
#		print "Starting Index number for your substring [$sub_string] is : $string_location \n";
#		}
# }
# 
# * Function - substr()
# This function is used to return a "sub_string" from a string according to the "starting_index" value and "length" given. 
# This is very useful when you have something some substring to retrun with respect to specific column layout
# 
# syntax : substr (string, starting_index, length)
#
# string 			- This will be the string which you are going to process
# starting_index 	- You want start returing the string from this index value 
# length			- Until this lenth you want to print the details
#
# Example : Below example will give us an idea about how substr() works 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict; 
#
# {
#	my $fstab_file = "/etc/fstab";
#	open (my $FSTAB, '<', $fstab_file) or die "$fstab_file : $!";					# opening /etc/fstab
#	while (<$FSTAB>) {
#		chomp;
#		if ($_ !~ /^\#/) {
#			if ($_) {
#				#my $mount_point = substr ($_, index($_, /^\/[\W{3}\/]/));
#				my $mount_point = substr($_, 24, 6);										# getting the value of mountpoint from /etcfstab, here '24' is the starting index & 6 is the length
#				print "$mount_point\n";
#				}
#			}
#		}
#	close $FSTAB;
# }
#
# * Function - tr() or translation
# Transalation function tr() is used to translate a variable, i.e if you want to replace one set of charector or word to another then you can use the 'tr()' function.
# This function is almost similar to 'substitution' you see in regular expressions.
#
# Note : For more examples and details refer book
#
# syntax : $input_string =~ tr/<search_pattern>/<replace_pattern>/ 
#
# Example : Below example exaplains the usage of tr()
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	print "Enter any string you want to translate to capital letter : ";
#	chomp(my $input_string=<STDIN>);
#	$input_string =~ tr/a-z/A-Z/;
#	#$input_string =~ tr/a-z/0-9/;
#	print "$input_string \n";
# }
# 
# * Function learned in this chapter *
#
#  length()		- This will help to uderstand the length of a string
#  index() 		- This will be help to starting index value to a substring
#  rindex()		- This is similar to index, but it start search from left to right 
#  substr()		- This will help tp retun a sub-string which is indicate to given with a 'start_index' and length 
#  tr()			- This will help to translate the charectors or word
#


#*************************************************************************************************************************************************
#																																				 #
#										 **** CHAPTER 10 - Interface to operating system ******																					 #	
#																																				 #
#*************************************************************************************************************************************************
#
# This chapter tell us about using various builtin function in perl which can help system administrator to deal with files and directories. 
# These activities includes creating files, directories, creating links, renaming files & executing oprating system programms etc. 
# 
# * Hash -  %ENV or %ENV hash
# When a perl program executes it inherits all environment variables set on the shell, that is any of the variable set on the shell will be still be accessible by perl
# If you want to know more about what variables are available please run "env" or "printenv" from your shell. 
# This environment variables can be used in our programs & also you can modify it according to your need
#
# Note : Incase you are modifying the 'env variable' while executing the program that change will be applicable to the execution of the program not in the shell. 
# 		 Change will be discard when the programs gets terminated 
#
# Synatx : if you want to print the print the path variable you can print as follows 
#		   print "$ENV{PATH} \n"; 	
#
#		 : Incase you want to modify the PATH variable you can do as follows 
#		   $ENV{PATH} = '/usr/local/sbin:/usr/local/bin:/opt/ajay/bin'; print "$ENV{PATH} \n";
#
# Example : Below example will exaplin the usage of %ENV
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $cmd = shift @ARGV;												# Reading user input as argument to the script 
#	die "No cmd arguments given" unless ($cmd);							# Exit program if there is no argument passed along along with the script 
#	foreach my $path (split /:/, $ENV{PATH}) {							# splitting each path and reading it
#		if (-x "$path/$cmd") {											# Making sure the executable cmd given is under the current path
#			print "$ENV{HOSTNAME} : $cmd is located on $path/$cmd \n"; 	# Hostname is also reading from environment variable 
#			last;
#			}	
#	}
# }
#
# * Working with files and directories *
# You will find several perl builtin functions in chapter which basically help us in dealing with operating system. Key things you will learn in this chapter are "File Globbiging", "DIR streaming", etc 
#
# * Function : File Globbing  - glob() 
# Those who work in Unix knows that when you want to print a group of files with a similar extension we uses "*", i.e incase you want to print all '.pl' file you will say as "ls *.pl"
# The part which we mention as " *.pl " is known as the file globing, in perl we can achieve the same using glob() function. i.e you can write this as glob('*.pl')
# File globbing can alos be represent with on ' < > ', i.e glob(*.pl) can be written as <*.pl> also 
#
# Syntax  : glob('file_glob')    or   <'flie_glob'>
# Example : glob('*.dat')        or   <*.dat>
# 
# sclar context - In scalar context when we use glob() it will return the next available data found in the search pattern. 
# Example : Below example will tell us the usage of glob() function
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	my $source_dir='/var/log';
#	my @var_globbed_list=glob('/var/log/*.log');							# This is 'list method', this will print all '*.log' files under '/var/log/' directory
#	print "List of logfile on host $ENV{HOSTNAME}\n\n@var_globbed_list\n\n"; 
#	my $etc_glob_list=</etc/*.conf>;										# This is 'scalar method', this will print the next available value for *.conf find under '/etc/'. 
#	print "List of configuration file under /etc on $ENV{HOSTNAME} is\n\n$etc_glob_list\n\n";
# }
#
# * Reading Directories *
# To read a directory and its contents you require couple of perl inbuilt modules such as 'opendir() and readdir()'
#
# * Function : opendir() 
# This function is similar to open() function which used to handle files using filehandler 
# Here you need to have a 'directory handler' along with this function to process the content you read using 'opendir()'
#
# Synatx  : opendir(directory_handler,  /dir_path);
#         : opendir(directory_handler,  /dir_path) or die "unable to open dir_path : $!";  # Here using '$!' & die()  will help you to understand why opendir() failed & exit if any issues.
#
# Example : opendir(NET_DIR_HNDLR, /etc/sysconfig/network-scripts) or die "unable to open /etc/sysconfig/network-scripts : $!";
#
# * Function : readdir()
# This function will help you to read the content of the files or directories that read by opendir() filehandler. 
#
# Synatx  : readdir(directory_handler);
# Example : readdir($NET_DIR_HNDLR);
#
# Example : Below example will go through the usage for opendir() and readdir(), this program is written to list how many .conf files under /etc
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
# 	my $source_dir='/etc';
# 	my $data;
#	opendir(my $ETC_DIR_DH, "$source_dir") or die "Unable to open $source_dir : $!";
#	while ($_ = readdir($ETC_DIR_DH,)) {
#		next if ($_ eq ".") or ($_ eq "..");
#		if ($_ =~ /.conf$/) {
#			print $_, " " x (40 - length($_));			# This will print the configuration file under /etc with a standard format with 40 space
#			print "config_file"; 
#			print "\n";
#		}
#	}
#	close $ETC_DIR_DH;
# }	
# 
# * Functions to work with files and directories *
# This contains various functions in perl which will help us prform various operating system tasks, please refer below for more details
#
# * Function - chdir()
# This function will help to chnage it current working directory for the program which we are running. 
# This don not have any effect on the shell from which this program is running, it only gets changed in the program we execute
#
# Syntax  : chdir(directory_path) or die "Unable to open directory_path : $!"
# Example : chdir(/etc/sysconfig/network-scripts) or die "Unable to open /etc/sysconfig/network-scripts : $!"
#
# Note : by default this will switch its patch to $ENV{PATH} unless we don't define a path
#
# * Function - unlink() 
# This function will help us to delete files from the system, what files you are given as an input to the function will be deleted 
#
# Syntax  : unlink(file1, file2, file3, etc..) or dir "Unable to delete files : $!"
# Example : unlink(/var/log/messages, /var/log/cron) or die "unable to delete files : $!"
#
# * Function : rename()
# This function is similar to "mv" command in unix, this can be used either for rename a file or to move a file to different location in filesystem.
#
# Syntax  : rename(old_file_name, new_file_name) or die "can't rename file : $!"
# Example : rename(sample.doc, sample.txt) or die "can't rename sample.doc : $!"
#
# Synatx  : rename(path_to_source_file, path_to_destination_file)
# Example : rename(/etc/sysconfig/network, /var/tmp/backup/network) or die "can't move /etc/sysconfig/network : $!"
#
# * Function : link(), symlink() and readlink() 
# These three functions will help us to work with link files please, see the details below 
#
# link()  - This function will create a 'hard link' from a file
# Syntax  : link(source_file, link_file) or die "can't create a hard link for source_file : $!"
# Example : link(/bin/ls, /usr/local/bin/ls) or die "can't create a hard link for /bin/ls : $!"
#
# symlink() - This function will create a 'soft link' from a file
# Syntax  : symlink(source_file, link_file) or die "can't create soft link for source_file : $!"
# Example : symlink(/bin/ls, /usr/local/bin/ls) or die "can't create soft link for source_file : $!"
#
# readlink() - This function will help us to find what file file is pointing a 'soft link or sym link'
# Syntax  : readlink(sym_link_name / soft_link_name)
# Example : readlink(/usr/local/bin/ls)
# 
# * Function - mkdir() and rmdir()
# These functions will help us in creating and deleting directories 
#
# mkdir()   - This function will help to create directories, this return true on success and false on failures
#			  Along this finction you need to pass 'mode' to the directory, here 'mode' is is the 'permission' you want to set on that directory 
# Note : mode or permission must always be represented in octal number proceeding with '0', perl will convert the permission and set it to the directory 
#
# Syntax  : mkdir(dir_to_create, mode) or die "failed to create directory : $!"
# Example : mkdir(/var/tmp/backup_dir, 0755) or die "failed to create directory /var/tmp/backup_dir : $!"
#
# rmdir() 	- This will help to remove directories from filesystem, this will return true on success and false on failure
#
# Syntax  : rmdir(dir_to_remove) or die "unable to remove directory :$!"
# Example : rmdir(/var/tmp/backup_dir) or die "  unable to remove directory /var/tmp/backup_dir : $!"
#
# * Function - chmod()
# This function will help to change permission of a file or directory 
#
# Syntax  : chmod(file_or_dir_name, mode) or die "unable to change permission : $!"
# Example : chmod(/etc/fstab, 0644) or die "unable to change permission : $!"
#
# Example : Below example will help us in understanding how to use various fail handling functions which studied in this chapter
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
#	my $base_dir='/var/tmp/cooking_lab';
#	my $veg_dish='thoran.ord';
#	my $veg_curry='sambar.ord';
#	my $non_veg_dish='chicken_fry.ord';
#	my $non_veg_curry='kadai_checken.ord';
#	my $veg_main_cource='kerala_rice.ord';
#	my $non_veg_main_cource='chappathi.ord';
#	my @veg_menu=($veg_dish, $veg_curry, $veg_main_cource);
#	my @non_veg_menu=($non_veg_dish, $non_veg_curry, $non_veg_main_cource);
#	my $current_directory=$ENV{PWD};
#	my $item;
#	my $customer_choice;
#
#	print "Please enter your options\n\n";
#	print "\t1. order_food\n\t2. change_order\n\t3. cancel_order\n\t4. exit\n\n:";
#	chomp($customer_choice=<STDIN>);	
#	if ($customer_choice eq 'order_food' || $customer_choice ==1) {
#		print "Do you want go with\n\t1. veg\n\t2. non_veg\n\n:";
#		chomp(my $order_type=<STDIN>);
#		if ($order_type eq "veg" || $order_type == 1) {
#			create_dishes($veg_dish, $veg_curry, $veg_main_cource);
#			}
#		if ($order_type eq "non_veg" || $order_type ==2) {
#			create_dishes($non_veg_dish, $non_veg_curry, $non_veg_main_cource);
#			}
#		}
#	elsif ($customer_choice eq "change_order" || $customer_choice == 2) {
#		change_order();
#		}
#	elsif ($customer_choice eq "cancel_order" || $customer_choice == 3) {
#		cancel_order();
#		}	
#	else
#		{
#		die "Exiting";
#		}
#	
#	sub create_dishes {
#		my $dish1=shift;
#		my $dish2=shift;
#		my $dish3=shift;
#		my @menu_type=($dish1, $dish2, $dish3);
#		print "setting up the base directory for test : [$base_dir]\n";
#		if (! -d $base_dir) {
#			mkdir($base_dir, 0755) or die "unable to create [$base_dir] : $!";
#			}
#		change_to_base_dir();
#		print "creating dishes [@menu_type]\n";
#		foreach $item (@menu_type) {
#			open(my $MENU_ITEM, '>' ,$item) or die "unable to create [$item] : $!";
#			print "success : created $item  and now setting up permission\n";
#			#chmod("$base_dir/$item", 0644) or die "failed to setup permission for [$item] : $!";	
#			close $MENU_ITEM;
#			};
#		list_your_order ();
#	}
#
#	sub change_order {
#		my %change_options_available = (
#				thoran 			=> "avial",
#				sambar 			=> "rasam",
#				kerala_rice 	=> "ponni_rice",	
#				chicken_fry 	=> "chicken_tandoori",
#				kadai_chicken 	=> "chicken_chettinad",
#				chappathi		=> "naan"
#			);
#		list_your_order();
#		print "\nwhich dish you want to change (please choose the name of the dish from above) : ";
#		chomp(my $change_item=<STDIN>);
#		print "Your order can only change with $change_options_available{$change_item}";
#		print " do you want to continue (y/n) :";
#		chomp(my $user_confirm=<STDIN>);
#		if ($user_confirm eq "y" || $user_confirm eq "yes" || $user_confirm eq "YES" || $user_confirm eq "Yes") {
#			change_to_base_dir();
#			rename("$change_item.ord", "$change_options_available{$change_item}.ord") or die "unable to change your order : $!";
#			print "success : your order successfully changed to $change_options_available{$change_item} \n";
#			}
#		else
#			{
#			print "information : no changes are made as requested, thank you!!!\n";
#			}
#	}
#
#	sub cancel_order {
#		print "Do you want to cancel your order (y/n) : ";
#		chomp(my $user_confirm=<STDIN>);
#		if ($user_confirm eq "y" || $user_confirm eq "yes" || $user_confirm eq "YES" || $user_confirm eq "Yes") {
#			my @cancel_ord=glob("$base_dir/*.ord");
#			foreach my $cancel_item (@cancel_ord) {
#				unlink($cancel_item) or die "unable to remove $cancel_item : $!";
#				print "success : removed $cancel_item from order \n";
#				};
#			rmdir($base_dir) or die "unable to remove $base_dir : $!";
#			print "success : removed $base_dir \n";
#			}
#		else
#			{
#			die "Exitinig since no chnages required";
#			}
#	}	
#
#	sub list_your_order {
#		my @current_available_dishes=glob("$base_dir/*.ord");
#		my $count=1;
#		print "\nDear customer : below items are your order \n\n";
#		foreach $item (@current_available_dishes) {
#			my @mod_item_array=split(/\//, $item);
#			my $mod_item=$mod_item_array[4];
#			$mod_item =~ s{.ord$}{}g;
#			print "\t$count. $mod_item\n";
#			$count++;
#			};
#	}	
#
#	sub change_to_base_dir {
#		print "switching from [$current_directory] to [$base_dir] \n" if ($current_directory ne $base_dir);
#        chdir($base_dir) or die "unable to switch to $base_dir : $!" if ($current_directory ne $base_dir);
#		}
# }
#
# * Executing external programs *
# There are few utilities available in perl which helps you to run external programs such as an external script or shell command.
# Earlier with 'open()' function we learned using '-|' (pipe) we can get the output of commands to a 'FILE_HANDLER' and then process the output. 
# Likewise we have few more utilities available to deal with shell commands such as system(), backquates ` `, qx() etc..
#
# Note : even though you will sometime have to run a shell command and get details it is always best to go with the inbuilt functions available with perl itself.
#        reason for this is when you run a shell command it is going to start a new shell which a larger program and then accourding to the usage it is going to call the system functions. 
#        rather than doing that you can call the same functions using the perl inbuilt functions and this will help inturn to stop loading the entire shell program.
#        when you start writing programs with light approch (using minimal system resources) you must try to avoid as much as shell commands. 
#
# * Function - system()
# This function will help us to run any shell commands and if any standard output available with the script then it will print as standard output in screen.
#
# Syntax  : system('command')
# Example : system('date')
#
# Note : This function will return a error code depend on the command is successful or not, if success error code will be 0 and if fails then code will be between 1 - 255
#
# Example : below example will give us an idea about the system() usage 
#
# #!/usr/bin/perl
# use warnings;
# use strict;
#
# {
#	my $error_code=system('df -h');			# This will print the df output on screen and will store the error code on the variable
#	if ($error_code == 0) {
#		print "success : last command run was successful, Error code is : $error_code \n";
#		};
# }
#
# * backquotes ` ` or qx()
# system() function was helping us to print the output on screen, but there are sometimes where we want to store output to an array or scalar variabe.
# That can be achieved by this either backquotes ` ` or qx (), both can used for same purpose 
#
# Syntax  : $scalar_variable=`command`
# 		  : $scalar_variable=qx(command)
# 		  : @array_variable=`cmd`
# 		  : @array_variable=qx(command)
#
#

#*************************************************************************************************************************************************
#																																				 #
#											*** CHAPTER 11 - References ****																					 #
#																																				 #		
#*************************************************************************************************************************************************
#
# References is piece of data that tells us the location of another set of data. In perl reference is always a 'scalar' but the data stored inside it may not be a scalar. 
# This can talk about the data stored with in a hash or array. Hashes are similar to 'pointers' in C or C++ languages.
# Using referance we can talk about the hash of a hash or array of array an array or more complex multi dimentional data types, which may require at certaiin times.
# Using referance we can put an array inside an array or hash inside a hash, but not only limited to that ..
#
# Note : Reference will always store the 'memory adress' to a data type it referring to, not the actual data. Using this memory address with the help of reference you can access the data.
#
# * Anonymity (reference to anonymous data) *
# Normaly when we do a reference, first we define a set of data to array or hash or any other type to a variable name and then we refer to that data via the variable. 
# Rather than accessing it indirectly via a '@array_variable' or '%hash_variable' or anything of that type, we can refer to that data directly since we know the memory location for that data. 
# Using this anonymity method we can avoid the middle man in between (variable).
#
# For example, @array_name=(1, 2, 3, 4) rather than accessing the data via variable @array_name we can directly refer to the data & access or use or modify it.
#
# Note : This doesn't mean that we are not going to use array or hash in a program anymore with reference. We will be still using them.
#        But there will be situation coming while creating programs we need to refer data directly, on such situations we will use it
#
# * Creation of a reference (Page - 232) *
# Reference can be created in two different situation, see details below 
# * Create reference to a variable where data is already stored in a variable
# * Create a direct refernce to the data you are looking for (anonymous reference)
#
# * Create reference to a variable where data is already stored in a variable 
# if the data is already inside a variable then we can use a 'backslash ( \ )' infront of the variable 
#
# Syntax  : $reference_variable = \@array_variable
# 		  : $reference_variable = \%hash_variable
# 		  : $referenve_variable = \$scalar_variable
#
# Example : @data = (1, 2, 3, 4, 5)
# 		  : $array_ref  = \@data			# here an array referance named "$array_ref" created to an array "@data"
#		  
#		  : %phone_book = {ajay => "8667546", appu => "78686"}
# 		  : $hash_ref   = \%phone_book		# here a hash reference named "$hash_ref" created to a hash called "%phone_book"
#
#		  : $student_name = ajay
# 		  : $scalar_ref = \$student_name 	# here a scalar referance named "$scalar_ref" created to a hash called "$student_name"
#
# * Referencing ordinary scalars to an array 
# Using this method we can do reference to a vraible and use them directly in an array, using this method you are removing the middle man (variable) between the array and data by referring to direct mem address.
#
# Example : Below example will tell us about how to reference ordinary scalar vaiable to and array 
#
#	my $data01=123;
#	my $data02=456;
#	my $data03=789;
#	my @number_array = (\$data01, \$data02, \$data03); # This will help array to access the elements inside the array with direct memeory address
#
# * Referencing an array to a hash
# Using this method you can reference an array to a hash which will inturn help the hash to access the data stored in array directly using memory address without the help of a 'array variable'
#
# Example : Below example will tell us about how to reference an array to a hash
#
# 	my @sing_house=(achan, amma, shuppu, achu);
# 	my @ktda_house=(achachan, achamma);
# 	my @adoor_house=(appupan, ammama);
# 	%family_members = {
# 					sing  => \@sing_house,		# This will have the memeory adress of data @sing_house stored
# 					ktda  => \@ktda_house,		# This will have the memeory adress of data @ktda_house stored
# 					adoor => \@adoor_house		# This will have the memeory adress of data @adoor_house stored
# 					};
#
# * Arrays inside an array
# Using reference we can call array inside an array which will help to create an multi dimentional arrays & will help to access data more faster 
#
# Example : Below example tell us about an array inside an array
#
# 	@family_tree01=(shuppu, achu);
# 	@family_tree02=(ajay, aparna, \@family_tree01);
# 	@family_tree03=(vijayan, lolitha, \@family_tree02);
# 	@family_tree04=(surendran, sulochana, \@family_tree03);			# here @family_tree04 will contain the data of all its sub array mentioned 
#
#
# Note : See page 233 in "perl begin guide" to understand above two concept with the help of a "diagram"
# 
# * Anonymous arrays and anonymous hashes
# Using anonymous method we can directly reference to an array or hash without the help of a middleman (variable)
# This will help us to reach out to the 'raw data' directly without calling any other variable.
# Way to achive this is mentioned below 
#
# To do reference directly to an array we can use square bracket '[ ]' instead of paranthesis '( )' while defining them
#
# Synatx  : $array_ref = [1 ,2 3, 4]
# Example : Below exampe will tell us how a indirect reference can be made to direct or anonymous reference 
# {
# 	@house_members = (Ajay, Aparna, Vaiga, Rishi);		# This is the indirect method where we are using a middle man variale @house_members to access the data in that mem address
#   $house_mem_ref = \@house_members;
# }
# $house_mem_ref = [Ajay, Aparna, Vaiga, Rishi]		# This is the direct method and here we are using square bracket to define the data '[]' to reference anonymously
#
# Note : This creates an array reference to a nameless array using anonymous reference on "$house_mem_ref = [ ]"
#
# To do reference directly to a hash we can use hash '{ }' instead of paranthsis '( )' while defining them
#
# Syntax  : $hash_ref  = {name => "Ajay", contact => "86165478"}
# Example : Below example will tell us what is difference between inderect referance (using variable) and anonymous (direct) refernce methods
# {
# 	%relation = (						# This is the indirect method where we are accessing data via a middle man (variable)
# 			Ajay	=> "Father",
# 			Appu	=> "Mother",
# 		 	Shuppu	=> "Daughter",
# 			Tuplu	=> "Son");
# 	$relation_ref = \%relation;
# }
#
# $relation_ref = {						# This is the direct method where we are accessing data using data reference using { } to access data 
# 			Ajay    => "Father",
# 			Appu    => "Mother",
# 			Shuppu  => "Daughter",
# 			Tuplu   => "Son"};
#
# Note : This creates a hash reference to a nameless (no name) hash using anonymous reference on "$relation_ref = { }"
#
# * Using Reference * 
# The process of accessing data using reference is called 'de-referencing'
# To 'derefernce' a data put reference in a curly braces, wherever we uses the variable name
#
# Syntax  : @new_array = @{$array_ref_name}  # Here '@new_array' array variable in which we are going to store the data array areference '$array_ref_name'
# Example : Below example tell us about how to use reference 
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#  {
#	my @indirect_array = (1..10);
#	my $indirect_array_ref	= \@indirect_array;
#	my $indirect_array_max_index = $#{$indirect_array_ref};				# This will store the highest index value of an array 
#	print "Below are the elements from indirect array reference \n";
#	foreach (@{$indirect_array_ref}) {
#		print "Current element is : $_ \n";
#		};
#	print "Maximum Index number of indirect array is : $indirect_array_max_index \n";
#	print "Our reference is looks like : $indirect_array_ref \n";		# This will print the memory address of the array
#  }
#
# * Array elements - Handling array and array elements with reference 
# We have already seen how to define reference for an array using the direct method and indirect method 
# To access an element in an array you need to call reference in curely braces and then give the index number for array in square bracket
#
# Syntax   : $varibale_name = ${$ref_name}[Index_number]
# Example  : $family_array_ref = [ajay, aparna, shuppu, appu ]		# anonymous or direct reference 
#            $father_name = ${$family_array_ref}[0] 				# Here we are calling the father name in anonymouns refernce 'family_array_ref' with index value 0
#
# Example  : Below array contains details about family and calling their details using reference
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
#{
#	my $kernel_family_ref = ["sulochana", "surendran"];												# Here reference directly pointing to the data using anonymous reference
#	my @root_family = qw(vijayan, lolitha, raji);					
#	my $root_family_ref = \@root_family ;															# Indirect reference using the array variable declared former 
#	my @family = ("ajay", "aparna", "appu", "shuppu", @{$root_family_ref}, @{$kernel_family_ref});	# Combining anonymous and indirect reference to an array 
#	my $family_ref = \@family;
#	foreach (0 .. $#family) {																		# Requesting array to continue till the max index number of the array
#		print "current element using array variables is (index = $_)\t : $family[$_] \n";			# Printing from array 	
#		print "Current element using array reference is (index = $_)\t : @{$family_ref}[$_] \n";	# printing from reference
#		};
#}
#
# Note : There is no difference between the data we access from the array variabe and reference veriable, only difference is reference can reach to the data faster since uses the memory address of the data 
#
# * Reference Modification 
# You can use all shift(), unshift(), push(), pop() functions along with reference also to modify its contents. 
# When you change the data it will change the data in the actual array also since it directly making the changes using the memory address of the data
#
# To do modification using any of the array modification functions mentioned above syntax is below 
# Syntax  : unshift @{$array_ref};
#
# To do modification to an array element, you can directly make changes in element_itself
# Syntax  : ${$array_ref}[index_number] = new_value
# Example : ${$fruit_array}[0] = apple
#
# Example : Below example will tell us about various ways of reference modification for array
#
# #!/usr/bin/perl
#
# use warnings;
# use strict;
#
# {
#	sub unshift_using_array_ref {
#	my @fruit_tray = qw(apple orange grape pear);
#	print "\norginal array content is [@fruit_tray]\n\n";
#	my $fruit_tray_ref = \@fruit_tray;
#	unshift(@{$fruit_tray_ref}, 'jackfruit', 'plum');					# This will help to add contact infront of array and result is [jackfruit plum apple orange grape pear]
#	print "Here are are modified contents of \@fruit_tray using reference with \"unshift()\" [@fruit_tray] \n";
#	}
#
#	sub pop_using_anonymous_array_ref {
#	my $fruit_tray_ref = [qw(apple orange grape pear)];
#	pop(@{$fruit_tray_ref});
#	print "Here is the modified contents of anonymous reference \$ruit_tray_ref using \"pop()\" [@{$fruit_tray_ref}] \n";
#	}	
#
#	sub array_element_modification {
#	my $fruit_tray_ref = [qw(apple orange grape pear)];
#	@{$fruit_tray_ref}[0] = "jackfruit";
#	print "Here is the modified value for \[index 0\] in anonymous array \$fruit_tray_ref  : [@{$fruit_tray_ref}] \n";
#	}	
#
# unshift_using_array_ref();
# pop_using_anonymous_array_ref();
# array_element_modification();
# }
#
# * Hash reference (Page 241)
#
# ((( Will continue reference after completing remaining chapters )))
#


#*************************************************************************************************************************************************
#                                                                                                                                                #
#                               ***** Chapter 12 - Modules *****                                                                 #
#                                                                                                                                                #
#*************************************************************************************************************************************************
#
# * What is Modules * 
# Modules are pre written functions or sub-routines and varibales which are available to perform certain tasks. 
# Modules can be acessed by browsing in below two websites which points to CPAN (Comprehensive Perl Archive Network).
#
# www.cpan.org
# www.search.cpan.org           # This site will help you to search and browse through CPAN
#
# Perl modules can help us in solving many problems using simple prigrams, for example, network, sharepoint, dns and many other.
# In this chapter we will see how to write modules and use it your program and also how to use various modules available in CPAN
#
#
#
# * How to create a Module * 
# To create a module, you will need to mainly look at below five points 
# . First think about a very good name which can easily give an understanding about the functionality of the module (e.g : module used for logging can be called as "Logger")
# . Put the source code into the file which has naming as filename.pm (e.g : incase we uses logging, we can call the filename as "Logger.pm")
# . Make the module a package or namespace (more on package later), by placing the "Package module_name" at the top of file (e.g : if the module name is logger, then use "package Logger;")
# . Define the variables and functions in the file, which is needed to design the module
# . Have the file a return a value by returning a true value "1"
#
# Example : Below is an example of defining a module (Testing pending)
#
# Logger.pm                 # This is the definition of the module 
# package Logger;             # definings package for the module 
#
# use warnings;
# use strict;
#
# my $filename=shift;
# my $level=1;
# chomp(my $time_stamp=qx(date));
# chomp(my $host_name=qx(uname -n);
#
# sub open_log {
#   open(my $LOG_FILE, ">>", $filename) or die "unable to open $filename : $!";
#    print $LOG_FILE "$time_stamp : $host_name : log file started \n";
# }
#
# sub write_log {
#    my ($msg_level, $msg_content) = shift @_;
#    print $LOG_FILE "$time_stamp : $host_name : $msg_level : $msg_content";
# 
# }
#
# sub log_level {
#    my $level_adjust=shift
#    $level = $level_adjust if ($level_adjust > $level);
# }
#
# sub close_log {
#    close $LOG_FILE;
# }
#
# 1;                      # This will return a true value to program
#
# Note : We need to return a true value of "1" to program as you see in the program. However latest perl versions do not require this practice we will still use it for backward compatibility.
#
# 
# * Calling external programs and modules *
# There are various methods available to process external programs such as do(), require() and use(), details of each function are defined below.
#
# do()	 	: used for calling external programs at the @INC module library location, more details are below 
# require()	: used for calling external programs and modules located in @INC, more details below 
# use()		: Most common method used for accessing modules, this gets loaded in the compile stage rather than run time.
#
# * do () - How to call an external script or program *
# do() will look for a program or script file by searching in the @INC path or the path specified, if the it is able to locate the program then it will execute the code block and will proceed further. 
# Incase it is unable to locate the program then it will skip the code block and move on with the further programs. 
#
# Note 	: When you are using 'do' it will not see the lexical variable what defined with in the main program once you are inside the additional program which called by do.
# 		: do() will not throw an error even if the requested program is not located in the location 
# 		: do() can be used to load a program any number of times  
#
# Disadvantage : This will not give any error incase you are unable to load the program or if there any error in the external code block you are calling.
#
# Syntax  : do (program.pl)
#
# Example : Below program will import a script from test module directory and will run that program
#
# use warnings;
# use strict;
#
# {
# 	push (@INC, '/docs/study_material/perl/script/modules');		# here we are pushing our custom perl module location to @INC module paths
#	do ("test_do_method.pl");										# here an external script test_do_method.pl gets executed from '/docs/study_material/perl/script/modules'
#	print "TEST \n";
#	do ("test_do_method.pl"); 										# Calling the same external program again to make sure it gets loaded as requested 
# }
#
#
# * require () - How to call an external script or program * 
# require() can also be used for calling external programs and importantly it can be used for calling modules available in the @INC location. 
# This will allow you to load the program only once and not more than one time since it is already loaded.
# It will fail with an error message if the program not found in @INC which will help you in debugging the issues unlike do() which gives difficulty there.
# This will help you in defining modules available in a base module directory with the help of a seperator ' :: '.
#
# Sytanx 	: require program.pl				# Calling an external program
# 			: require module.pm					# Calling a module located inside @INC
# 			: require module_dir::module.pm		# calling a module names module.pm inside the directory module_dir
# 			: require perl_version				# this will terminate the program if the perl version is lower than expected (example : require v5.20.3)
#
# Example : below example will explain various usage about the require function.
#
# use warnings; 
# use strict; 
#
# {
#	push (@INC, '/docs/study_material/perl/script/modules');			# modifying the module array list with custom made modules 
#	require ("test_do_method.pl");										# calling external program using require
#	print "Test code block 1 \n";
#	require ("test_do_method.pl");										# calling the same external program second time and this will not get executed since require will run the program only once
#	print "Test code block 2 \n";
# }
#
# {
#	require Net::Ping;													# using require to source Ping module from Net directory under default @INC location
#	my $p = Net::Ping->new();
#	if ($p->ping("ubuntu.master.lab.com")) {
#		print "Host : ubuntu.master.lab.com is alive \n";
#	}
#	else {
#		print "Host : ubuntu.master.lab.com is Not Alive \n";
#	}
# }
#
# {
#	require v6.20.3;													# using require to check for the supported perl version, if the host is not of the same version program will terminate
# }
#
#
# * use - calling modules (Page 262) *
# The way we use modules normally in perl is "use". Unlike require use will start loading any modules defined via 'use' at the begining of the program.
# So we can say, 'use' loads the modules in the compile time ratherthan run time. 
# If perl sees 'use' anywere in the program, then it will include the module in that program.
#
# Note : There is no point of calling a module using use after validating few condition since it gets loaded in the very begining. 
# 	   : i.e you do not need to define something like this, use FILE::basename if ($BASENAME)
#
# Syntax : use module_name
# 		 : use module_dir::module_name
#
# Example : use warnings;
# 		  : use File::Find
#
# * How to modify @INC
# This is very important to know that how can you modify @INC.
# Default contents of @INC are loaded during the compile time & so if you are asking perl to refer to a module then  you need to place the module in any of the @INC directory before executing the script. 
#
# * Special subroutine "BEGIN"
# If you execute a program as below it will not make any sense because the modules gets loaded from @INC well before the run time. 
#
# unshift (@INC, "/apps/uat_modules");
# use apps_test.pm								# This module cannot be loaded from @INC since use gets executed at compile stage and unshift gets loaded in run time.
#
# To address this scenario there is another special subroutine called "BEGIN", this can help us in defining something during the complile stage of the program.
#
# Syntax : sub BEGIN {
# 					unshift(@INC, "/apps/uat_modules");
# 					}
# 			use apps_test.pm;
#
# Note : using this method "unshift" will gets executed during the compile stage well before it calls "use"
#
# * Using "use lib" to load module directories 
# Similar to what we seen for "BEGIN", this is another easy way of loading or updting the module path during the compile stage. 
#
# Syntax :	use lib "/apps/uat_modules";
# 			use apps_test.pm; 
#
# Note : Here "/apps/uat_modules" will gets loaded into @INC well before apps_test.pm in the compile stage and that way we will be to load the module successfully.
# 		  
#
# More on Modules (Page 263)
#
# * Tips from this chapter *
# @INC 		: This is the default array contains the information about the path of all modules
#
#*************************************************************************************************************************************************
#                                                                                                                                                #
#                               ***** Chapter 15 - Perl and DBI *****                                                                 #
#                                                                                                                                                #
#*************************************************************************************************************************************************
#
# * What is a database 
# This is a way to represent data and there are various database available in the market 
# 
# 1. Relational database (RDBMS)
#  - These are the most common database available such as postgressql, mysql, oracle, sybase etc 
#  - These provides better performamnce compare to the desktop based databases software 
#  - Here Data is stored in tables and each tables will have some key fields which connects to other tables, hence all tables are connected each other
#
# 2. Operational database
#  - An operational database is usually hugely important to Organisations as they include the customer database, personal database and inventory database 
#  - ie the details of how much of a product the company has as well as information on the customers who buy them. 
#  - The data stored in operational databases can be changed and manipulated depending on what the company requires.
#
# 3. Database warehouses
#  - Normally in organisations where they need to preserve data for a long time this database is used 
#  - Data which kept in database warehouse must have already gone through all editing and alteration required and will be unchanged
#  - These database are kept for market analysis and other comapritive studies using older data with current market 
#
# 4. Distributed database
#  - These database are often used by companies where they have offices in various geographical locations 
#  - Each location will have its own copy of the database and combination of all together makes a single ditributed database
#
# 5. End user database 
#  - There are wide variety of database available in the end user database 
#  - Typical examples are excel, word, notepad, presentation and downloadable files etc 
#
# * What is DBI module 
# This is one of the strong and reliable module which provided by perl. 
# This act as an API between perl program and database to fetch the data and also to insert the database 
# More details about the DBI module, we will see later in this chapter 
# 
# * A detailed look at relational database 
# There are mainly two features with the relational database 
# - Relational database has the data persistent, it continues to exist even after a program continues to access or modifies it 
# - Unlike files on a server, relational database provides concurrent access for the files by multiple useres, database server make sure the changes are done in a safer way.
# 
# Relational database stores data in a tables, tables contain both rows and fields, fields contains one basic piece of information  
# Let’s say we want to keep some information about our favorite musicians: their names, phone
# numbers, and the instruments that they play. We might start by creating a list of the musicians like this: 1
# 
# Name 					phone
# Roger Waters 				555-1212
# Geddy Lee					555-2323
# Marshall Mathers III 		555-3434
# Thom Yorke 				555-4545
# Lenny Kravitz 			555-5656
# Mike Diamond 				555-6767
# 
# This list shows six lines of data—the "rows" in relational-database-speak. 
# When we take these and place them together into one collection of data, we have a table. 
# Normally, for each row we want to create a unique identifier—the "primary key", or simply the key (just in case we have two different Marshall Mathers III in our table). 
# We can access the MMIII we’re interested in using this unique value.
# We’ll name the field column containing the key player_id and name the other fields, as well:
# 
# player_id 	name 				phone
# 1 		Roger Waters 			555-1212
# 2 		Geddy Lee 				555-2323
# 3 		Marshall Mathers III 	555-3434
# 4 		Thom Yorke 				555-4545
# 5 		Lenny Kravitz 			555-5656
# 6 		Mike Diamond 			555-6767
# 
# 
# So now we’ve created a table (let’s name it musicians) with three fields—player_id, name, and phone and six rows of information.
# Normally when we build a database, we spread the information among several tables that connect to one another in some way, usually by the key, but you can use another field. 
# To illustrate, let’s expand our information about musicians to describe what each plays and some important facts about those instruments.
# We could add each instrument to the row in the musicians table, but we’d duplicate a lot of information. 
# For instance, three of our performers play guitar, so any guitar data we provide we’d have to be repeat for each musician. 
# Also, several of our musicians have multiple talents—for instance, Thom Yorke plays guitar and keyboards and sings. 
# If we enter data for each instrument Thom plays, our table will become big and difficult to work with. 
# Instead, let’s create another table, named instruments, to hold this information:
# 
# inst_id		 instrument 		type 		difficulty
# 1 		Bagpipes 		reed 			9
# 2 		Oboe 			reed 			9
# 3 		Violin 			string 			7
# 4			Harp 			string 			8
# 5			Trumpet 		brass 			5
# 6 		Bugle 			brass 			6
# 7 		keyboards 		keys 			1
# 8 		Timpani 		percussion 		4
# 9 		Drums 			percussion		0
# 10 		Piccolo 		flute 			5
# 11 		Guitar 			string 			4
# 12 		Bass 			string 			3
# 13 		conductor 		for-show-only 	0
# 14 		Vocals 			vocal 			5
# 
# 
# Now that we’ve defined some instruments along with our opinion of their associated degrees of difficulty, 
# we somehow need to map the instrument information to the information stored in the musicians table. 
# In other words, we need to indicate how the instruments and the musicians tables relate. 
# We could simply add the inst_id value to the musicians table like this:
# 
# player_id 		Name 		phone 		inst_id
# 1 			Roger Waters 555-1212 		 12
# 
# and so on, but remember that many of our musicians play more than one instrument. 
# We would then need two rows for Roger Waters (he sings, too) and three rows for Thom Yorke. 
# Repeating their information is a waste of memory and makes the database too complex. 
# Instead, let’s create another table that will connect these two tables. 
# We will call it what_they_play and it will have two fields:player_id and inst_id.
# 
# player_id 	inst_id
# 1 		11
# 1 		14
# 2 		12
# 2 		14
# 3 		14
# 4 		7
# 4 		11
# 4 		14
# 5 		11
# 5 		14
# 6 		9
# 
# To read all this information and make sense of how it relates, we would first look in the musicians table and find the musician we want—for instance Geddy Lee. 
# We find his player_id, 2, and use that value to look in the what_they_play table. 
# In that table, two entries for his player_id map to two instr_ids: 12 and 14. 
# Taking those two values, we use them as the keys in the instruments table and find that Geddy Lee plays the bass and sings for his band.
# 
#
# Need to start 
