Feature: Gameplay session
  As a player
  I want to play a game with reliable controls
  So that gameplay feels responsive and stable

  Scenario: Starting a game
    Given the user selects a game in the library
    When the game launches
    Then the emulator starts in full screen
    And on-screen controls appear for the selected system

  Scenario: Saving and loading a state
    Given a game is running
    When the user creates a save state from the pause menu
    Then the save state is listed with a timestamp
    When the user loads that save state
    Then gameplay resumes at the saved point
