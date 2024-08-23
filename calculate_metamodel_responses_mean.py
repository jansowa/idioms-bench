import pandas as pd
import os
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Script that sends prompts to metamodel by batch api")
    parser.add_argument('--input_directory', type=str, default="data/batch_response", help='path of directory containing .jsonl files')
    parser.add_argument("--output_file", type=str, help="Path of output csv file")

    args = parser.parse_args()

    directory = args.input_directory
    results = []

    # Iteracja przez wszystkie pliki CSV w folderze
    for filename in os.listdir(directory):
        contents = []
        if filename.endswith(".jsonl"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    # Parsujemy linię jako obiekt JSON
                    data = json.loads(line)

                    # Wyciągamy pierwszą odpowiedź z pola "choices"
                    content = data['response']['body']['choices'][0]['message']['content']

                    # Dodajemy pole "content" do listy
                    contents.append(content)
            df = pd.DataFrame(contents, columns=['content'])
            df['content'] = df['content'].str.strip('"')
            sum_wydzwiek = 0
            sum_ocena = 0
            sum_zwiazki = 0

            count_wydzwiek = 0
            count_ocena = 0
            count_zwiazki = 0
            # Iteracja przez każdą komórkę w kolumnie 'cleaned_evaluation_answer'
            for cell in df['content']:
                # Rozdzielenie komórek na poszczególne obiekty JSON
                json_objects = cell.split('\n')

                for obj in json_objects:
                    # Zamiana tekstu na obiekt JSON
                    try:
                        data = json.loads(obj)

                        # Sumowanie wartości dla "WYDŹWIĘK"
                        if "WYDŹWIĘK" in data:
                            sum_wydzwiek += int(data["WYDŹWIĘK"])
                            count_wydzwiek += 1

                        # Sumowanie wartości dla "OCENA"
                        if "OCENA" in data:
                            sum_ocena += int(data["OCENA"])
                            count_ocena += 1

                        # Sumowanie wartości dla "ZWIĄZKI"
                        if "ZWIĄZKI" in data:
                            sum_zwiazki += int(data["ZWIĄZKI"])
                            count_zwiazki += 1
                    except:
                        print("Some problems!")
            # Obliczanie średnich dla pliku
            average_wydzwiek = sum_wydzwiek / count_wydzwiek if count_wydzwiek > 0 else 0
            average_ocena = sum_ocena / count_ocena if count_ocena > 0 else 0
            average_zwiazki = sum_zwiazki / count_zwiazki if count_zwiazki > 0 else 0
            mean_value = (average_wydzwiek + average_ocena + average_zwiazki) / 3

            # Dodanie wyników do listy
            results.append({
                "Model": filename,
                "Rozmiar": "",
                "Średnia": mean_value,
                "Analiza wydźwięku": average_wydzwiek,
                "Zrozumienie tekstu": average_ocena,
                "Znajomość związków frazeologicznych": average_zwiazki
            })

    # Konwersja wyników na DataFrame
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="Średnia", ascending=False)
    results_df.to_csv(args.output_file)

    data_dict = results_df.to_dict('records')
    with open(args.output_file[:-4] + '.json', 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()