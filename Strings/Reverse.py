
def Reverse(*collection):
    """Reverse the String elements in the Collection"""
    cnt = 0
    result = ""
    revlst = []

    for word in collection:
        while cnt < len(word):
            result += word[len(word) - 1 - cnt]
            cnt += 1
        # print(result) # Can print Individual Result
        revlst.append(result) # Append Result to a List
        result = "" # Reset Variable
        cnt = 0 # Reset Variable
    
    print(revlst) # Print Reversed List

Reverse("Mrinal","Smith","Molu","Goosy") # Calling Reverse Method - ['lanirM', 'htimS', 'uloM', 'ysooG']
