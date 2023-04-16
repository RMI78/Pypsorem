import argparse
from lorem import Lorem

def main(args):
    assert args.what in ["paras", "words", "lists", "bytes"]
    assert type(args.amount) == int
    assert type(args.start_with_lipsum) == bool
    lorem = Lorem(args.what, args.amount, args.start_with_lipsum)
    print(lorem)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--version', help='Show program\'s version number and exit.', action='store_true')    
    parser.add_argument('-s','--start-with-lipsum', help='Whether or not your text start your text with "Lorem Ipsum dolore sit amet..."', action='store_true')
    parser.add_argument('-w','--what', help='The type of each text structure that will be returned. Choose from "lists"/"paras" (paragraphs), "words", or "bytes"', type=str)
    parser.add_argument('-a','--amount', help='The number of text structures that will be returned.', type=int)
    args = parser.parse_args()
    main(args)