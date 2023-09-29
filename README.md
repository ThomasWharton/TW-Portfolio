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