from openai import OpenAI
import argparse
import os
import glob


def main():
    parser = argparse.ArgumentParser(description="Script that generates evaluations for the benchmark.")
    parser.add_argument('--input_file', type=str, help='path of input file')
    parser.add_argument('--input_directory', type=str, help='path of directory containing .jsonl files')
    parser.add_argument('--api_key', type=str, help='OpenAI API key')

    args = parser.parse_args()

    client = OpenAI(api_key=args.api_key)

    if args.input_file:
        process_file(client, args.input_file)
    elif args.input_directory:
        process_directory(client, args.input_directory)
    else:
        print("Please provide either --input_file or --input_directory")


def process_file(client, file_path):
    batch_input_file = client.files.create(
        file=open(file_path, "rb"),
        purpose="batch"
    )

    batch_input_file_id = batch_input_file.id

    client.batches.create(
        input_file_id=batch_input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )


def process_directory(client, directory_path):
    jsonl_files = glob.glob(os.path.join(directory_path, "*.jsonl"))

    for file_path in jsonl_files:
        print(f"Processing file: {file_path}")
        process_file(client, file_path)


if __name__ == "__main__":
    main()