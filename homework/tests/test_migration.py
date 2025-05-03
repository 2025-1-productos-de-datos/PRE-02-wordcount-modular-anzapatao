import os

from homework.src.wordcount import main


def test_migration():
    main()
    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")

    results = {}
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = value

    assert (
        results.get("statistics", 0) == "3"
    ), "The word 'statistics' should appear '3' times."
    assert (
        results.get("interpretation", 0) == "2"
    ), "The word 'interpretation' should appear '2' times."
    assert (
        results.get("analytics", 0) == "5"
    ), "The word 'analytics' should appear '5' times."
    assert results.get("data", 0) == "19", "The word 'data' should appear 19 times."
    assert results.get("data", 0) == "19", "The word 'data' should appear 19 times."
    assert results.get("data", 0) == "19", "The word 'data' should appear 19 times."
