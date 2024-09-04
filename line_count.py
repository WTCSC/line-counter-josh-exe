def line_count():
    
    file = open('file.txt', 'r')                # Opens file.txt as read only.

    lines = len(file.readlines())               # Counts the number of lines.

    file.close()                                # Closes the file.

    return lines                                # Returns the number of lines.