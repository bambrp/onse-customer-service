Feature: Update customer
  As a recently married customer
  I want to change my surname
  In order to ensure my information is correct

  Scenario: Successful name change
    Given customer "Jez Humble" with ID "1" exists
    When I change my surname to "Smith"
    When I fetch customer "1"
    Then I should see customer "Jez Smith"

