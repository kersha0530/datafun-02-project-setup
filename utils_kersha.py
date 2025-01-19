"""
Module: utils_kersha

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Kersha Broussard

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True 
is_employee_active: bool = True
is_vip_client: bool = False

# Define a boolean variable
is_sustainable_business: bool = True

# Another integer variable
number_of_certifications: int = 8

# Another list of strings
tools_used: list = ["SQL", "GitHub", "Python", "Docker", "AWS"]


# Print additional variables to verify
print(f"Sustainable Business: {is_sustainable_business}")
print(f"Number of Certifications: {number_of_certifications}")
print(f"Tools Used: {', '.join(tools_used)}")

# Additional variables - revenue
monthly_revenues: list = [15000, 18000, 17500, 16000, 20000, 19000]

# Byline using f-string
byline: str = f"""
Over the past six months, my business has achieved an average monthly revenue of ${sum(monthly_revenues)/len(monthly_revenues):,.2f}.
Our highest revenue month brought in ${max(monthly_revenues):,.2f}.
"""
print(byline)


# Monthly revenue list
monthly_revenues = [15000, 18000, 17500, 16000, 20000, 19000]

# Calculate statistics
min_revenue = min(monthly_revenues)  # Minimum revenue
max_revenue = max(monthly_revenues)  # Maximum revenue
mean_revenue = statistics.mean(monthly_revenues)  # Mean (average) revenue
stdev_revenue = statistics.stdev(monthly_revenues)  # Standard deviation of revenue

# Print results
print("Monthly Revenue Analysis")
print(f"Monthly Revenues: {monthly_revenues}")
print(f"Minimum Revenue: ${min_revenue:,.2f}")
print(f"Maximum Revenue: ${max_revenue:,.2f}")
print(f"Mean Revenue: ${mean_revenue:,.2f}")
print(f"Standard Deviation of Revenue: ${stdev_revenue:,.2f}")

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 12

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.4

# Import the statistics module for calculations
import statistics
# declare a list of strings
# TODO: Add or replace this with your own list 


# Service detail variables
name: str = "Kersha Broussard"
operates_globally: bool = True
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence","Web Development","Data Science", "Cybersecurity", "Cloud Computing"]

# Byline using f-string
byline: str = f"""
I'm {name}, and I {'' if operates_globally else 'do not '}offer services globally.
My areas of expertise include:
- {', '.join(skills_offered)}.
"""
print(byline)


# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7, 4.5, 4.9]


# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names

# Added monthly revenue list
monthly_revenues = [15000, 18000, 17500, 16000, 20000, 19000]

# Calculate statistics
min_revenue = min(monthly_revenues)
max_revenue = max(monthly_revenues)
mean_revenue = statistics.mean(monthly_revenues)
stdev_revenue = statistics.stdev(monthly_revenues)

# Updated byline with monthly revenue analysis
byline: str = f"""
---------------------------------------------------------
Broussard Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Employee Active:          {is_employee_active}
Is VIP Client:               {is_vip_client}
Years in Operation:          {years_in_operation}
Average Client Satisfaction: {average_client_satisfaction:.2f}
Skills Offered:              {", ".join(skills_offered)}
Client Satisfaction Scores:  {client_satisfaction_scores}
Minimum Satisfaction Score:  {min_score}
Maximum Satisfaction Score:  {max_score}
Mean Satisfaction Score:     {mean_score:.2f}
Standard Deviation of Scores: {stdev_score:.2f}

---------------------------------------------------------
Monthly Revenue Analysis
---------------------------------------------------------
Monthly Revenues:           {monthly_revenues}
Minimum Revenue:            ${min_revenue:,.2f}
Maximum Revenue:            ${max_revenue:,.2f}
Mean Revenue:               ${mean_revenue:,.2f}
Standard Deviation:         ${stdev_revenue:,.2f}
"""

# Print the byline
print(byline)

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
