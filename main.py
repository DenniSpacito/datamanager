# Imports for plotting graphs and general mathematics
import math
import matplotlib.pyplot as plot 
import statistics
import argparse

# argparse stuff
# parser = argparse.ArgumentParser()
# parser.parse_args()

# User chooses what mode they want to enter the program in.
def start_program():
  if __name__ == "__main__":
    start_mode = input("""Would you like to graph your data, get a statistical summary, see information on each, or see the about? (1/2/3/4)""")
    if start_mode == "1":
      graph()
    elif start_mode == "2":
      summarize()
    elif start_mode == "3":
      print("""
      1.) Graphing will allow you to input x and y values, and make a graph of a line (or multiple).
      2.) Statistical Summary will give you the mean, median, and mode.
      """)
      kill()
    elif start_mode == "4":
      print(""""
      This program was originally made as a final project for
      AP Computer Science, but evolved into what has become
      my first ever python project of any actual  value.
      """")

    else:
        print("Please enter a valid number")

# Graphing function
def graph():
        # Checks if the user wants to label the x and y axis.
    labels_question = input("Would you like labels on the x and y axis? (y/n)")
    
    if labels_question == "y":
        plot.xlabel(input("What would you like your x-axis to be labeled?"))
        plot.ylabel(input("What would you like your y-axis to be labeled?"))
    else:
        pass
        
    # Checks if the user wants to name their graph
    name_question = input("Would you like to name your graph? (y/n)")
    if name_question == "y":
        plot.title(input("What would you like to name your graph?"))
    else:
        pass
    line_count = int(input("How many lines would you like to create?"))
    
    x_vals = [] # List of x values
    y_vals = [] # List of y values
    line_names = [] # List of line names 
    
    # User inputs data for lines
    for i in range(line_count):
        
        try:
          # Adds the name of the lines to the line_names list
          name = input(f"What do you want to name line {i + 1}?")
          line_names.append(name)
        
          print(f"Now enter your data values for line {i + 1}")
          # Creates the list of x values.
          x_count = int(input("How many x values would you like in your graph?"))
          x_values = [int(input("Enter an x value: ")) for _ in range(x_count)]
        
          # Creates the list of y values.
          y_count = int(input("How many y values would you like in your graph?"))
          y_values = [int(input("Enter a y value: ")) for _ in range(y_count)]
        
          # Turns the lists into tuples and appends them to x_vals and y_vals (master list of coords)
          x_vals.append(tuple(x_values))
          y_vals.append(tuple(y_values))
        except ValueError:
          print("Make sure you are inputting INTEGER values for your data.")
          kill()
    # Plots the lines and names them
    for i in range(line_count):
      try:
        plot.plot(x_vals[i], y_vals[i], label = line_names[i])
      except:
        print("Please give valid x and y values for your plot.")
        kill()
    print("Creating graph...")
    plot.show()
    # Either exits program or restarts
    exit_or_continue = input("Would you like to continue or leave the program? (exit/continue")
    if exit_or_continue == "exit":
      exit()
    elif exit_or_continue == "continue":
      kill()
    
# Data summary function

def summarize():
  values = []
  # Creates a list of numerical data based off user input.
  try:
    value_count = int(input("How many values would you like to use?"))
  except: 
    print("Enter a valid number.")
    summarize()
  for _ in range(value_count):
      try:
        value = int(input("Input a numerical data value."))
      except ValueError: 
        print("Please enter valid numberical data.")
        kill()
      values.append(value)
  # Prints Mean, Median, and Mode using statistics module functions.
  print(f"""
    MEAN: {statistics.fmean(values)}
    MEDIAN: {statistics.median(values)}
    MODE: {statistics.mode(values)}
    """)
  # Either exits program or restarts
  exit_or_continue = ""
  while exit_or_continue != "exit" or exit_or_continue != "continue":
    exit_or_continue = input("Would you like to continue or leave the program? (exit/continue")
    if exit_or_continue == "exit":
      exit()
    elif exit_or_continue == "continue":
      kill()
    
# Restarts the program
def kill():
    start_program()

start_program()
