Feature: Hantera favoriter
  Som en användare
  Vill jag kunna lägga till och ta bort favoriter
  så att jag kan spara böcker jag gillar

  Scenario: Använder lägger till en bok i favoriter
    Given att användaren öppnas startsidan
    When användaren lägger till första boken
    Then ska boken visas i favoritlistan

  Scenario: Användaren tar bort en bok från favoriter
    Given att användaren har en favoritbok
    When användaren tar bort boken från favoriter
    Then ska boken inte längre visas i favoritlistan