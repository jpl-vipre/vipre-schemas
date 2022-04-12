import json
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", type=str, help="Name of the attribute to add to each field")
parser.add_argument(
    "-v", "--value", help="Default value to initialize the added attribute"
)
parser.add_argument(
    "-f",
    "--force",
    action="store_true",
    help="Force writing the specified value if attr already exists",
)

if __name__ == "__main__":
    args = parser.parse_args()
    schemas = Path(__file__).parent.parent.resolve() / "models"
    default_value = args.value if args.value is not None else f"TODO:{args.name}"
    print(f"Adding {args.name} attribute with default value: {default_value}")
    for model in schemas.glob("*.json"):
        print(f"Adding {args.name} to all fields in {model.stem.split('-')[-1]} model")
        with model.open() as fp:
            data = json.load(fp)
        for field in data["fields"]:
            if args.name in field and not args.force:
                continue
            field[args.name] = default_value
        with model.open("w") as fp:
            json.dump(data, fp, indent=2)
