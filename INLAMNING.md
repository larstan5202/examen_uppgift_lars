# inlämning - Examensuppgift Lars

## Projektbeskrivning

Backend

Tekniker
- Python
- FastAPI
- Uvicorn

Funktioner

- Ta emot data från fontend
- Validera inkommande data
- Returnera svar till frontend
- Loggar eller bearbetar data

Starta backend
- pip install -r requirements.txt
- uvicon main:app --reload

Automatisera tester

Testverktyg

- pytest
- pytest-playwright
- Playwright för UI-tester

Vad som testats

- Att formuläret visas korrekt
- Att validering fungerar
- Att knappar och flöden fungerar
- Att backend svarar korrekt
- Att API-anrop fungerar
- Att felhantering fungerar

Köra tester

- pytets

Reflektioner

Det som gick bra

- Frontend och backend fungerar lokalt
- Formuläret går att fylla i och skicka
- Backend tar emot och svarar korrekt
- Automatiserade tester fungerar lokalt

Det som var svårt

- Att få CI-delen att fungera
- Problem med att låsta filer i PyCharm
- Skillanden mellan lokal miljö och GitHub Actions

CI-delen fungerade inte

Jag försökte sätta upp en CI-pipline i GitHub Actioins, men stötte på flera problem somk gjorde
att jag inte fick CI att fungera fullt ut

Problem som uppstod

- GitHub Actions körde inte testerna korrekt
- Pipelines fastnade på beroenden elle sökvägar
- Miljöskillnader gjorde att tester som fungerade lokalt inte fungerade i CI
- Vissa filer orsakade konflikter eller låsningar

Vad jag försökte

- Justera YAML-filen flera gånger
- Delade upp installation, test och build
- Fixade beroenden i requirements.txt
- Testade olika Python-versioner
- Försökte återskapa lokal miljö i CI

Slutsats

Trots flera försök fick jag inte CI att fungera
Jag valde därför att fokusera på att säkerställa att frontend, backend och tester fungerade lokalt,
vilket det gör.

Övrigt

- Projektet fungerar lokalt enligt kravspecifikationen
- Backend och frontend kommunsicerar korrekt
- Tester går att köra lokalt
- CI är den enda delen som inte blev klar