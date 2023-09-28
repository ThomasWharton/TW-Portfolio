//Skill Description Box

const skillIcons = Array.from(document.querySelectorAll('.skill-icon'));
const defaultSkill = document.querySelector('#default-skill-p')
const skillName = document.querySelector('#skill-name');
const skillDescription = document.querySelector('#skill-description');
const skillHeadingIcon = document.querySelector('#skill-heading-icon')


// Take icon info and replace elements in skill description box
const updateInfo = (name, description, image) => {
    skillHeadingIcon.src = image;
    skillName.innerHTML = name;
    skillDescription.innerHTML = description;
    skillHeadingIcon.classList.remove('hidden');
    skillName.classList.remove('hidden');
    skillDescription.classList.remove('hidden');
    defaultSkill.classList.add('hidden');
};

// Pull info from skill icons when clicked
const pullIconInfo = () => {
    skillIcons.forEach(skillIcon => {
        skillIcon.addEventListener('click', function () {
            let image = skillIcon.src;
            let name = skillIcon.alt;
            let description = skillIcon.title;
            updateInfo(name, description, image)
        })
    });
};

const initialise = async() => {
    pullIconInfo();
}

window.addEventListener("DOMContentLoaded", (event) => {
    initialise();
});
