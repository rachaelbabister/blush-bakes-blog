# BLUSH BAKES BY RACH | RECIPE BLOG


Welcome to the Recipe Blog by Blush Bakes by Rach. Utilising the existing branding and style from my business website, I've built this blog with a focus on elegant simplicity, wanting to share my baking passion with a wider audience.

Using a combination of HTML, CSS, JavaScript, and Python using the Django framework, this blog offers a responsive experience across all devices, whether on your desktop, tablet, or phone -  the content is easy to navigate and visually appealing.

As a visitor to the site, you'll find a diverse selection of baking recipes, ranging from cakes and cupcakes to biscuits and brownies. You're invited to register an account, enabling you to engage with the community by commenting on recipes and sharing your own baking experiences.

One of the highlights of this blog is the ability to save your favourite recipes directly to your profile, giving easy access to the recipes at a later date.

![Blush Bakes by Rach Recipe Blog shown on a range of devices, using amiresponsive(https://ui.dev/amiresponsive)](readmefiles/images/ux/responsivedesigns.jpg)

LIVE SITE

[You can view the live site here.](https://blush-bakes-blog-2f3197aab1bc.herokuapp.com/)

GITHUB PAGES

[You can view the GitHub code pages here.](https://github.com/rachaelbabister/blush-bakes-blog)


---

## CONTENTS

- [BLUSH BAKES BY RACH](#blush-bakes-by-rach)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
      - [Client Goals](#client-goals)
      - [First Time Visitor Goals](#first-time-visitor-goals)
      - [Returning Visitor Goals](#returning-visitor-goals)
      - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [General features on each page](#general-features-on-each-page)
      - [Home Page](#home-page)
      - [Gallery](#gallery)
      - [Contact](#contact)
      - [Thank You](#thank-you)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### User Stories

Blush Bakes by Rach is a company run by cake artist, Rachael Babister. This website is dedicated to sharing delightful baking recipes; whether you're a seasoned baker or just starting out, you'll find an array of mouth-watering recipes for cakes, cupcakes, biscuits, brownies, and more. Rachael wants to share her recipes with the baking community, enabling users to comment and share their experiences with the recipes, as well as saving their favourites to their profile page in order to come back to them at a later date.

#### Client Goals

- To easily add new recipes to the blog to share with the baking community.
- To enable site visitors to comment on individual recipes and have these posted once approved.
- Site visitors to be able to create a profile and save their favourite recipes.
- For site visitors to be able to get in touch with Blush Bakes by Rach Recipe Blog with an enquiry.
- To easily navigate through the site on any device, whether a mobile phone or a desktop computer.

#### First Time Visitor Goals

- I want to see a good mix of different baking recipes I can make.
- I want to see what other people are saying about the recipes, any tips etc.
- I want to be able to add my own comments to a recipe.
- I want to be able to save my favourite recipes to my profile.
- I want to be able to search for recipes by category.
- I want to know if a recipe is easy to do.
- I want to be able to get in touch using a contact form.
- I want to find out more about the baking business on their Social Media pages.

#### Returning Visitor Goals

- I want to be able to login to my profile and view my saved recipes.
- I want to have a look at what other people have been saying about the recipes.
- I want to delete a previous comment I made.

#### Frequent Visitor Goals

- I want to see if there are any new recipes on the blog.
- I want to add more or delete favourite recipes to my profile.
- I want to amend the details of my profile.

### Agile Methodology

Before work started on the build of the website, I created a Board of User Stories to determine exactly what was needed. Using the MoSCoW method, it was much easier to implement each issue based on their priority rather than trying to get everything completed. My User Story Board can be viewed [here.](https://github.com/users/rachaelbabister/projects/3/views/1)

---
## Design

### Colour Scheme

The colour scheme for the website came from the colours that were used in the main Blush Bakes by Rach website.

![Blush Bakes by Rach colour palette](readmefiles/images/ux/colour-palette.png)

### Typography

- Reenie Beenie: A cursive font used for headings throughout the website, offering a touch of elegance that resonates with the branding and logo aesthetics.
- Raleway: A clean sans-serif font, with good legibility for the main body text, giving a modern appearance for easy reading, enhancing the overall user experience. 

![Google Fonts used by Blush Bakes by Rach](readmefiles/images/ux/googlefonts.png)

Font Awesome is also used for the 'back to top' arrow on the website and the comments icon.

### Imagery

The type of imagery used on the website is all photography. The logo was designed by me, and the main header photo was taken by myself. The recipe photo's have been taken from Google search and are referenced in Credits.

### Wireframes

Before implementing the website, I created Wireframes for each page using Balsamiq. You can access them [here](readmefiles/images/wireframes).

### Data Models

Various data models were drawn out before creating the actual models, to serve as a blueprint for database design, helping with concepts and organisation of the structure of a database. 

![Blush Bakes by Rach Data Models](readmefiles/images/ux/datamodels.png)

#### Relationships:

#### Recipe Posts:
- User (OneToMany): Each recipe is written and posted by a user. This relationship indicates a OneToMany relationship, where one user can create multiple recipe posts, but each recipe post is associated with only one user.

#### Comments:
- Recipe Post (OneToMany): Comments are associated with recipe posts, following a OneToMany relationship. Each recipe post can have multiple comments, but each comment is linked to only one recipe post.
- User (OneToMany): Similarly, comments are posted by users, forming another OneToMany relationship. A user can write multiple comments, but each comment is attributed to only one user.

#### User Profile:
- User (OneToOne): Each user has a user profile, establishing a OneToOne relationship. This ensures that each user has a single profile, and vice versa.

#### Contact Page:
- User (ManyToOne): The contact page allows users to send messages via a form. This establishes a ManyToOne relationship with users, as multiple messages can be sent by different users, but each message is associated with only one user.

#### Category:
- Recipe Categories (ManyToMany): Recipe posts can belong to multiple categories, while each category can have multiple recipe posts. This establishes a ManyToMany relationship, allowing for flexible categorisation of recipes.

### Website Security

#### env.py File
- Storing sensitive information on a website is vital to keep your website safe. API keys and databases are stored in the env.py which is not included in version control to prevent exposure.

#### Defensive Programming
- Using secure coding techniques such as {%%} and @login_required helps to restrict unauthorised actions on the site, ensuring certain functions are only seen by authorised users.

#### Input Validation
- A plus to using Django is utilising their built-in form validation framework. The system can check for exising users, required fields and password confirmation, triggering errors if anything doesn't meet the requirements.

#### User Feedback
- Flash messages are used to feedback to a user when a certain action has been processed - whether successful or not. The user has a much more improved experience, feeling confident they know the processes of what is happening with their actions on the site.

---

## Features

### General features 

- The site is easily navigated with recipes appearing on the home, so users can start choosing a recipe straight away. 
- A drop down menu features difference categories to choose a recipe based on flavour or type of bake.
- A user can register on the site to make comments on recipes and save their favourite recipes. 
- All pages show the branding of the company with a logo and styling to match. A responsive navigational bar is in a header at the top of the page.
- Social media links can be found in the footer, with links for Facebook & Instagram, along with a contact link. These are shown as icons.
- There is a 'back to top' button for longer pages in the bottom right corner, making it easier for users to scroll to the top of the page.

![Blush Bakes by Rach Recipe Blog shown on a range of devices, using amiresponsive(https://ui.dev/amiresponsive)](readmefiles/images/ux/responsivedesigns.jpg)


#### Home Page

- NAV BAR: Is the same on every page. Logo on the left with main page navigation just to the left, with account management links to the right of the page. These change when you are signed in so you can access your profile page or logout. There is also a category drop down menu under Recipes, which when you select one will only show recipes within that category.

![NavBar](readmefiles/images/screenshots/navbar.png)

![NavBar - Logged in](readmefiles/images/screenshots/navbar-loggedin.png)

![NavBar - Categories](readmefiles/images/screenshots/category-dropdown.png)

- Header: Features the nav bar and a full width image strip and heading of 'Tasty Baking Recipes'.

![Header](readmefiles/images/screenshots/header.png)

- MAIN CONTENT: Features recipe posts with a small description underneath an image of the recipe. Users can see what the recipe is, a small excerpt, the difficulty rating, and who it was posted by and when. A user can click on the image or content of the recipe card to be taken to the full recipe page.

![Home Page Main Content](readmefiles/images/screenshots/maincontent-home.png)

![Home Page Main Content](readmefiles/images/screenshots/recipelinks-home.png)

- PAGINATION: At the bottom of the recipe cards/links there are pagination buttons depending on how many pages there are and what page you are on. You can scroll forwards and backwards using these.

![Home Page Pagination](readmefiles/images/screenshots/pagination.png)

- FOOTER: A pink background banner stretching across the width of the site, with social media links and a copyright message.

![Footer](readmefiles/images/screenshots/footer.png)

#### User Account

- SIGN UP: Users are able to fill in their details to create a user profile on the website, in order to be able to make comments and add favourites.

![Sign Up](readmefiles/images/screenshots/signup.png)

- SIGN IN: Allows registered users to sign in and access features on the site.

![Sign In](readmefiles/images/screenshots/signin.png)

- PROFILE PAGE: Users can access their profile page in order to view their favourite recipes and see their personal information. They also have the ability to delete the recipes listed in their favourites.

![Profile](readmefiles/images/screenshots/profileinfo.png)
![Delete Favourites ](readmefiles/images/screenshots/favourites-delete.png)

- FLASH MESSAGES: Users will get flash messages at the top of the main content (underneath the main header of the page), notifying them of an action that has taken place.

![Flash Messages](readmefiles/images/screenshots/flashmessages.png)
![Flash Messages](readmefiles/images/screenshots/flashmessages2.png)

- SIGN OUT: Users can use the sign out button in the main nav bar to sign out of their account. They are asked to confirm if they would like to sign out, or return back to the home page if they want to stay logged in.

![Sign Out](readmefiles/images/screenshots/signout.png)

#### Recipe Posts

- RECIPE HEADER: When a user clicks on a recipe from the home page, they get taken to a detailed page of that recipe. At the top is a larger image of the food, and the same details as on the recipe card - title, difficulty rating, excerpt and posted by and when. There is also a 'back to previous page' button, which will take the user back to the previous page they were on.

![Recipe Header](readmefiles/images/screenshots/recipe-header.png)

- RECIPE DETAILS: Underneath the image are the recipes ingredients and method. Some recipes may have information paragraphs from the author, and so to help with user accessibility, there is a Jump to Recipe button so it auto scrolls to the actual recipe.

![Recipe Details](readmefiles/images/screenshots/recipe-details.png)

- HEART ICON: The heart icon in the top right of the recipe header enables users to add that recipe to their favourites. They can access them when they visit their profile page. A user is only able to see the heart when they are logged in.

![Heart Icon](readmefiles/images/screenshots/favourites-heart.png)

- COMMENTS: Comments appear underneath the recipe details. Once a comment has been approved by admin, anyone can view the comments. When they are under approval, only the user who posted the comment can see it, and is able to manage that comment with an edit or delete button. You can only make comments when you are logged in. If a user tries to delete a comment, they are asked to confirm and are able to cancel the delete should they wish.

![Comments](readmefiles/images/screenshots/comments.png)
![Manage Comments](readmefiles/images/screenshots/comment-manage.png)

#### Category View

- CATEGORIES: If a user wants to find a recipe by category, they can use the Recipe drop down menu on the main navigation bar. Once clicked, only the recipes under that category will show. To view all recipes again, they can click on Home or the logo which will also take you back to the home page.

![Category List](readmefiles/images/screenshots/category-view.png)

### Future Implementations

- Update or delete a user profile. (this should have been included in this design iteration, but time didn't allow)
- A contact form for users to get in touch. (this should have been included in this design iteration, but time didn't allow)
- A star rating on the recipes for users to rate a recipe, and for other users to see what the star rating is.
- A toggle of metric/imperial measurements on each recipe.
- Instructional videos for users to follow along.
- A printable versin of the recipe.
- Nutrional values for the recipes.
- The ability for a user to adjust ingredient quantities based on the size of the bake they want to do.
- Email subscription, with unsubscribe options too.
- A forgotten/reset password function.
- A search by keyword function.
- To be able to share the recipes on a users social media pages.

### Accessibility

I have tried to ensure the site has been made as accessible as possible by:

- Using semantic HTML.
- Using alt attributes on images where available.
- A responsive design.
- Using colour contrasts between the text and background.
- Readable fonts.
- User feedback where required.

---

## Technologies & Frameworks

### Main Technologies

- HTML & CSS - to create the structure and add styling to the site.
- JavaScript - for functionality.
- Django - a Python based framework for backend development.
- ElephantSQL - a Postgres database to store all data.

### Frameworks, Libraries & Programs Used

- Am I Responsive? - to showcase the website on different devices.
- Balsamiq - to create Wireframes.
- ChatGPT - to create a JSON file of all the recipes.
- Codeanywhere - cross platform cloud IDE to deploy workspace environment to Github.
- Cloudinary - cloud based storage for images.
- Font Awesome - to use icons on the website.
- Github - to store and dislay all files and assets for the website.
- Google Fonts - to import the fonts used on the website.
- Google Image Search - to find images for the recipes.
- Google Dev Tools - to troubleshoot, test and solve issues with any styling.
- Heroku - for hosting and deployment of the site.
- Lighthouse - to test the accessibility of the site.
- Lucid - to create my Data Models.
- Photoshop 2023 - to optimise images for the website.
- W3C Markup Validator - to check the source code of my html files for any bugs.
- W3C CSS Validator - to check the source code of my css file for any bugs.

### Deployment





I used Github Pages to deploy the live website. To deploy a website on Github, follow these steps:

1. Log in to Github - or set up a new account.
2. Find the repository for [Blush Bakes by Rach](https://github.com/rachaelbabister/blush-bakes-by-rach).
3. Click on 'Settings' along the top.
4. Click on 'Pages' in the left hand side navigation bar.
5. In the 'Source' section, ensure 'Deploy from a branch' is selected. Choose 'main' and 'Root' from the drop down menus and click Save.
6. Your live site is now deployed and can be viewed using the link provided.

### Local Development

#### How to Fork

To fork a repository on Github, follow these steps:

1. Log in to Github - or step up a new account.
2. Click on the repository for [Blush Bakes by Rach](https://github.com/rachaelbabister/blush-bakes-by-rach).
3. Click the Fork button in the top right corner.

#### How to Clone

To clone a repository on Github, follow these steps:

1. Log in to Github - or step up a new account.
2. Find the repository for [Blush Bakes by Rach](https://github.com/rachaelbabister/blush-bakes-by-rach).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and paste the link you copied in step 3. Press enter.

- - -


## Testing

I have learnt from this project to ensure I start my TESTING file from the begining in future. I continually test the site as I go along and have fixed many small issues that didn't work straight away, but unfortunately these weren't catalogued.

In the TESTING file linked below, you can see the tests and fixes I did manage to catalogue.
  
[TESTING.md file](TESTING.md)

---

## Credits

### Code Used

- [W3Schools](https://www.w3schools.com/howto/howto_css_transition_hover.asp) - helped to style my buttons to have a smoother transition. I also used them for a Font Awesome tooltip, but have since removed the element that used it.
- [W3Docs](https://www.w3docs.com/snippets/css/display-the-hidden-element-on-hovering-over-hyperlink-or-a-tag.html) - helped to display an element on hover.
- [RapidTables](https://www.rapidtables.com/convert/color/hex-to-rgb.html) - converting hex colours to rgb values.
- [Stack Overflow](https://stackoverflow.com/questions/51893686/css-columns-fill-row-first) - helped to style my gallery page so that the columns filled the rows across first, rather than down.
- [Free Code Camp](https://www.freecodecamp.org/news/css-only-back-to-top-button/) - helped to code the 'back to top' button using only html and css.
- [W3Docs](https://www.w3docs.com/tools/code-editor/3033) - styling to increase the checkbox size in the contact form.
- [Soft Author](https://softauthor.com/css-flexbox-responsive-registration-form-with-source-code/) - used the code in order to help make the contact form responsive by having the form elements go into two columns on a bigger screen.
- I also used the [Love Running](https://rachaelbabister.github.io/loverunning/) project I created with [Code Institute](https://codeinstitute.net/) to help with some coding.

### Content

All content used on the site was written by Rachael Babister.

### Media

All photos were taken by Rachael Babister and are originals. Icons used on the site are Font Awesome icons.
  
### Acknowledgments

I would like to thank the following people for their help, whether directly or indirectly!

- My two daughters who have been very patient with me whilst doing this project, and helping to walk the dog and clean the house!
- My Code Institute Mentor [Jubril Akolade](https://www.linkedin.com/in/jubrillionaire/?originalSubdomain=ca).
- Members of the Code Institute Slack community. Although I didn't ask any direct questions for help, when searching for little queries, I always managed to find the answer!
- My friend Victoria Walters who has had to listen to me chat about code for far too long! And for looking over my site and checking for errors.
- My friend Kelly Bates who knows nothing about code but still happily looked through my live site for me checking for any issues - and bringing some to my attention!
- [Stuart Crang](https://www.linkedin.com/in/stuart-crang-50401897/) from Code Institute who signed me up to the course! I hope you like my first project!
