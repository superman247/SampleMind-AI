import argparse
from cli.importer import import_samples


def main():
    parser = argparse.ArgumentParser(description="🎧 SampleMind AI CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 📥 Import command
    import_parser = subparsers.add_parser("import", help="Import WAV samples")
    import_parser.add_argument("source", type=str, help="Path to the sample folder")

    args = parser.parse_args()

    if args.command == "import":
        import_samples(args.source)

if __name__ == "__main__":
    main()
