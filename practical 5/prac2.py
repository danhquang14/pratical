COLOR_NAMES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc", "BLACK": "#000000",
               "BLANCHEDALMOND": "#ffebcd", "BlUEVIOLET": "#8a2be2", "BROWN": "#a52a2a", "BURLYWOOD": "#deb887",
               "CADETBLUE": "#5f9ea0", "CHOCOLATE": "#d2691e"}

# print(COLOR_NAMES)
color = input("Enter the color:")
while color != " ":
    if color.upper() in COLOR_NAMES :
        print("The code of {} is {}".format(color,COLOR_NAMES[color.upper()]))
        break
    else:
        print("this color not available in list")
        color = input("Enter the color:")