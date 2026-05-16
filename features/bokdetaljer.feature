Feature: Visa bokdetaljer

  Scenario: Användaren öppnar bokdetaljer
    Given att användaren är på startsidan
    When användaren klickar på en bok
    Then visas bokdetaljer
