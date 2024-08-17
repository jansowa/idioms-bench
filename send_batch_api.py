from openai import OpenAI
import argparse


def main():
    parser = argparse.ArgumentParser(description="Script that generates evaluations for the benchmark.")
    parser.add_argument('--input_file', type=str, help='path of input file')
    parser.add_argument('--api_key', type=str, help='OpenAI API key')

    args = parser.parse_args()

    client = OpenAI(api_key=args.api_key)
    batch_input_file = client.files.create(
        file=open(args.input_file, "rb"),
        purpose="batch"
    )

    batch_input_file_id = batch_input_file.id

    client.batches.create(
        input_file_id=batch_input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )



if __name__ == "__main__":
    main()