# Imports for plotting graphs and general mathematics
import math
import matplotlib.pyplot as plot 
import statistics
import sys

# User chooses what mode they want to enter the program in.
def start_program():
  if __name__ == "__main__":
    start_mode = input("""Would you like to:
    1.) Line graph of your data
    2.) Summary of your data (mean,median,mode,standard deviation)
    3.) Help
    4.) About
     (1/2/3/4)""")
    if start_mode == "1":
      graph()
    elif start_mode == "2":
      summarize()
    elif start_mode == "3":
      print("""
      1.) Graphing will allow you to input x and y values, and make a graph of a line (or multiple).
      2.) Statistical Summary will give you the mean, median, and mode.
      """)
      restart()
    elif start_mode == "4":
      print(""""
      This program was originally made as a final project for
      AP Computer Science, but evolved into what has become
      my first ever python project of any actual  value.
      """)
      restart()
    else:
        print("Please enter a valid number")
        restart()

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
    try: 
      line_count = int(input("How many lines would you like to create?"))
    except ValueError:
      print("Input a integer value, please.")
      graph()
    
    line_names = [] # List of line names 
    x_vals = []
    y_vals = []
    # User inputs data for lines
    for i in range(line_count):
        
        try:
          # Adds the name of the lines to the line_names list
          name = input(f"What do you want to name line {i + 1}?")
          line_names.append(name)
        
          print(f"Now enter your data values for line {i + 1}")
          # Creates a list of x and y values
          x_val = list(input("Enter your x values, seperated by a comma (no space)").split(","))
          y_val = list(input("Enter your y values, seperated by a comma (no space)").split(","))
          # Converts x values to integers
          for i in range(0, len(x_val)):
            x_val[i] = int(x_val[i])
          for i in range(0, len(y_val)):
            y_val[i] = int(y_val[i])
          x_vals.append(tuple(x_val))
          y_vals.append(tuple(y_val))
        except ValueError: 
          print("Make sure you are inputting INTEGER values for your data.")
          graph()
    # Plots the lines and names them
    try:
      for i in range(line_count):
        plot.plot(x_vals[i], y_vals[i], label = line_names[i])
      print("creating graph...")
      plot.legend()
      plot.show()
    except ValueError:
      print("Please input valid integers.")
      graph()
    # Either exits program or restarts
    exit_or_continue = input("Would you like to continue or leave the program? (exit/continue")
    if exit_or_continue == "continue":
      restart()
    else: 
      sys.exit()

    
# Data summary function
def summarize():
  value = list(input("Input your values, seperated by a comma (no space)").split(","))
  values = []
  for i in range(len(value)):
    try:
      values.append(int(value[i]))
    except ValueError:
      print("""Be sure you are entering valid integers and following the rules (Seperate values with a comma, without any spaces""")
      summarize()
    
  # Prints the statistics using statistics module functions.
  # Checks if the user wants to round
  round_ = input("Would you like to round your results? (y/n)")
  if round_ == "y":
    try: 
      i = int(input("How many decimals do you want to round to?: "))
    except ValueError:  
      print("Please use a valid integer value.")
      summarize()
    try:
      print(f"""
      MEAN: {round(statistics.fmean(values), i)}
      MEDIAN: {round(statistics.median(values), i)}
      MODE: {round(statistics.mode(values), i)}
      STANDARD DEVIATION: {round(statistics.stdev(values), i)}
      """)
    except statistics.StatisticsError:
      print("Please enter more then one value.") 
      summarize()
  else: 
    try:
      print(f"""
        MEAN: {statistics.fmean(values)}
        MEDIAN: {statistics.median(values)}
        MODE: {statistics.mode(values)}
        STANDARD DEVIATION: {statistics.stdev(values)}
        """)
    except statistics.StatisticsError:
      print("Please enter more then one value. ")
      summarize()
    


  # Either exits program or restarts
  exit_or_continue = input("Would you like to continue or leave the program? (exit/continue)")
  if exit_or_continue == "continue":
    restart()
  else: 
    sys.exit()
    
# Restarts the program
def restart():
    start_program()

start_program()
