Feature: Library management
  As a player
  I want to manage my game library
  So that I can find and launch games quickly

  Scenario: Importing a game from Files
    Given the user has a compatible ROM file in the Files app
    When the user imports the ROM into Delta
    Then the game appears in the library with its title metadata
    And Delta suggests matching box art

  Scenario: Searching for a game
    Given the library contains multiple games
    When the user searches by game title
    Then the library filters to matching results
