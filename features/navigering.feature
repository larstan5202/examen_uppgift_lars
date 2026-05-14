Feature: Navigera mellan vyer
  Som en användare
  Vill jag kunna navigera mellan katalog, favoriter och statistik

  Scenario: Användaren navigerar till favoritvyn
    Given att användaren öppnar startsidan
    When användaren klickar på "Favorites"
    Then visas favoritvyn

  Scenario: Användaren navigerar till statistikvyn
    Given att nvändaren öppnar startsidan
    When användaren klickar på "Statistics"
    Then visas stastikvyn