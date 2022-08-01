import json
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", type=str, help="Name of the attribute to check")
parser.add_argument(
    "-g",
    "--globally",
    action="store_true",
    help="Check for globally unique values across all models",
)

if __name__ == "__main__":
    args = parser.parse_args()
    schemas = Path(__file__).parent.parent.resolve() / "models"
    values = {}
    for model_file in schemas.glob("*.json"):
        model = model_file.stem.split("-")[-1]
        values[model] = set()
        with model_file.open() as fp:
            data = json.load(fp)
        for field in data["fields"]:
            values[model].add(field[args.name])

    if args.globally:
        print("Unique values across all models:")
        for val in set.union(*values.values()):
            print(f"  - {val}")
    else:
        for model in values:
            print(f"{model}.{args.name}:")
            for val in values[model]:
                print(f"  - {val}")
            print()
