# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes content to a file. Creates a new file with a .txt extension.
    """
    try:
        with open(file_name + ".txt", 'w') as file:
            file.write(file_content)
    except Exception as e:
        print(f"Error writing file: {e}")

def append_file(file_name, append_content):
    """
    Appends content to an existing file. If the file does not exist, it creates the file.
    """
    try:
        with open(file_name + ".txt", 'a') as file:
            file.write(append_content)
    except Exception as e:
        print(f"Error appending file: {e}")

def read_file(file_name):
    """
    Reads content from a file and returns it.
    """
    try:
        with open(file_name + ".txt", 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
