import argparse

from bump2release.release_flow import run_release_flow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bump_type", help="Major / Minor / Patch etc.")
    parser.add_argument("tag_message", help="annotated tag message")
    args = parser.parse_args()
    bump_type = args.bump_type
    tag_message = args.tag_message
    run_release_flow(bump_type, tag_message)


if __name__ == "__main__":
    main()
