Feature: Sync and devices
  As a player
  I want to sync and use controllers
  So that I can move between devices and play comfortably

  Scenario: Syncing save data
    Given Delta Sync is enabled for the user
    When a save file changes on the device
    Then Delta uploads the change to the connected service
    And other devices receive the updated save file

  Scenario: Pairing a controller
    Given a compatible controller is nearby
    When the user pairs the controller in iOS settings
    Then Delta detects the controller on the next launch
    And the user can remap controls for the system
