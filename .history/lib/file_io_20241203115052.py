# test_file_io.py
import os
from lib.file_io import write_file, append_file, read_file

def test_write_file():
    write_file("testfile", "First log")
    with open("testfile.txt", 'r') as file:
        content = file.read()
    assert content == "First log"

def test_append_file():
    append_file("testfile", " Second log")
    with open("testfile.txt", 'r') as file:
        content = file.read()
    assert content == "First log Second log"

def test_read_file():
    content = read_file("testfile")
    assert content == "First log Second log"

def test_file_creation():
    write_file("newfile", "Test content")
    assert os.path.exists("newfile.txt") == True
