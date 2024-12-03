# lib/testing/file_io_test.py

from lib.file_io import write_file, append_file, read_file  # Correct import

def test_write_file():
    write_file("testfile", "First log\n")
    with open("testfile.txt", 'r') as file:
        content = file.read()
    assert content == "First log\n"

def test_append_file():
    append_file("testfile", " Second log\n")
    with open("testfile.txt", 'r') as file:
        content = file.read()
    assert content == "First log\n Second log\n"

def test_read_file():
    content = read_file("testfile")
    assert content == "First log\n Second log\n"

# Test write, append, and read
test_write_file()
test_append_file()
test_read_file()

print("All tests passed successfully!")
