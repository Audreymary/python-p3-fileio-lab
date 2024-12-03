# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes content to a file. Creates a new file with a .txt extension.
    """
    with open(file_name + ".txt", 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends content to an existing file. If the file does not exist, it creates the file.
    """
    with open(file_name + ".txt", 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads content from a file and returns it.
    """
    with open(file_name + ".txt", 'r') as file:
        return file.read()
