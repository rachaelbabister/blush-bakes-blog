# BLUSH BAKES BY RACH BLOG - TESTING

![Blush Bakes by Rach shown on a range of devices, using amiresponsive(https://ui.dev/amiresponsive)](readmefiles/images/ux/responsivedesigns.jpg)

LIVE SITE

[You can view the live site here.](https://blush-bakes-blog-2f3197aab1bc.herokuapp.com/)

## CONTENTS

- [BLUSH BAKES BY RACH - TESTING](#blush-bakes-by-rach---testing)
  - [CONTENTS](#contents)
  - [AUTOMATED TESTING](#automated-testing)
    - [W3C Validator](#w3c-validator)
    - [Lighthouse](#lighthouse)
    - [Desktop Results](#desktop-results)
    - [Mobile Results](#mobile-results)

Testing was continually carried throughout the build process of this website. There were some User Stories that tested my own patience and resilience during this project (!), and required more fixing than others, which did mean that time didn't allow for other User Stories to get completed, eg. Contact page.

With that in mind, the site doesn't fully reflect what was built in the wireframes, but I'm pleased with how close it is.

Chrome Developer Tools has been extremely useful to bug the code and inform me where things may have been going wrong.

I used the W3C Validator to check my HTML and CSS source code, JSHint to check any JavaScript code, and also LightHouse within Chrome Developer Tools to test the performance and accessibility. These are explained in more detail below.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the source code for both the html and css on all pages of the website. Apart from the issues detailed below, there were no other errors or warnings to show.


- [Home page](readmefiles/images/testing/index-validator.png)
  - Not able to use an 'a' element as a child element of 'ul'. FIX - wrapped the 'a' within an 'li' element.
- Recipe Pages
- [Error 1](readmefiles/images/testing/recipepages-validator.png)
  - Elements 'h2', 'p' and 'hr' now allowed as a child element of 'span'. FIX - changed the 'span' element within recipe_detail.html to a 'div'.
- [Error 2](readmefiles/images/testing/recipepages-validator2.png)
  - Tag errors. FIX - change 'p' tag to a 'div' and remove stray 'div' end tag.
- [Category pages](readmefiles/images/testing/category-validator.png)
  - Trailing slash on void element. FIX - remove the trailing slash from 'hr'.
- [Logout page](readmefiles/images/testing/logout-validator.png) 
  - Not able to use 'button' element as a descendant of 'a' element. FIX - remove 'button' tag. 
- [CSS stylesheet](readmefiles/images/testing/css-validator.png)
  - Property 'justify' doesn't exist on .jump-button. FIX - .jump-button class was removed from stylesheet after reviewing it wasn't adding any style to the button, and the recipe_detail.html template was amended to remove any instances of the class.
  - Also a parse error. FIX - added a missing '}' bracket to the end of the stylesheet.

### JSHint Validator

- [script.js](readmefiles/images/testing/javascript-validator.png)
  - A missing semicolon - after reviewing the script file, I'm not sure where I would add a missing semicolon so this has been left.
  - Undefined and unused variables - these are used within the template pages of the site.


### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

#### Desktop Results

I came across some issues with Cloudinary causing low scores on Best Practices. I added in some code to ensure images were secure in my settings.py and when run again, this did improve the scores. Interestingly, when Lighthouse is run in incognito mode, the score improves on some pages. I have included both below.

- Home Page
  - Public
![Public](readmefiles/images/testing/home-lighthouse-public.png)
  - Incognito
![Incognito](readmefiles/images/testing/home-lighthouse-incognito.png)

- Recipes/Category
  - Public
![Public](readmefiles/images/testing/recipes-lighthouse-public.png)
  - Incognito
![Incognito](readmefiles/images/testing/recipes-lighthouse-incognito.png)

- Register page
  - Public  
![Public](readmefiles/images/testing/register-lighthouse-public.png)

- Profile page
  - Public  
![Public](readmefiles/images/testing/profile-lighthouse-public.png)


#### Mobile Results

Unfortunately Performance had a low score on mobile results. Some the issues were to do with the Cloudinary images, and other images which could have a lower image size for mobile viewing. 

- Home
  - Public
![Public](readmefiles/images/testing/mobile-home-public.png)
  - Incognito
![Public](readmefiles/images/testing/mobile-home-incognito.png)

- Recipes/Category
  - Public
![Public](readmefiles/images/testing/mobile-home-public.png)
  - Incognito
![Incognito](readmefiles/images/testing/mobile-home-public.png)

- Register page
  - Public  
![Public](readmefiles/images/testing/mobile-register-public.png)

- Profile page
  - Public  
![Public](readmefiles/images/testing/mobile-profile-public.png)

