import sys
import os

# Добавляем корневую папку проекта в пути для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import hello_world

def test_hello():
    assert hello_world() == "hello world"