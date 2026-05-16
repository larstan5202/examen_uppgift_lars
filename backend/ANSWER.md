# 1 Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest

## Enhetstest
Testar en enskild funktioin, metod eller klass i isolering.
Syftet är att säkerställa att den minsta byggstenen i koden fungerar korrekt utan beroende.

## Integrationstest
Testar hur flera delar av systemet fungerar tillsammans.
Fokus ligger på samspelet mellan moduler, klasser eller backend-frontend.

## Regretionstest
Testar att redan fungerande funktion fortfarande fungerar efter att man gjort
ändringar i koden.
Syftet är att upptäcka om något som tidigare fungerade har gått sönder.

## Prestandatest
Testar hur systemet fungerar under belastning.
Fokuserar på svarstider, skalbarhet och hur systemet hanterar många användare eller
stora datamängder.

# 2 Beskriv hur det går när man arbetar med TDD
TDD(Test Driven Development)
1. Red - Skriver ett test som beskriver önskat beteende. Testet ska först misslyckas.
2. Green - Skriv minsta möjliga kod för att få testet att gå igenom.
3. Refactor - Förbättra koden utan att ändra beteendet. Alla tester ska fortsätta vara gröna.
TDD leder till tydligare krav, bättre design och hög testtäckning.

# 3. Beskriv hur BDD skiljer sig från TDD
# TDD
- Utgår från utvecklarens perspektiv
- Fokuserar på funktioner, metoder och kod
- Skriver tester först, sedan kod
- Kodnära och tekniskt

# BDD
- Utgår från användarens beteende
- Beskriver funktionalitet i form av user stories
- Använder Gherkin-syntax (Given/When/Then)
- Testar systemet från användarens synvinkel
- Används ofta med verktyg som Paywright
Kort sammanfattnig
TDD testar hur koden fungerar. BDD testar hur användaren upplever systemet.

# 4 Vilka tester skulle du välja för en webbsisa som liknar Läslisstan? Motivera ditt val.
För en webbsida som Läslistan skulle jag använda följande tester:

# Enhetstester
För att säkerställa att backend-lofigen fungerar korrekt t ex
- Lägga till bok
- toggla favorit
- hantera listor

# Integrationstester
För att testa att backend-delarna fungerar tillsamman, t ex
- att favoritmarkeringar uppdateras korrekt
- att BookStore och FavoriteBooks samspelar som de ska

# End-to-end-tester (BDD + Playwrighr)
För att testa hela användarflödet, t ex
- lägga till en bok
- markera favorit
- navigera mellan vyer
- att Ul och backend fungerar ihop

# Regressionstester
För att säkerställa att nya ändringar inte förstör befintlig funktionalitet

# Motivering
En sådan webbsida har både logik (backend) och användarflöden (frontend)
Därför behövs både kodnära tester och tester som simulerar verkliga användare
Kombinationen ger hög kvalitet, minska buggar och gör systemet mer robust.

