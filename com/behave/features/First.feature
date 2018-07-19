Feature: Calculator scenarios

  @add
  Scenario: addition of two numbers
    Given two nos a and b
    When I add two numbers
    Then the result must be greater than ten

  @sub
  Scenario: substraction of two numbers
    Given two nos a and b
    When I sub two numbers
    Then the result must be less than ten

  @mul
  Scenario: Multiplication of two numbers
    Given two nos a and b
    When I multiply two numbers
    Then the result must be greater than ten

  @div
  Scenario: Division of two numbers
    Given two nos a and b
    When I divide two numbers
    Then the result must be less than ten