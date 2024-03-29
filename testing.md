# Green Cuisine -  Testing

![Green Cuisine presented with various screen sizes](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/mock-up-design/all-devices-white.png)

Visit the deployed site: [Green Cuisine](https://green-cuisine.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. I utilised Chat GPT, Chrome developer tools and Code Insitutes support team, whilst building to pinpoint and troubleshoot any issues as I went along.

During development I made use of google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using google chrome developer tools & Firefox inspector tool to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

- I removed all Jinja coding from the html files and tested on that basis. The errors seen from the W3C checker all relate to erros caused by removing the Jinja code, e.g. expecting to see a doctype first, the head element is missing - all related to html elements that do not appear in any of the files apart from the base.html. Otherwise there were no errors in the html.

* [home.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/home-page-test.png) - Passed.
* [register.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/register-page-test.png) - Passed
* [login.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/login-page-test.png) - Passed.
* [profile.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/profile-page-test.png) - Passed.
* [add_recipe.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/addrecipe-test-page.png)Passed.
* [all_recipe.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/allrecipe-page-test.png) - Passed.
* [edit_recipe.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/editrecipe-page-test.png) - Passed.
* [base.html](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/base-page-test.png) - Passed.

* [style.css](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/html-css-test-results/css-stylesheet-testpass.png) - Passed.

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [javascript.js](static/images/lighthouse-seo-results/Lighthouse Report Viewer.html) - Passed.

**Python**
- [PEP8 Online](http://pep8online.com/)
    - pycodestyle was used in the CLI to test compliance to pep8 and the file test 'threw' no errors

- - -

### Lighthouse Results

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

* [Overall results](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/seo-overall-results.png)
* [Opportunities report](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/opportunities-report.png)
* [Opportunities resport 2](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/opportunities-report-cont.png)
* [Seo page results](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/seo-report.png)
* [Best practice report](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/best-practice-report.png)
* [Accesibility report](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/accessibility-report.png)
* [PWA commentary](https://github.com/JMcbeath1966/Green-Cuisine/blob/main/static/images/lighthouse-seo-results/pwa-commentary.png)





- - -

## MANUAL TESTING

### Testing User Stories

* Due to time constraints the testing was conducted within my family - my wife, 4 daughters and my son! The devices used are detailed in the Full Testing section of this document

They were asked to look at the following criteria from the readme and comment on the requirements outlined, namely:

- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *view all recipes* as a **Guest**.
- :white_check_mark: *search all recipes* as a **Guest**.
- :white_check_mark: *filter recipes* by **recipe type - vegan/vegetarian**.
- :white_check_mark: *sort/order recipes* by **recipe title, description, ingredients, cooking time, and cuisine**.
- :white_check_mark: *create* my **own profile**.
- :white_check_mark: *add* my **own recipes**.
- :white_check_mark: *edit* my **own recipes**.
- :white_check_mark: *delete* my **own recipes**.
- :white_check_mark: be able to **log out**.
- :white_check_mark: be able to **change my password**.

They reported responsiveness issues at screen sizes between 600px, down to 400px on tablet/mobile devices. 
These were:
- Salad icon moving out of alignment in header
- Text and links became more difficult to read at small screen size
- The color of the link became very difficult to see at small screen size


- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 15 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 10 
  * iPhone X.
  * Kindle Fire.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox
* Edge


`Home Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The sites title | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| The site nav-brand | The page links to the home page | Clicked on nav-brand icon | Home page reloads | Pass |
| Navbar displays Home/Login/Register only | Navbar will add additonal pages | Clicked on close button | Screen refreshes smoothy to home page | Pass |
| Footer links | Open 3 external websites open to a new tabs| clicked on each link and open new tab for website | All links opened to new tabs | Pass | 

`Register Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|Register Below | User will be able to register username and a password by clicking on a register button | Once the register button is clicked a message will appear saying "Registration Successful and display the users profile name in username/profile format| On clicking the registration button both the message and username/profile details appear | Pass | 
| Username exists message | If your username exists a flash message saying "Username already exists - Please use a different name! | Various existing usernames were tested with the message appearing every time | Pass |
|Message below registration container to allow a user to login if already registered. This will be quicker to use than going back to the nav-bar to click on register again | The user will access see both a message (Already Registered?) | Login button tested and it takes the user to the login page| Pass |


`Login Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|On successfull login, profile page appears | Profile page displays with message to welcome user and the username profile| Tested with multiple usernames on login| Welcome message and username profile display successfully | Pass | 
|Unsuccessful login message | Due to defensive programming the login will be unsuccessul if the details entered do not match the criteria to login | I tested the defensive programmes parameters (e.g. No data entered, specific length of password etc) | Testing the defensive programs was carried out on different login accounts and was successful for the parameters used for the site | Pass |


`Profile Page`
Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|On successfull login, profile page appears | Profile page displays with message to welcome user and the username profile| Tested with multiple usernames on login| Welcome message and username profile display successfully | Pass | 
| Nav-bar to display liks for additional pages and Login is removed from nav-bar display | Add Recipes, All Recipes and Log Out pages will be added to Home and Profile pages | Profile page shows correct pages in the nav-bar | When profile is displayed, Home/Profile/Add Recipe/All Recipes/ all appear in the nav-bar. Login is removed | Pass |


`Add Recipe Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Six input areas display, one of the inputs being a dropdown modal | Inputs will be allowed up to the charachter lilmits set| All input fields were tested against charachter lengths by users | There were no issues |Pass |
| Add Recipe Button | On click, the All Recipe page will render with a flash message updating the user "Recipe added Successfully" | Tested MongoDB to ensure data is added and manually tested | The All Recipe page renders correctly with the flash message | Pass |
| Add Recipe Button | On click, the All Recipe page will render with the recipe added to the accordion dropdown with the recipe type and short description added" | Tested MongoDB to ensure data is added and manually tested | The All Recipe page renders correctly with the recipe type and description displayed | Pass |

`All Recipes Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Search Recipe bar | Users can search by keywords but must have minimum 3 charachters and the field must be entered - a modal message to enter more than 3 charachters should pop up. If nothing is entered then a modal pop up asking the user to fill in the field appears | The charachter and required requirements were tested manually | The functionality was tested manually and everything worked as expected | Pass |
| Filter/Sort by Recipe type| On click in the sort area or the dropdown arrow, the user can choose their recipe type, prior to using the filter recipe button | Functionality for both sort area and dropdown work as expected | Funcionality worked as expected under user test| Pass|
| Filter recipe button | On click the the filter recipe button will then sort recipes by the choosen option and display them in the accodion | User tested with recipes adding as expected | Filter works as expected | Pass |
| Display Edit button | Recipes can be edited in a rendered edit page on click of the edit button | Under manual testing the functionality works successfully | On click the user button renders to the new page successfully | Pass |
| Display Delete button | Recipes can be deleted on click of the delete button | Under manual testing the functionality works successfully | The funtionality works as expected| Pass |
| Dropdown "accordion" to display full recipe | On down arrow click, the full recipe will open and collapse | Dropdown worked on manual testing | Accordion opens and closes as expected| Pass |

`Edit Recipe Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Note * Edit page opens from the All Recipes page. In the Edit page,  users can amend recipe details in the Edit Page| Users amend input fields  | Manually tested, users can easily amend details prior to next action | Input fields are successfully entered | Pass |
 | Edit Recipe button/ Flash message | A user clicks on the edit recipe button and the amendments pass to the database. On click a message - "Recipe edited Successfully displays| Tested MongoDB to check the details have updated correclty and manually tested the menus have correctly updated| Edit Recipe updates inputs succesfully and flash message appears | Pass |
 |Cancel button | On click the user will go back to the All Recipe page | Manually tested, the user returns to the page| Functionality works | Pass |

`Log Out Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|Log out with flash message to confirm a user has logged out | The user logs out and the message "You have been logged out" displays | Manually tested only | The log out and return to the login page with the flash message is successful | Pass |

### Bugs and Fixes

Significant bugs were recorded as the project progressed and are detailed below:

`Bug`
| Bug  | Fix  | Resouces Used |
| --- | --- | --- |
| In my site footer from the Materialize site, the underline was not appearing on the a link and I wanted it to display, to be more prominent that a link had be clicked on to and improve user experience |I went back to my milestone 2 project where I had encountered a similar issue, reviewed the code and amended the css sheet to show: text-decoration: underline; | Milestone 2 project |
| Jinja error stating Undefined error. 'register' is undefined.| I traced the error and found I had missed the single quotes around the register variable. I compared the code to my github task_manager project to confirm the issue | GitHub and Code Insitute tutorial |
|Jinja error: Template not found | I used the error message to traceback to the issue and eventually found I'd missed quotes around the categories and added them in to resolve the error| Self review and Chat GPT |
| Jinja error: Template Syntax Error | After seeking tutoring support I realised I did not understand that my code was not reflecting the tables in MongoDB, and to be honest I had not understood the concepts stongly enough, so I asked the tutor support to overview the process for building an all_recipes function. My issue started with trying to get a quick fix by 'dumping' code from a tutorial and using that. It was the only time I did it and delayed my project, so lesson learned. I rectified the issue by going back over the code to identify the routes required for the POST and GET requests. Then reviewed the query for the database (and it's conversion to a cursor object, corrected the templates which was a naming issue which i quickly corrrected ) | Support from the Code Insitutue support and review of the key sections of building routes, database (naming functions to reflect the tables) |
| When trying to login with my original username/password it didn't work | On manually testing the site and checking code I realised I had my register and login template url's were back to front | Self review of code and website|
| Dropdowns/Options/Forms not working | I encountered this a few times but, in essence I was forgetting to add the required Javascript into the html templates which led to nothing happening when clicking on dropdown menu's| Self review of code and tutor support (once)|