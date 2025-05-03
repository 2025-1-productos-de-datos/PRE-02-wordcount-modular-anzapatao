import os
import subprocess

from homework.src.wordcount import main


def test_migration():
    try:
        subprocess.run(
            ["python3", "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    if not os.path.exists("data/output/wordcount.tsv"):
        raise FileNotFoundError("El archivo wordcount.tsv no existe.")

    wordcount = {}
    with open("data/output/wordcount.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        wordcount[key] = value

    assert (
        wordcount.get("statistics", 0) == "3"
    ), "The word 'statistics' should appear '3' times."
    assert (
        wordcount.get("interpretation", 0) == "2"
    ), "The word 'interpretation' should appear '2' times."
    assert (
        wordcount.get("analytics", 0) == "5"
    ), "The word 'analytics' should appear '5' times."
    assert wordcount.get("data", 0) == "19", "The word 'data' should appear 19 times."
    assert wordcount.get("data", 0) == "19", "The word 'data' should appear 19 times."
    assert wordcount.get("data", 0) == "19", "The word 'data' should appear 19 times."
