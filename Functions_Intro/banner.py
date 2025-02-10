# def banner_text(text="", width=80):  # Default parameters
def banner_text(text: str = " ", width: int = 80) -> None:
    """ Print a string centered, with ** either side

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at the left
        and right edges.
    :param width: The overall width to print within (including the 4
        spaces for the ** either side).
    :raise ValueError: if the supplied string is too long to fit.
    """
    if len(text) > width - 4:
        raise ValueError("String {0} is larger then specified width {1}."
                         .format(text, width))

    if text == "*":
        print("*" * width)
    else:
        centered_text = text.center(width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,", 80)
banner_text(width=80)  # keyword argument - positional-or-keyword, either pass the arguments by position or name as
# keyword
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And...always look on the bright side of life...")
banner_text("*")
