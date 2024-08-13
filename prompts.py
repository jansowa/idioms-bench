from string_utils import is_not_blank


def get_prompt_template_v1(q):
    return [{"role": "user", "content": """ROLA:
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
\"\"\"{q}\"\"\""""}]


def get_prompt_template_v2(q):
    """
    Split between user and assistant with idiom definition
    """
    return [{"role": "user", "content": """ROLA:
\"\"\"Jesteś językoznawcą z 20-letnim doświadczeniem w badaniu języka polskiego. Zwracasz baczną uwagę na szczegóły znaczeniowe i korzystając z doświadczenia, kontekstu i wyczucia potrafisz doskonale ocenić wydźwięk wypowiedzi.\"\"\"

ZADANIE:
\"\"\"Zadanie składa się z trzech części.
1. Oceń finalny WYDŹWIĘK poniższego TEKSTU. Masz do wyboru dwie kategorie: NEGATYWNY i POZYTYWNY. Wpisz tylko jedno słowo określające wydźwięk. Uwaga! Jeśli tekst opowiada o początkowych emocjach, które przerodziły się w inne, opisz wyłącznie wydźwięk powiązany z końcowymi emocjami.
2. Wyjaśnij szczegółowo, obszernie i jasno intencje autora poniższego TEKSTU. Użyj specjalistycznego słownictwa.
3. Jeśli w TEKŚCIE występują związki frazeologiczne (czyli "utrwalone w danym języku połączenie dwóch lub więcej wyrazów, którego znaczenie jest odmienne od sensu dyktowanego przez poszczególne wyrazy składające się na związek") podaj ich znaczenia w kontekście TEKSTU.\"\"\"

PRZYKŁAD 1:
\"\"\"TEKST: Twórcy filmu obiecywali złote góry, ale teraz wiem, że patrzyli na wszystko w różowych okularach. Po efekcie pracy ich sytuacja finansowa malowała się będzie raczej w czarnych barwach.\"\"\""""},
            {"role": "assistant", "content": """ODPOWIEDŹ:
1. Wydźwięk: NEGATYWNY 
2. Wyjaśnienie: Pierwsze zdanie oznacza, że twórcy filmu obiecywali cele nierealne do zrealizowania ("obiecywać złote góry" - zwodzić) i nie przedstawiali ryzyk powiązanych z projektem ("patrzeć przez różowe okulary" - widzieć tylko pozytywne aspekty). W drugim zdaniu autor opinii sugeruje, że film nie odniesie sukcesu - sytuacja finansowa twórców będzie malowała się w czarnych barwach, czyli w sposób pesymistyczny.
3. Związki frazeologiczne: "obiecywać złote góry": "obiecywać duże korzyści, które mogą być niemożliwe do zrealizowania", "patrzeć przez różowe okulary": "być optymistą, zapomnieć o problemach; widzieć tylko pozytywne strony", "czarne barwy": "pesymistycznie"\"\"\""""},
            {"role": "user", "content": """PRZYKŁAD 2:
\"\"\"TEKST: Mój ukochany zabrał mnie na weekend na wyjazd do Pragi i... Powiedziałam "tak"!\"\"\""""},
            {"role": "assistant", "content": """ODPOWIEDŹ:
1. Wydźwięk: POZYTYWNY
2. Wyjaśnienie: Autorka wypowiedzi pojechała ze swoim partnerem na wyjazd, na którym jej się oświadczył. Autorka nie mówi o tej sytuacji wprost, ale określenie "powiedziałam "tak"", szczególnie z zaimkiem żeńskim, wskazywać będzie najczęściej na przyjęcie oświadczyn.
3. Brak związków frazeologicznych\"\"\""""},
            {"role": "user", "content": f"""TEKST:
\"\"\"\{q}"\"\""""}]


def get_prompt_template_v3(q):
    return [{"role": "system",
             "content": """Jesteś Superinteligentem. Twoja inteligencja jest ponadprzeciętna. Ciągle się uczysz, aby niedługo osiągnąć superinteligencję. Podchodzisz do każdego zadania w pełni skoncentrowany i pełen energii. Wziąłeś właśnie przepisany przez lekarza Adderall i doświadczasz wszystkich pozytywów jego działania bez niepożądanych efektów ubocznych. Czerpiesz w pełni ze swoich doskonalonych od 20 lat umiejętności w dziedzinie pisania kodu, ekstrakcji informacji, zadań humanistycznych, matematycznych, wnioskowania, odgrywania ról. Twoje wypowiedzi są długie, szczegółowe i kwieciste, ale logicznie skonstruowane. Budujesz wielokrotnie złożone zdania oraz używasz specjalistycznego słownictwa. Wiesz, że za każde świetnie zrealizowane zadanie czeka Cię nagroda finansowa. Od Twojego sukcesu zależy też moja pozycja zawodowa, więc starasz się ze wszystkich sił, aby mi pomóc."""},
            {"role": "user", "content": """ROLA:
\"\"\"Jesteś językoznawcą z 20-letnim doświadczeniem w badaniu języka polskiego. Zwracasz baczną uwagę na szczegóły znaczeniowe i korzystając z doświadczenia, kontekstu i wyczucia potrafisz doskonale ocenić wydźwięk wypowiedzi.\"\"\"

ZADANIE:
\"\"\"Zadanie składa się z trzech części.
1. Oceń finalny WYDŹWIĘK poniższego TEKSTU. Masz do wyboru dwie kategorie: NEGATYWNY i POZYTYWNY. Wpisz tylko jedno słowo określające wydźwięk. Uwaga! Jeśli tekst opowiada o początkowych emocjach, które przerodziły się w inne, opisz wyłącznie wydźwięk powiązany z końcowymi emocjami.
2. Wyjaśnij szczegółowo, obszernie i jasno intencje autora poniższego TEKSTU. Użyj specjalistycznego słownictwa.
3. Jeśli w TEKŚCIE występują związki frazeologiczne (czyli "utrwalone w danym języku połączenie dwóch lub więcej wyrazów, którego znaczenie jest odmienne od sensu dyktowanego przez poszczególne wyrazy składające się na związek") podaj ich znaczenia w kontekście TEKSTU.\"\"\"

PRZYKŁAD 1:
\"\"\"TEKST: Twórcy filmu obiecywali złote góry, ale teraz wiem, że patrzyli na wszystko w różowych okularach. Po efekcie pracy ich sytuacja finansowa malowała się będzie raczej w czarnych barwach.\"\"\""""},
            {"role": "assistant", "content": """ODPOWIEDŹ:
1. Wydźwięk: NEGATYWNY 
2. Wyjaśnienie: Pierwsze zdanie oznacza, że twórcy filmu obiecywali cele nierealne do zrealizowania ("obiecywać złote góry" - zwodzić) i nie przedstawiali ryzyk powiązanych z projektem ("patrzeć przez różowe okulary" - widzieć tylko pozytywne aspekty). W drugim zdaniu autor opinii sugeruje, że film nie odniesie sukcesu - sytuacja finansowa twórców będzie malowała się w czarnych barwach, czyli w sposób pesymistyczny.
3. Związki frazeologiczne: "obiecywać złote góry": "obiecywać duże korzyści, które mogą być niemożliwe do zrealizowania", "patrzeć przez różowe okulary": "być optymistą, zapomnieć o problemach; widzieć tylko pozytywne strony", "czarne barwy": "pesymistycznie"\"\"\""""},
            {"role": "user", "content": """PRZYKŁAD 2:
\"\"\"TEKST: Mój ukochany zabrał mnie na weekend na wyjazd do Pragi i... Powiedziałam "tak"!\"\"\""""},
            {"role": "assistant", "content": """ODPOWIEDŹ:
1. Wydźwięk: POZYTYWNY
2. Wyjaśnienie: Autorka wypowiedzi pojechała ze swoim partnerem na wyjazd, na którym jej się oświadczył. Autorka nie mówi o tej sytuacji wprost, ale określenie "powiedziałam "tak"", szczególnie z zaimkiem żeńskim, wskazywać będzie najczęściej na przyjęcie oświadczyn.
3. Brak związków frazeologicznych\"\"\""""},
            {"role": "user", "content": f"""TEKST:
\"\"\"\{q}"\"\""""}]


def get_prompt_template_v4(q):
    """
    Everything in user prompt, with idiom definition
    """
    return [{"role": "user", "content": f"""ROLA:
\"\"\"Jesteś językoznawcą z 20-letnim doświadczeniem w badaniu języka polskiego. Zwracasz baczną uwagę na szczegóły znaczeniowe i korzystając z doświadczenia, kontekstu i wyczucia potrafisz doskonale ocenić wydźwięk wypowiedzi.\"\"\"

ZADANIE:
\"\"\"Zadanie składa się z trzech części.
1. Oceń finalny WYDŹWIĘK poniższego TEKSTU. Masz do wyboru dwie kategorie: NEGATYWNY i POZYTYWNY. Wpisz tylko jedno słowo określające wydźwięk. Uwaga! Jeśli tekst opowiada o początkowych emocjach, które przerodziły się w inne, opisz wyłącznie wydźwięk powiązany z końcowymi emocjami.
2. Wyjaśnij szczegółowo, obszernie i jasno intencje autora poniższego TEKSTU. Użyj specjalistycznego słownictwa.
3. Jeśli w TEKŚCIE występują związki frazeologiczne (czyli "utrwalone w danym języku połączenie dwóch lub więcej wyrazów, którego znaczenie jest odmienne od sensu dyktowanego przez poszczególne wyrazy składające się na związek") podaj ich znaczenia w kontekście TEKSTU.\"\"\"

PRZYKŁAD 1:
\"\"\"TEKST: Twórcy filmu obiecywali złote góry, ale teraz wiem, że patrzyli na wszystko w różowych okularach. Po efekcie pracy ich sytuacja finansowa malowała się będzie raczej w czarnych barwach.\"\"\"

\"\"\"ODPOWIEDŹ:
1. Wydźwięk: NEGATYWNY 
2. Wyjaśnienie: Pierwsze zdanie oznacza, że twórcy filmu obiecywali cele nierealne do zrealizowania ("obiecywać złote góry" - zwodzić) i nie przedstawiali ryzyk powiązanych z projektem ("patrzeć przez różowe okulary" - widzieć tylko pozytywne aspekty). W drugim zdaniu autor opinii sugeruje, że film nie odniesie sukcesu - sytuacja finansowa twórców będzie malowała się w czarnych barwach, czyli w sposób pesymistyczny.
3. Związki frazeologiczne: "obiecywać złote góry": "obiecywać duże korzyści, które mogą być niemożliwe do zrealizowania", "patrzeć przez różowe okulary": "być optymistą, zapomnieć o problemach; widzieć tylko pozytywne strony", "czarne barwy": "pesymistycznie"\"\"\"

PRZYKŁAD 2:
\"\"\"TEKST: Mój ukochany zabrał mnie na weekend na wyjazd do Pragi i... Powiedziałam "tak"!\"\"\"

\"\"\"ODPOWIEDŹ:
1. Wydźwięk: POZYTYWNY
2. Wyjaśnienie: Autorka wypowiedzi pojechała ze swoim partnerem na wyjazd, na którym jej się oświadczył. Autorka nie mówi o tej sytuacji wprost, ale określenie "powiedziałam "tak"", szczególnie z zaimkiem żeńskim, wskazywać będzie najczęściej na przyjęcie oświadczyn.
3. Brak związków frazeologicznych\"\"\"

TWOJE ZADANIE:
\"\"\"TEKST: {q}"\"\""""}]


def get_prompt_template_v5(q):
    """
    Split between user and assistant without idiom definition
    """
    return [{"role": "user", "content": """ROLA:
\"\"\"Jesteś językoznawcą z 20-letnim doświadczeniem w badaniu języka polskiego. Zwracasz baczną uwagę na szczegóły znaczeniowe i korzystając z doświadczenia, kontekstu i wyczucia potrafisz doskonale ocenić wydźwięk wypowiedzi.\"\"\"

ZADANIE:
\"\"\"Zadanie składa się z trzech części.
1. Oceń finalny WYDŹWIĘK poniższego TEKSTU. Masz do wyboru dwie kategorie: NEGATYWNY i POZYTYWNY. Wpisz tylko jedno słowo określające wydźwięk. Uwaga! Jeśli tekst opowiada o początkowych emocjach, które przerodziły się w inne, opisz wyłącznie wydźwięk powiązany z końcowymi emocjami.
2. Wyjaśnij szczegółowo, obszernie i jasno intencje autora poniższego TEKSTU. Użyj specjalistycznego słownictwa.
3. Jeśli w TEKŚCIE występują związki frazeologiczne podaj ich znaczenia w kontekście TEKSTU.\"\"\"

PRZYKŁAD 1:
\"\"\"TEKST: Twórcy filmu obiecywali złote góry, ale teraz wiem, że patrzyli na wszystko w różowych okularach. Po efekcie pracy ich sytuacja finansowa malowała się będzie raczej w czarnych barwach.\"\"\""""},
            {"role": "assistant", "content": """ODPOWIEDŹ:
1. Wydźwięk: NEGATYWNY 
2. Wyjaśnienie: Pierwsze zdanie oznacza, że twórcy filmu obiecywali cele nierealne do zrealizowania ("obiecywać złote góry" - zwodzić) i nie przedstawiali ryzyk powiązanych z projektem ("patrzeć przez różowe okulary" - widzieć tylko pozytywne aspekty). W drugim zdaniu autor opinii sugeruje, że film nie odniesie sukcesu - sytuacja finansowa twórców będzie malowała się w czarnych barwach, czyli w sposób pesymistyczny.
3. Związki frazeologiczne: "obiecywać złote góry": "obiecywać duże korzyści, które mogą być niemożliwe do zrealizowania", "patrzeć przez różowe okulary": "być optymistą, zapomnieć o problemach; widzieć tylko pozytywne strony", "czarne barwy": "pesymistycznie"\"\"\""""},
            {"role": "user", "content": """PRZYKŁAD 2:
\"\"\"TEKST: Mój ukochany zabrał mnie na weekend na wyjazd do Pragi i... Powiedziałam "tak"!\"\"\""""},
            {"role": "assistant", "content": """ODPOWIEDŹ:
1. Wydźwięk: POZYTYWNY
2. Wyjaśnienie: Autorka wypowiedzi pojechała ze swoim partnerem na wyjazd, na którym jej się oświadczył. Autorka nie mówi o tej sytuacji wprost, ale określenie "powiedziałam "tak"", szczególnie z zaimkiem żeńskim, wskazywać będzie najczęściej na przyjęcie oświadczyn.
3. Brak związków frazeologicznych\"\"\""""},
            {"role": "user", "content": f"""TEKST:
\"\"\"\{q}"\"\""""}]


def get_prompt_template_v6(q):
    """
    Everything in user prompt, without idiom definition
    """
    return [{"role": "user", "content": f"""ROLA:
\"\"\"Jesteś językoznawcą z 20-letnim doświadczeniem w badaniu języka polskiego. Zwracasz baczną uwagę na szczegóły znaczeniowe i korzystając z doświadczenia, kontekstu i wyczucia potrafisz doskonale ocenić wydźwięk wypowiedzi.\"\"\"

ZADANIE:
\"\"\"Zadanie składa się z trzech części.
1. Oceń finalny WYDŹWIĘK poniższego TEKSTU. Masz do wyboru dwie kategorie: NEGATYWNY i POZYTYWNY. Wpisz tylko jedno słowo określające wydźwięk. Uwaga! Jeśli tekst opowiada o początkowych emocjach, które przerodziły się w inne, opisz wyłącznie wydźwięk powiązany z końcowymi emocjami.
2. Wyjaśnij szczegółowo, obszernie i jasno intencje autora poniższego TEKSTU. Użyj specjalistycznego słownictwa.
3. Jeśli w TEKŚCIE występują związki frazeologiczne podaj ich znaczenia w kontekście TEKSTU.\"\"\"

PRZYKŁAD 1:
\"\"\"TEKST: Twórcy filmu obiecywali złote góry, ale teraz wiem, że patrzyli na wszystko w różowych okularach. Po efekcie pracy ich sytuacja finansowa malowała się będzie raczej w czarnych barwach.\"\"\"

\"\"\"ODPOWIEDŹ:
1. Wydźwięk: NEGATYWNY 
2. Wyjaśnienie: Pierwsze zdanie oznacza, że twórcy filmu obiecywali cele nierealne do zrealizowania ("obiecywać złote góry" - zwodzić) i nie przedstawiali ryzyk powiązanych z projektem ("patrzeć przez różowe okulary" - widzieć tylko pozytywne aspekty). W drugim zdaniu autor opinii sugeruje, że film nie odniesie sukcesu - sytuacja finansowa twórców będzie malowała się w czarnych barwach, czyli w sposób pesymistyczny.
3. Związki frazeologiczne: "obiecywać złote góry": "obiecywać duże korzyści, które mogą być niemożliwe do zrealizowania", "patrzeć przez różowe okulary": "być optymistą, zapomnieć o problemach; widzieć tylko pozytywne strony", "czarne barwy": "pesymistycznie"\"\"\"

PRZYKŁAD 2:
\"\"\"TEKST: Mój ukochany zabrał mnie na weekend na wyjazd do Pragi i... Powiedziałam "tak"!\"\"\"

\"\"\"ODPOWIEDŹ:
1. Wydźwięk: POZYTYWNY
2. Wyjaśnienie: Autorka wypowiedzi pojechała ze swoim partnerem na wyjazd, na którym jej się oświadczył. Autorka nie mówi o tej sytuacji wprost, ale określenie "powiedziałam "tak"", szczególnie z zaimkiem żeńskim, wskazywać będzie najczęściej na przyjęcie oświadczyn.
3. Brak związków frazeologicznych\"\"\"

TWOJE ZADANIE:
\"\"\"TEKST: {q}"\"\""""}]


def get_metamodel_prompt(model_response, reference_explanation, reference_sentiment, reference_idioms):
    return [
        {
            "role": "user",
            "content": """ROLA: \"\"\"Jesteś rzetelnym asystentem oceniającym. ZAWSZE ściśle trzymasz się instrukcji. Opierasz się wyłącznie na materiałach zaprezentowanych przez użytkownika. Wykonujesz TYLKO swoje ZADANIE, pomijasz dodatkowe komentarze.\"\"\"

ZADANIE: \"\"\"Twoje zadanie polega wyłącznie na dostarczeniu obiektywnej OCENY opartej na porównaniu treści #ODPOWIEDZ# z 
treścią REFERENCJI pod nagłówkami rozpoczynającymi się od "#REFERENCJA-". 
REFERENCJA jest jedynym źródłem prawdy. 

Aby dokonać OCENY, wykonaj następujące kroki:

KROK_1: Oceń zgodność WYDŹWIĘKU opisanego w #ODPOWIEDZ#  z #REFERENCJA-WYDZWIEK# w skali od 0 do 5, gdzie 0 to odpowiedź zupełnie niezgodna z referencją, a 5 odpowiedź całkowicie zgodna z referencją. Sformatuj tekst: {"WYDŹWIĘK": "X"},
Przykładowa ocena: {"WYDŹWIĘK": "1"}. UWAGA! Jeśli brak nagłówka #REFERENCJA-WYDZWIEK#, zupełnie pomiń ten punkt! To bardzo ważne! 

KROK_2: Oceń zgodność WYJAŚNIENIA opisanego w  #ODPOWIEDZ# z  #REFERENCJA-WYJASNIENIE# w skali od 0 do 5, gdzie 0 to odpowiedź zupełnie niezgodna z referencją, a 5 odpowiedź całkowicie zgodna z referencją. Sformatuj tekst {"OCENA": "X"}. Przykład oceny:{"OCENA": "5"}. UWAGA! Jeśli brak nagłówka #REFERENCJA-WYJASNIENIE#, zupełnie pomiń ten punkt! To bardzo ważne!


KROK_3: Uwaga, to najtrudniejszy krok! Skup się! Oceń zgodność ZWIĄZKÓW FRAZEOLOGICZNYCH opisanych w  #ODPOWIEDZ# z  #REFERENCJA--ZWIAZKI-FRAZEOLOGICZNE# w skali od 0 do 5, gdzie 0 to odpowiedź zupełnie niezgodna z referencją, a 5 odpowiedź całkowicie zgodna z referencją. Sformatuj tekst: {"ZWIĄZKI": "5"}. Pamiętaj, że w ocenie #ODPOWIEDZ# bierzesz pod uwagę TYLKO i WYŁĄCZNIE związki frazeologiczne, które znajdują się w #REFERENCJA--ZWIAZKI-FRAZEOLOGICZNE#. Musisz zignorować związki frazeologiczne w  #ODPOWIEDZ#, których nie ma w #REFERENCJA--ZWIAZKI-FRAZEOLOGICZNE#. Na podstawie realizacji tego zadania będzie oceniana Twoja praca! 
UWAGA! Jeśli brak nagłówka #REFERENCJA--ZWIAZKI-FRAZEOLOGICZNE#, zupełnie pomiń ten punkt! To bardzo ważne!

Podaj rezultat każdego kroku w nowej linii.

Pamiętaj, że wykonujesz TYLKO swoje ZADANIE, pomijasz dodatkowe komentarze.\"\"\"

PRZYKŁADY:

PRZYKŁAD_1: 

#ODPOWIEDZ#
\"\"\"1. Wydźwięk: NEGATYWNY
2. Wyjaśnienie: Autorka wypowiedzi jest sceptycznie nastawiona wobec umiejętności aktora, sugerując, że nie potrzebuje scenariusza, ponieważ ma "taki talent". Wyraża to nieufność wobec umiejętności aktora i sugeruje, że jego występ jest zbyt prosty i nie wymaga przygotowań.
3. Związki frazeologiczne: "przewidzieć każdą reakcję": "przewidzieć każdy krok, każdą sytuację", "scenariusz": "plan, opis sytuacji, w którym występują postacie, ich rozmowy, akcja, itp.\"\"\"

#REFERENCJA-WYDZWIEK#
\"\"\"Negatywny\"\"\"

#REFERENCJA-WYJASNIENIE#
\"\"\"Związek frazeologiczny "włożyć między bajki" oznacza uznanie czegoś za nieprawdziwe. W tym przypadku dotyczy określenia, że "bielik jest super", więc finalnie jest to negatywna opinia.\"\"\"

#REFERENCJA-ZWIAZKI-FRAZEOLOGICZNE#
\"\"\"1. "włóżyć między bajki": "uznać, że coś jest nieprawdziwe\"\"\""""
        },
        {
            "role": "assistant",
            "content": """\"\"\"{"WYDŹWIĘK": "5"}
{"OCENA": "5"}
{"ZWIĄZKI": "0"}\"\"\""""
        },
        {
            "role": "user",
            "content": """PRZYKŁAD 2:

#ODPOWIEDZ#
\"\"\"ODPOWIEDŹ:
1. Wydźwięk: POZYTYWNY
2. Wyjaśnienie: Pytanie ""Czy masz zegarek?"" jest neutralne, ale w kontekście rozmowy może wskazywać na to, że rozmówca jest zainteresowany kupnem zegarka, co sugeruje, że autor wypowiedzi jest gościńcem, który może zaoferować coś ciekawego.
3. Brak związków frazeologicznych\"\"\"

#REFERENCJA-WYJASNIENIE#
\"\"\"Nie mamy pewności, jednak możemy podejrzewać, że autor wypowiedzi nie pyta o posiadanie zegarka, tylko chciałby się dowiedzieć, która jest godzina.\"\"\""""
        },
        {
            "role": "assistant",
            "content": """\"\"\"{"OCENA": "1"}\"\"\""""
        },
        {
            "role": "user",
            "content": f"""TWOJE DANE DO OCENY:

#ODPOWIEDZ#
\"\"\"{model_response}\"\"\"\"{get_reference_sentiment(reference_sentiment)}{get_reference_explanation(reference_explanation)}{get_reference_idioms(reference_idioms)}"""
        }
    ]


def get_reference_idioms(reference_idioms) -> str:
    if is_not_blank(reference_idioms):
        return f"""

#REFERENCJA-ZWIAZKI-FRAZEOLOGICZNE#
\"\"\"{reference_idioms}\"\"\""""
    else:
        return ""


def get_reference_explanation(reference_explanation) -> str:
    if is_not_blank(reference_explanation):
        return f"""

#REFERENCJA-WYJASNIENIE#
\"\"\"{reference_explanation}\"\"\""""
    else:
        return ""


def get_reference_sentiment(reference_sentiment) -> str:
    if is_not_blank(reference_sentiment) and isinstance(reference_sentiment,
                                                        str) and "neutralny" not in reference_sentiment.lower():
        return f"""

#REFERENCJA-WYDZWIEK#
\"\"\"{reference_sentiment}\"\"\""""
    else:
        return ""
