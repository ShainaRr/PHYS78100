# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
""" 
Ex 7.2
In the on-line resources there is a file called sunspots.txt, which contains the observed number of sunspots 
on the Sun for each month since January 1749. The file contains two columns of numbers, the first representing the 
month and the second being the sunspot number.
a) Writeaprogramthatreadsthedatainthefileandmakesagraphofsunspotsasafunction of time. You should see that the number
 of sunspots has fluctuated on a regular cycle for as long as observations have been recorded. Make an estimate of 
 the length of the cycle in months.
b) Modify your program to calculate the Fourier transform of the sunspot data and then make a graph of the magnitude
 squared |ck|2 of the Fourier coefficients as a function of k—also called the power spectrum of the sunspot signal. 
 You should see that there is a noticeable peak in the power spectrum at a nonzero value of k. The appearance of t
 his peak tells us that there is one frequency in the Fourier series that has a higher amplitude than the others around
  it—meaning that there is a large sine-wave term with this frequency, which corresponds to the periodic wave you can see 
  in the original data.
c) Find the approximate value of k to which the peak corresponds. What is the period of the sine wave with this value of k? 
You should find that the period corresponds roughly to the length of the cycle that you estimated in part (a).
This kind of Fourier analysis is a sensitive method for detecting periodicity in signals. Even in cases where it is not 
clear to the eye that there is a periodic component to a signal, it may still be possible to find one using a Fourier transform."""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy as np


