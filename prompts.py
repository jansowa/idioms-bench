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
