import html
from termcolor import colored

print(colored(r"""
|-------------------------------------------------------------------|
|     =========== ____        ____     ________   ======||======    |
|         ||       ||          ||     ||                ||          |
|         ||       ||          ||     ||                ||          |
|         ||       ||          ||     ||======||        ||          |
|         //        \\         //             ||        ||          |
| \\_____//          \\=======//       _______||        ||          |
|                                                                   |
|      __________          ________      ___________ ======||====== |
|      ||        \\      //      ` \\         ||           ||       |
|      ||         \\    //          \\        ||           ||       |
|      ||          \\  //            \\       ||           ||       |
|      ||          //  \\            //       ||           ||       |
|      ||         //    \\          //        ||           ||       |
|      ||________//      \\________//    _____||_____      ||       |
|                                                                   |
| CODED BY:@muslimfrompk                                            |
|-------------------------------------------------------------------|""","green"))   
def get_option():
    option=input(colored('Choose action below you want to perform:\n    1-Auto HTML Encode/Decode\n    2-Encode HTML\n    3-Decode HTMl\n    4-Exit\n---=>',"blue"))
    if option=='1' or option=='2' or option=='3':
        return option
    elif option=='4':
        print(colored("Goodbye!\nTerminating the program......","green"))
        exit(0)
    else:
        print(colored("Enter a valid option","red"))
        main()
def get_value():
    value=str(input(colored("Enter the value you want to Encode/Decode:","blue")))
    return value
def main():
    option=get_option()
    value=get_value()
    border_for_encode="\n|----------------"+"--"*len(html.escape(value))+"|>\n "
    border_for_decode="\n|----------------"+"--"*len(html.unescape(value))+"|>\n "
    if option=='1':
        decoded_value=html.unescape(value)
        if decoded_value==value:
            print(colored(border_for_encode+"Encoded value---=> "+html.escape(value)+border_for_encode,"green"))
            main()
        elif value==html.escape(decoded_value):
            print(colored(border_for_decode+"Decoded value---=> "+decoded_value+border_for_decode,"green"))
            main()
        else:
            print(colored("An error was occured while trying to Encode/Decode given value.\nPlease open an issue at our GitHub project","red"))
    elif option=='2':
        print(colored(border_for_encode+"Encoded value---=> "+html.escape(value)+border_for_encode,"green"))
        main()
    elif option=='3':
        print(colored(border_for_decode+"Decoded value---=> "+html.unescape(value)+border_for_decode,"green"))
        main()
    else:
        main()
main()
