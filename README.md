shocksInBurgersEquation
=======================

Finding shocks in Burger's Inviscid Equation given a continuous initial function.

This program is used to find the shock in the system of Burger's invisicid equation given a continuous initial function. The user is given a list of functions (at the time of writing, the list of functions is the Gaussian from -10 to 10, the hyperbolic tangent from -10 to 10, and a sine from 0 to pi) from which they can choose which function they want to see the shocks of. The program then will calculate when the first shock occurs. Once this shock has been reached, it shows a plot of the initial function that is unaltered along with the altered function that has stopped at the first shock. After this graph is closed, the program will loop through the remaining time values, and find the shock at that time value using the equal area rule. To do this, it splits up the function into it's upper section, middle section, and bottom section. Then, it finds the midpoint of the top section and uses that as a guess for where the shock is located. It then takes the integral of the left and right sides of the sectioned off function, and changes the guess until it has a close approximation to where the shock is located. This sectioned off view of the function and the value at where the integral ends of working at is then shown in a graph (all of this is a little hard to explain, but the graph should show what I am talking about here). After this, it calculates the characteristics, and plots the values that were found for the shocks on the characteristic plot. The program then does a simply animation of the initial function as time progresses. 
