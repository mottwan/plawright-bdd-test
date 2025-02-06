Feature: Basic search form

  @basic_search
  Scenario: T1 - One way flight search
    Given As a not logged-in user, navigate to the homepage "https://www.kiwi.com"
    When I select "one-way" trip type
    And Set the "departure" airport "RTM"
    And Set the "arrival" airport "MAD"
    And Set the departure time 1 "week" in the future starting from the current date
    And Uncheck the Check accommodation with booking.com option
    And Click the search button
    Then I am redirected to the search results page

  Scenario: T2 - not tagged scenario
    Given As a not logged-in user, navigate to the homepage "https://www.kiwi.com"
    When I select "one-way" trip type
    And Set the "departure" airport "RTM"
    And Set the "arrival" airport "MAD"
    And Set the departure time 1 "week" in the future starting from the current date
    And Uncheck the Check accommodation with booking.com option
    And Click the search button
    Then I am redirected to the search results page
