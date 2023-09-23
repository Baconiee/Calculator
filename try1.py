current_text = "-3x6"

if current_text and current_text[-1].isdigit() or "." in current_text:

        i = len(current_text) - 1

        while i >= 0 and current_text[i].isdigit() or current_text[i] == ".":
            i -= 1

        operation = i
        if current_text[operation] == "x":
              print("Yes")