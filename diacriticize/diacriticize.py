import random
import argparse


def diacriticize(input_string: str, times: int = 4, unsafe_range: bool = False) -> str:
    """
    Combine input strings with random diacritical marks.

    Parameters
    ----------
    input_string : str
        String to combine
    times : int, default 4
        Number of diacritical marks to combine
    unsafe_range : bool, default False
        Use characters not visible in common fonts

    Returns
    -------
    combined : str
        Combined string
    """

    if unsafe_range:
        unicode_ranges = (
            (768, 879),
            (6832, 6911),
            (7616, 7679),
            (8400, 8447),
            (65056, 65071),
        )
    else:
        unicode_ranges = ((768, 879),)

    diacritical_marks = []

    for r in unicode_ranges:
        for i in range(r[0], r[1]):
            diacritical_marks.append(chr(i))

    out = ""

    for char in input_string:
        dm = random.choices(diacritical_marks, k=times)
        dm = "".join(dm)
        char += dm

        out += char

    return out


def cli():
    parser = argparse.ArgumentParser(
        prog="diacriticize",
        description="combine input chars with random diacritical marks",
    )
    parser.add_argument("input")
    parser.add_argument(
        "--times",
        "-t",
        type=int,
        default=4,
        help="number of diacritical marks to combine (default: 4)",
    )
    parser.add_argument(
        "--unsafe-range",
        "-u",
        action="store_true",
        help="use characters not visible in common fonts",
    )

    args = parser.parse_args()

    out = diacriticize(args.input, args.times, args.unsafe_range)

    print(out, end="")


if __name__ == "__main__":
    cli()
