# Thomas' Personal Portfolio Webpage

![Site Image](static/media/screenshots/home-desktop.png)

[View live project here.](https://tw-portfolio-f81a23484316.herokuapp.com/)

## Introduction

Welcome to my personal portfolio page, built as my project 4 for my CodeInstitute Full Stack Software Development Diploma.
The webpage will be geared towards showcasing my skills as a developer and sharing who I am as a person.

## Table of Contents

## UX

### User Stories
* As a user, I can click navigation links so that I can easily navigate the site. 
* As a user, I can access social media links so that I can see other activity from the site owner.
* As a user, I can download the site owners CV so that I can view their professional credentials.
* As a user, I can view the skills of the site owner so that I can get an idea of how they are progressing as a developer.
* As a user, I can view basic information about the site owner so that I can get a feel of what type of person they are.
* As a user, I can view projects completed by the site owner so that I can see how they have implemented their skills.

### Admin Stories
* As an admin, I want a secure log-in so that I can access the admin dashboard.
* As an admin, I want CRUD functionality so that I can create, read, update and delete data.
* As an admin, I want log-in validation so that only super users (admins) have access to the admin dashboard.
* As an admin, I want templates to pull information from the database so that it can be viewed by general users.

## Website Goals

The goals of this website are to showcase my journey as a developer and share what I am like as a person.
There will also be functionality to download my CV.
The site will have information to highlight my skills and showcase the projects I have previously completed. 
The aim is to attract future employers and show that I would be a worthy member of their team.

## Requirements
* Landing page.
* About section.
* Skills section.
* Project showcase section.
* Downloadable CV.
* Links to social media.
* Login access for admins only to admin dashboard.
* CRUD functionality for admins to add, change or delete data.

## Design Choices

### Fonts

[Google Fonts](https://fonts.google.com/ "Google Fonts") has been used to select the fonts for the website. The font selected for the logo was [Playfair Display](https://fonts.google.com/specimen/Playfair+Display "Playfair display") as it is elegant and gives off a professional vibe. [Montserrat](https://fonts.google.com/specimen/Montserrat "Montserrat") was chosen for headings for its clean and striking aesthetic. [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab "Roboto Slab") was chosen for the body text for its readability and how easily it pairs with the other fonts selected.

### Colours

![Colour Palette](static/media/screenshots/colour-palette.png)

* #000080 - Navy Blue header/footer
* #00AEFF - Picton Blue background
* #FFFFFF - White Text

### Icons

The icons used for the site were sourced from [Font Awesome](https://fontawesome.com/ "Font Awesome") and [Devicon](https://devicon.dev/ "Devicon").

## Structure

The structure of the site will be simplistic as to not deter the user from engaging with the content. The main site will be broken into sections and be a continuous scroller for ease of reading. There will be a backend admin dashboard for the management of data used on the site. This dashboard will only be available to super users. The navbar will contain a login link and once logged in (admins only), the login link will change to one for the admin dashboard.

### Database Models

Home:<br>

| Object            | Field           |
|-------------------|-----------------|
| hero_image        | CloudinaryField |
| main_heading      | CharField       |
| brief_description | CharField       |

Personal Details:<br>

| Object             | Field           |
|--------------------|-----------------|
| detail_paragraph_1 | CharField       |
| detail_paragraph_2 | CharField       |
| full_name          | CharField       |
| nationality        | CharField       |
| nationality_flag   | CloudinaryField |
| residence          | CharField       |

Skill:<br>

| Object            | Field      |
|-------------------|------------|
| name              | CharField  |
| skill_icon        | URLField   |
| skill_description | CharField  |
| category          | ForeignKey |

Skill Category:<br>

| Object            | Field      |
|-------------------|------------|
| category          | CharField  |

Project:<br>

| Object              | Field           |
|---------------------|-----------------|
| name                | CharField       |
| project_image       | CloudinaryField |
| project_description | CharField       |
| site_link           | URLField        |
| repo_link           | URLField        |

Work History:<br>

| Object       | Field     |
|--------------|-----------|
| company_name | CharField |
| start_date   | DateField |
| end_date     | DateField |
| position     | CharField |

Education:<br>

| Object         | Field     |
|----------------|-----------|
| place_of_study | CharField |
| accreditation  | CharField |
| start_date     | DateField |
| end_date       | DateField |

## Wireframes

Wireframes have been created using [Balsamic](https://balsamiq.com "Balsamic"). These wireframes gave a basic view of how my portfolio was going to be laid out. The layout may have changed slightly in the finished product.

*Home Desktop Wireframe*<br>
![Home Desktop Wireframe](static/media/wireframes/home-desktop-wireframe.png)

*Home Mobile Wireframe*<br>
![Home Mobile Wireframe](static/media/wireframes/home-mobile-wireframe.png)

*About Desktop Wireframe*<br>
![About Desktop Wireframe](static/media/wireframes/about-desktop-wireframe.png)

*About Mobile Wireframe*<br>
![About Mobile Wireframe](static/media/wireframes/about-mobile-wireframe.png)

*Skills Desktop Wireframe*<br>
![Skills Desktop Wireframe](static/media/wireframes/skills-desktop-wireframe.png)

*Skills Mobile Wireframe*<br>
![Skills Mobile Wireframe](static/media/wireframes/skills-mobile-wireframe.png)

*Projects Desktop Wireframe*<br>
![Projects Desktop Wireframe](static/media/wireframes/projects-desktop-wireframe.png)

*Projects Mobile Wireframe*<br>
![Projects Mobile Wireframe](static/media/wireframes/projects-mobile-wireframe.png)

## Features

### Home Section

The landing page will feature an image of myself along with some basic information in regards to the site.

*Home Desktop*<br>
![Home Desktop](static/media/screenshots/home-desktop.png)

*Home Mobile*<br>
![Home Mobile](static/media/screenshots/home-mobile.png)


### Navbar

The navbar will be present on all pages and will contain navigation links to all the pages on the site. Once logged in as admin, an additional button for the dashboard will show on the navbar. There will be a different navbar for the dashboard, only consisting of a home, dashboard and logout link. The navbar will change to a toggle icon with a dropdown list once the screen size drops below a certain width.

*Navbar Desktop*<br>
![Navbar Desktop](static/media/screenshots/nav-desktop.png)

*Navbar Mobile*<br>
![Navbar Mobile](static/media/screenshots/nav-toggle.png)

*Navbar Admin*<br>
![Navbar Admin](static/media/screenshots/admin-navbar.png)

*Navbar Dashboard*<br>
![Navbar Dashboard](static/media/screenshots/dashboard-nav.png)

### About Me Section

The about me section will give more information about myself than the original landing page. Information such as my current location, more on my coding journey and work history.

*About Desktop*<br>
![About Desktop](static/media/screenshots/about-desktop.png)

*About Mobile*<br>
![About Mobile](static/media/screenshots/about-mobile.png)

### Skills Section

Tne skills section will highlight what coding related skills I have learned thus far and how strong of an understanding I have with each. The skills page will show a table with icons for each skill which will be a clickable button. When clicked, the description box will update with more detailed information about that particular skill.

*Skills Desktop*<br>
![Skills Desktop](static/media/screenshots/skills-desktop.png)

*Skills Mobile*<br>
![Skills Mobile](static/media/screenshots/skills-mobile.png)

### Projects Section

The project section will contain a look at all the projects I have completed so far with links to the repositories and the live sites for each. There will be an image and brief description of each project.

*Projects Desktop*<br>
![Projects Desktop](static/media/screenshots/projects-desktop.png)

*Projects Mobile*<br>
![Projects Mobile](static/media/screenshots/projects-mobile.png)

### CV Section

The CV section will contain a link to my CV on my GitHub repository where the user can download it.

*CV Desktop*<br>
![CV Desktop](static/media/screenshots/cv-desktop.png)

*CV Mobile*<br>
![CV Mobile](static/media/screenshots/cv-mobile.png)

### Admin Dashboard

The admin dashboard will be used to create, update or delete information used on the site. This will only be available to admins and will be accessable once logged in.

*Dashboard Desktop*<br>
![Dashboard Desktop](static/media/screenshots/dashboard-desktop.png)

*Dashboard Mobile*<br>
![Dashboard Mobile](static/media/screenshots/dashboard-mobile.png)

### Footer

The footer will be present on each page and contain links to my social accounts.

*Footer*<br>
![Footer](static/media/screenshots/footer.png)

## Admin Dashboard

For security purposes, the admin dashboard is only available to super users (admins). To login as an admin, you must navigate to the admin login by putting /admin at the end of the site url. Once logged in, you will be taken to the default django backend dashboard. You can navigate back to the site using the view site link in the navigation bar. Once back to the main site, a new link for the dashboard in the navigation bar will be present. Any attempts to navigate to the admin dashboard or any related page will result in redirection to the home page if the user is not logged in.

## CRUD Functionality

CRUD functionality is fully available in the admin dashboard. The dashboard itself contains cards for each model with the option to add, edit and delete data dependent on the model. The buttons on the cards will take you to each individual page for change in data.

### Home

The home section will only have an edit page as there is no need to add or delete any data.

*Edit Home*<br>
![Edit Home](static/media/screenshots/edit-home.png)

### About

The about section will only have an edit page. As this page is very similar to the edit home page, I have opted not to add a screenshot for this page.

### Skills

The skills section will have options to add, edit or delete data. It is important to be able to add more skills as I progress as a developer. In the edit and delete pages, the form will be accompanied by a table containing all of the current skills. Clicking on a particular skill will reload the page and propagate the form with that skills information.


*Add Skill*<br>
![Add Skill](static/media/screenshots/add-skill.png)

*Edit Skill*<br>
![Edit Skill](static/media/screenshots/edit-skill.png)

*Delete Skill*<br>
![Delete Skill](static/media/screenshots/delete-skill.png)

### Projects

The project section will have the options to add, edit or delete data. As I complete more projects, I need the ability to add these to the database. A list of the projects will accompany the form and can be selected to propagate the specific information for editing and deleting purposes.

*Add Project*<br>
![Add Project](static/media/screenshots/add-project.png)

*Edit Project*<br>
![Edit Project](static/media/screenshots/edit-project.png)

*Delete Project*<br>
![Delete Skill](static/media/screenshots/delete-project.png)

### Work History

The work history section will have the options to add or edit data. There is no need to have a delete function in this section.

### Education

The education section will be the same as for the work history section.

## Testing

## Technologies Used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript")
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

### Libraries & Framework

* [Django](https://en.wikipedia.org/wiki/Django_(web_framework) "Django")
* [Bootstrap](https://getbootstrap.com/ "Bootstrap")
* [Google Fonts](https://fonts.google.com "Google Fonts")

### Databases
 * [PostgreSQL](https://www.postgresql.org/ "PostgreSQL")
 * [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL")

### Tools

* [GitHub](https://github.com "GitHub")
* [Gitpod](https://gitpod.io "Gitpod")
* [Balsamic](https://balsamiq.com "Balsamic")
* [Coolors](http://coolors.co "Coolors")
* [DevTools](https://developer.chrome.com/docs/devtools "DevTools")
* [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn "Gitpod")
* [Cloudinary](https://cloudinary.com/ "Cloudinary")
* [Heroku](https://heroku.com "Heroku")
* [Psycopg](https://wiki.postgresql.org/wiki/Psycopg "Psycopg")
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms")

## Development and Deployment

### Development

#### Forking GitHub Repository

Forking allows you to make a copy of a chosen repository to your own GitHub account. This allows you to test and edit the project without making changes to the original. Forking is done by following these steps.

1. Whilst logged into your GitHub account, navigate to the repository you would like to fork.
2. Click on the **Fork** button at the top right of the page.
3. Choose a name to give the repository. It will be intially named as the same as the original repository.
4. Click the **Create Fork** button.

#### Cloning GitHub Repository

Cloning allows you to download a local version of a chosen repository. Cloning can be done by following these steps.

1. Whilst logged into your GitHub account, navigate to the repository you would like to clone.
2. Click the green **<> Code** button.
3. Click on the **Local** tab.
4. Select **HTTPS** and copy the url.
5. Open your chosen IDE and ensure Git is installed.
5. In your IDE terminal type **git clone (url link that you copied)** and hit enter.

#### Cloudinary

1. Navigate to [Cloudinary](https://cloudinary.com/ "Cloudinary") and create an account.
2. Log in.
3. Navigate to your dashboard and copy the API Enviroment variable.
4. Keep a note of this variable as you will need to add it to your env.py file in your project.

#### ElephantSQL

1. Navigate to [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL") and create an account.
2. Once logged in, create new instance.
3. Select a plan, Tiny Turtle is the free to use plan.
4. Select a region, one closest to yourself.
5. Click create instance.
6. Select newly created instance.
7. Copy and make note of instance URL as this will be added to your env.py file.

#### env File

You need to create an env.py file in the root folder of your repository. This is where you assign hidden variables for security reasons. This file must be added to your list of ignored files in git.ignore to ensure it does not get pushed up to your repository on GitHub as it would then be publicly accessible.

*env.py*<br>
![env.py](static/media/screenshots/env-file.png)

For the DATABASE_URL variable, assign it your elephantSQL instance URL.
For the SECRET_KEY variable, assign a secret key of your choosing. You can generate one at [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/).
For the CLOUDINARY_URL, assign it your API Enviroment variable (you need to remove everything before cloudinary://).

As you can see in the picture above, I have a variable named DEBUG which is set to 1. The reason for this is because when I assign DEBUG in my settings.py file, I can assign it to this value. A string with a value in it is considered to be a boolean value of True, meaning DEBUG=True for my production environment. Due to the variable being set in my env.py file, it will not be pushed up to my repository and therefore default back to False. It is necessary to have DEBUG set to false for deployment purposes.

#### Requirements

The requirements for this particular project are as follows:<br>

asgiref==3.7.2<br>
backports.zoneinfo;python_version<"3.9"<br>
cloudinary==1.34.0<br>
crispy-bootstrap5==0.7<br>
dj-database-url==2.1.0<br>
dj3-cloudinary-storage==0.0.6<br>
Django==4.2.5<br>
django-allauth==0.56.1<br>
django-crispy-forms==2.0<br>
gunicorn==21.2.0<br>
oauthlib==3.2.2<br>
psycopg2==2.9.7<br>
PyJWT==2.8.0<br>
python3-openid==3.2.0<br>
requests-oauthlib==1.3.1<br>
sqlparse==0.4.4<br>
urllib3==1.26.16<br>

You can update your requirements file using the command in your IDE terminal:<br>
`pip freeze > requirements.txt`<br>
This is handy command to know for when you install any new components which would then be needed to be added to your requirements.

You can install all requirement packages using the following command in your IDE terminal:<br>
`pip3 install -r requirements.txt`<br>
*Disclaimer: Please check Python documentation for the correct terminal command as it may differ depending on the system you are using*


### Deployment

This project was deployed using [Heroku](https://www.heroku.com "Heroku") by following the steps detailed below.

1. Navigate to Heroku website and sign up or log in.
2. Navigate to your dashboard, select **New** and then **Create New App**.
3. Assign a unique name to your project, select your region and click **Create app**.
4. Navigate to **Settings** tab.
5. You need to add specific config vars to be able to deploy the project properly on Heroku. This is done by clicking on **Reveal Config Vars**, and adding them here. The config vars needed are listed below: <br>
CLOUDINARY_URL = Same as your CLOUDINARY_URL in your env.py.<br>
DATABASE_URL =  Same as your DATABASE_URL in your env.py.<br>
DISABLE_COLLECTSTATIC = 1 - This is needed so that it will not time out on deployment. Collect static must be completed in your IDE terminal each time a change is made to static files. Do this by running the command `python3 manage.py collectstatic`.<br>
PORT = 8000
SECRET_KEY = Another secret key here - Make sure it is different to the one in your env.py file for security reasons.

#### Deploying from a Github Repository

1. Navigate to **Deploy** tab.
2. Select **GitHub - Connect** for deployment method and connect your GitHub account by logging in with your GitHub details in the prompt.
3. Select your GitHub account from the dropdown list if not already preselected.
4. Search for your GitHub repository that you would like to deploy and click **Connect** on the respository in the search list.
5. Deployment options are found further down the **Deploy** tab with options for **Automatic Deploys** and **Manual Deploy**. Automatic deploys all for heroku to update your app everytime your GitHub is updated.
6. Choose your deployment option and the branch from which you would like to deploy.
7. If **Automatic deploys** is chosen, click on **Enable Automatic Deploys**. If **Manual deploy** chosen, click on **Deploy Branch**.
8. Heroku should now start the deployment process. Once successfully deployed, a message will appear saying **Your app was successfully deployed.** with a button to view your deployed application.

## Credits

I would like to thank my mentor [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin") for his continued support throughout the course.