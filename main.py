

import sys
from collate_links import collate_links
from bs import generatePDF

def main():
    # if len(sys.argv) != 2:
    #     print("Usage: python main.py <url to reddit user>")
    #     return

    try:
       
        # user_input = sys.argv[1]
        user_input = ""
        array_of_links = collate_links(user_input)
        for link in array_of_links:
            generatePDF(link)
    except ValueError:
        print("Invalid input. Please enter a valid url.")


if __name__ == "__main__":
    main()

    