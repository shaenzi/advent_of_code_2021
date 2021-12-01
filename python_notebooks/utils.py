from aocd import get_data

Vector = list[str]

def get_data_as_list(day: int) -> Vector:
    """given the day as an int, this function uses the get_data from the aocd package to get the data from the advent of code website 
    (which needs an access token, see https://pypi.org/project/advent-of-code-data/ or https://github.com/wimglenn/advent-of-code-wim/issues/1)
    then parses this into a list of strings, with each item representing one line
    """
    
    raw_data = get_data(day = day)
    
    # data is now one long string. write to file
    file = open(r"temp.txt","w+")
    file.write(raw_data)
    file.close()
    
    # read lines from file
    file = open("temp.txt", "r")
    data_list = file.readlines()
    file.close()
    
    # take away the new line character
    data_list = [x.rstrip("\n") for x in data_list]
    
    return data_list