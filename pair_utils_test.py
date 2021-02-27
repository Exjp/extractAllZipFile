from pair_utils import *

test_counter = 0

try:
    CA_pair()
    print("---Successfully generated CA pair---")
    test_counter+=1
except:
    print("---Unable to generate CA pair---")

try:
    client_pair("test")
    print("---Successfully generated client pair---")
    test_counter+=1
except:
    print("---Unable to generate client pair---")

print("---Test passed: " + str(test_counter) + "/2---")
