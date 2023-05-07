# Copyright (c) 2021-2023 California Institute of Technology ("Caltech"). U.S.
# Government sponsorship acknowledged.
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Caltech nor its operating division, the Jet Propulsion
#   Laboratory, nor the names of its contributors may be used to endorse or
#   promote products derived from this software without specific prior written
#   permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

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
