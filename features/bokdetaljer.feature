Feature: Visa bokdetaljer
  Som en användare
  Vill jag kunna öppna en dialog med mer information om en bok
  Så att jag kan läsa detaljer innan jag väljer den

  Scenario: Använder öppnar bokdetaljer
    Given att använden öppnar startsidan
    When användaren klickar på första boken
    Then visas en dialog med bokinformation