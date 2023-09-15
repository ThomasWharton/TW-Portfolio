# Thomas' Personal Portfolio Webpage

## Introduction

Welcome to my personal portfolio page, built as my project 4 for my CodeInstitute Full Stack Software Development Diploma.
The webpage will be geared towards showcasing my skills as a developer and sharing who I am as a person.

## Table of Contents

## UX

### User Stories
* As a user, I can click navigation links so that I can easily navigate the site. 
* As a user, I can fill in a contact form so that I can get in contact with the site owner.
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
There will also be functionality to download my CV and to contact me for further information or discuss working with me.
The site will have information to highlight my skills and showcase the projects I have previously completed. 
The aim is to attract future employers and show that I would be a worthy member of their team.

## Requirements
* Landing page.
* About section.
* Skills section.
* Project showcase section.
* Contact page.
* Downloadable CV.
* Links to social media.
* Login access for admins only to admin dashboard.
* CRUD functionality for admins to add, change or delete data.

## Design Choices

### Fonts

[Google Fonts](https://fonts.google.com/ "Google Fonts") has been used to select the fonts for the website. The font selected for the logo was [Playfair Display](https://fonts.google.com/specimen/Playfair+Display "Playfair display") as it is elegant and gives off a professional vibe. [Montserrat](https://fonts.google.com/specimen/Montserrat "Montserrat") was chosen for headings for its clean and striking aesthetic. [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab "Roboto Slab") was chosen for the body text for its readability and how easily it pairs with the other fonts selected.

### Colours

* #2E4052 - Charcoal header/footer
* #00AEFF - Picton Blue background
* #FFFFFF - White Text

### Icons

The icons used for the site were all sourced from [Font Awesome](https://fontawesome.com/ "Font Awesome").

## Structure

The structure of the site will be simplistic as to not deter the user from engaging with the content. The initial landing page will feature a brief description of myself including a picture. The user will be able to navigate to a page highlighting my skills, one for basic information about myself, one to showcase my projects and a contact form page. The site will be developed with a mobile first mindset and use bootstrap break points to restructure the layout dependent on the device. There will be a backend admin dashboard for the management of data used on the site. This dashboard will only be available to super users. The navbar will contain a login link and once logged in (admins only), the login link will change to one for the admin dashboard.

## Features

### Landing Page

The landing page will feature an image of myself along with some basic information in regards to the site and my coding jouirney. 

### Navbar

The navbar will be present on all pages and will contain navigation links to all the pages on the site. There will also be a log in link which will allow admins to log in and access the admin dashboard. Once an admin is logged in, the log in link will change to log out and an extra button for the admin dashboard will be present.

### About Me Page

The about me page will give more information about myself than the original landing page. Information such as my current location, more on my coding journey and work history.

### Skills Page

Tne skills page will highlight what coding related skills I have learned thus far and how strong of an understanding I have with each. The skills page will show a table with icons for each skill which will be a clickable button. When clicked, I modal will appear with information on how strong my knowledge is on each skill.

### Project Page

The project page will contain a look at all the projects I have completed so far with links to the repositories and the live sites for each. There will be an image and brief description of each project.

### Contact Page

The contact page will contain a form which a user can fill in with basic details and a message to send me. This can be used to contact me about potential work opportunities, for collaboration on a project or even if they would just like to get to know me better. There will also be a link to download a PDF version of my CV on this page.

### Admin Dashboard

The admin dashboard will be used to create, update or delete information used on the site. This will only be available to admins and will be accessable once logged in. 

### Footer

The footer will be present on each page and contain links to my social accounts.