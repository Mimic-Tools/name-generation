import argparse
import yaml
import random

def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("origin", type=str, choices=[
        "human",
        "dwarf",
        "any"
    ], default="any")
    parser.add_argument("gender", type=str, choices=[
        "male",
        "female",
        "neutral",
        "any"
    ], default="any")
    args = parser.parse_args()
    return args


class NameBank():
    def __init__(self, nametype, origin="", gender=""):
        prepender = lambda x: f"-{x}" if x != "" else ""
        self.origin = prepender(origin).lower()
        self.gender = prepender(gender).lower()
        self.filenames = [f"name-segments/{nametype}{self.origin}.txt"]
        if gender != "":
            self.filenames.append(f"name-segments/{nametype}{self.origin}{self.gender}.txt")

    def generate(self):
        # TODO: Actually randomize this
        for fn in self.filenames:        
            try:
                with open(fn, "r") as f:
                    lines = f.read().splitlines()
                    name = random.choice(lines)
                    return name
            except FileNotFoundError:
                print(f"Warn: No such file: {fn}")
        print("Error: No valid names in bank")
        quit()


class Generator():

    def __init__(self, args):
        # TODO: Actually randomize these
        if args.origin == "any":
            args.origin = "dwarf" 
        if args.gender == "any":
            args.gender = ""

        self.origin = args.origin
        self.gender = args.gender

        self.filename = "name-configurations/"+args.origin.lower()+".yml"
        with open(self.filename) as f:
            constructor = yaml.load(f, Loader=yaml.FullLoader)
            self.origin = constructor["origin"]
            # TODO: handle aliasing / choice
            self.construction = constructor["construction"]
            self.banks = constructor["name_banks"]



    def generate(self):
        name = ""
        for x in self.construction:
            key = list(x.keys())[0]
            b = self.banks[0]
            nb = NameBank(key, origin=self.origin, gender=self.gender)

            n = nb.generate()
            name += n + " "
        return name.rstrip()

def main():
    a = setup_args()
    ng = Generator(a)
    print("Suggested Name: ", ng.generate())


if __name__ == '__main__':
    main()