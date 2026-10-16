@regression @login
Feature: Login
    As a customer of the webshop
    I want to log in with my account
    so that I can see the products

    Background:
        Given I am on the login page

    @smoke
    Scenario: Successful login with a standard user
        when I log in as "standard_user" with password "secret_sauce"
        Then I should see the products page

    Scenario Outline: Login is rejected with invalid data
        when I log in as "<username>" with password "<password>"
        then I should see the login error "<message>"

        Examples:
            | username        | password      | message                                                                    |
            | locked_out_user | secret_sauce  | Epic sadface: Sorry, this user has been locked out.                        |
            | standard_user   | wrong_pass    | Epic sadface: Username and password do not match any user in this service  |
            |                 | secret_sauce  | Epic sadface: Username is required                                         |
            |standard_user    |               | Epic sadface: Password is required                                         |

    Scenario: Products page cannot be opened without login
        when I open the products page directly
        then I should see the login error "Epic sadface: You can only access '/inventory.html' when you are logged in."

