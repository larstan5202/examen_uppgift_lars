Feature: Navigering mellan vyer

  Scenario: Användaren navigerar till favoritvyn
    Given att användaren är på startsidan
    When användaren klickar på "Favorites"
    Then visas favoritvyn

  Scenario: Användaren navigerar till statistikvyn
    Given att användaren är på startsidan
    When användaren klickar på "Statistics"
    Then visas statistikvyn
