from tinydb_helper.helper import Table
from tinydb import TinyDB
import time


def main() -> None:
    db = TinyDB("db.json")
    timestamp = str(int(time.time()))
    project = Table(db=db, table="project", primary_key="proj_id")
    person = Table(db=db, table="person", key_gen=lambda: timestamp)

    for i in range(4):
        project.insert(dict(name=f"test-{i}", year=f"{2004 + i}"))
        person.insert(dict(first=f"first-{i}", year=f"{2004 + i}"))


if __name__ == "__main__":
    main()
