import json
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", type=str, help="Name of the attribute to add to each field")

if __name__ == "__main__":
    args = parser.parse_args()
    schemas = Path(__file__).parent.parent.resolve() / "models"
    for model in schemas.glob("*.json"):
        print(f"Removing {args.name} attribute from all fields in {model.stem.split('-')[-1]} model")
        with model.open() as fp:
            data = json.load(fp)
        for field in data["fields"]:
            if args.name not in field:  # Ensure that attribute is present in field
                print("Field does not have attribute")
                continue
            del field[args.name]  # Delete the attribute from the field
        with model.open("w") as fp:
            json.dump(data, fp, indent=2)
