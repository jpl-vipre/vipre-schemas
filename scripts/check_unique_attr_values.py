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
