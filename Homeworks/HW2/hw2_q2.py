"""
Author: [Your name here]
Assignment / Part: HW2 - Q1 (etc.)
Date due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import math

frequency = float(input("Enter a value for the frequence, w:"))
duration = float(input("Enter a value for the duration of the sound wave, T:"))


amplitude = ((2*math.sin(frequency*duration))/frequency)

rounded_amplitude = round(amplitude, 3)


print("The amplitude spectrum of this Fourier transform is:", rounded_amplitude)