# itemapp.py
import sqlite3


def conncet(name):
    con = sqlite3.connect(name);
    return con;
def close(*cs):
    for c in cs:
        if c is not None:
            c.close();

def makeTable():
    return None;

def insert():
    return None;

def delete():
    return None;

def update():
    return None;

def selectone():
    return None;

def select():
    return None;
