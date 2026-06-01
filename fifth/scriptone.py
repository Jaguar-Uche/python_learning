# At the top close to the play button, tap the : something and tap edit run configurations
# you press plus by the side(add new configuration) and then you will see python ,and then you will add python
# then add scriptone and scripttwo to it.
# Select scriptone for this one to work
# You will now see a dropdown by the side of the play button showing you the run configurations script you can run with
# The run configuration is for the main python file

from scripttwo import *

# print(dir())
# Imports run first na so the imported one shows first that's why the first one shows scripttwo and the second one shows __main__
print(__name__)
# This returns __main__ that's why you check with if __name__ == __main__
# It returns main because scriptone is the file I am running with in the script configurations