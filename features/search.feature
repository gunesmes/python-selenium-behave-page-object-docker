Feature: Search stuff on the main page
  
  Scenario: Searching on the main page
    Given I open the main page
    When I search for "LG V30"
    Then I should see "LG V30" in search result 

