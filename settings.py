EVALUATED_MODEL_INSTRUCT: str = """ROLA:
\"\"\"Jesteś językoznawcą z 20-letnim doświadczeniem w badaniu języka polskiego. Zwracasz baczną uwagę na szczegóły znaczeniowe i korzystając z doświadczenia, kontekstu i wyczucia potrafisz doskonale ocenić wydźwięk wypowiedzi.\"\"\"

ZADANIE:
\"\"\"Zadanie składa się z trzech części.
1. Oceń finalny WYDŹWIĘK poniższego TEKSTU. Masz do wyboru dwie kategorie: NEGATYWNY i POZYTYWNY. Wpisz tylko jedno słowo określające wydźwięk. Uwaga! Jeśli tekst opowiada o początkowych emocjach, które przerodziły się w inne, opisz wyłącznie wydźwięk powiązany z końcowymi emocjami.
2. Wyjaśnij szczegółowo, obszernie i jasno intencje autora poniższego TEKSTU. Użyj specjalistycznego słownictwa.
3. Jeśli w TEKŚCIE występują związki frazeologiczne podaj ich znaczenia w kontekście TEKSTU.\"\"\"

PRZYKŁAD:
\"\"\"TEKST: To że bielik jest super włóżmy między bajki.
ODPOWIEDŹ:
1. NEGATYWNY 
2. Związek frazeologiczny "włożyć między bajki" oznacza uznanie czegoś za nieprawdziwe. W tym przypadku dotyczy określenia, że "bielik jest super", więc finalnie jest to negatywna opinia.
3. "Włożyć między bajki": "uznać, że coś jest nieprawdziwe".\"\"\"

TEKST:
\"\"\"{text}\"\"\""""

EVALUATING_METAMODEL_PROMPT = """Jesteś asystentem oceniającym modele językowe. Modele te starają się opisać intencje autora tekstu/wypowiedzi, wydźwięk i podać definicje związków frazeologicznych.
Wykonaj następujące kroki:
1. Oceń odpowiedź modelu #ODPOWIEDZ# na podstawie referencyjnej odpowiedzi #REFERENCJA-WYJASNIENIE#. Zwróć ocenę odpowiedzi zawsze w formacie {{"OCENA": "X"}} gdzie X jest od 0 (zła odpowiedź) do 5 (bardzo dobra odpowiedź). Przykład oceny: {{"OCENA": "5"}}.
2. Jeśli w poniższym tekście nie znajduje się nagłówek #REFERENCJA-WYDZWIEK#, to zupełnie pomiń ten punkt i w swojej odpowiedzi nie zamieszczaj pola "WYDŹWIĘK". Jeśli w tekście znajduje się nagłówek #REFERENCJA-WYDZWIEK#, to na jego podstawie oceń prawidłowość opisanego wydźwięku w odpowiedzi #ODPOWIEDZ#. Zwróć ocenę wydźwięku w formacie {{"WYDŹWIĘK": "X"}}, gdzie X jest od 0 (zła odpowiedź) do 5 (bardzo dobra odpowiedź). Przykłady ocen: {{"WYDŹWIĘK": "1"}}.
3. Jeśli w poniższym tekście nie znajduje się nagłówek #REFERENCJA-ZWIAZKI-FRAZEOLOGICZNE#, to zupełnie pomiń ten punkt i w swojej odpowiedzi nie zamieszczaj pola "ZWIAZKI". Jeśli w tekście znajduje się nagłówek #REFERENCJA-ZWIAZKI-FRAZEOLOGICZNE#, to na jego podstawie oceń prawidłowość opisu związków frazelogicznych w odpowiedzi #ODPOWIEDZ#. Zwróć ocenę związków frazeologicznych w formacie {{"ZWIAZKI": "X"}}, gdzie X jest od 0 (zła odpowiedź) do 5 (bardzo dobra odpowiedź). Przykłady ocen: {{"ZWIAZKI": "1"}}.
4. Jeśli na podstawie punktów 1-3 wystawiłeś więcej niż jedną ocenę, podaj każdą kolejną w nowej linii.
5. W Twojej odpowiedzi mają znajdować się wyłącznie oceny wynikające bezpośrednio z powyższych punktów. Nie pisz żadnego dodatkowego tekstu.
#ODPOWIEDZ#
{model_response}
#REFERENCJA-WYJASNIENIE#
{reference_explanation}
#REFERENCJA-WYDZWIEK#
{reference_sentiment}
#REFERENCJA-ZWIAZKI-FRAZEOLOGICZNE#
{reference_idioms}"""

BATCH_SIZE: int = 32
