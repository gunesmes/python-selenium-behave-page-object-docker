Feature: Search stuff on the main page of Amazon
  Background: go to main page of Amazon
    Given I open the main page
    
  @search @smoke
  Scenario: Searching on the main page
    When I search for "LG V30"
    Then I should see "LG V30" in search result 
