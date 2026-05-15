Feature: Hantera favoriter

  Scenario: Användaren lägger till en bok i favoriter
    Given att användaren är på startsidan
    When användaren lägger till en bok i favoriter
    Then visas boken i favoritlistan

  Scenario: Användaren tar bort en bok från favoriter
    Given att användaren är på startsidan
    When användaren tar bort en bok från favoriter
    Then är favoritlistan tom
