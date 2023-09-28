//Skill Description Box

const skillIcons = Array.from(document.querySelectorAll('.skill-icon'));
const defaultSkill = document.querySelector('#default-skill-p')
const skillName = document.querySelector('#skill-name');
const skillDescription = document.querySelector('#skill-description');
const skillHeadingIcon = document.querySelector('#skill-heading-icon')

const updateInfo = (name, description, image) => {
    skillHeadingIcon.src = image;
    skillName.innerHTML = name;
    skillDescription.innerHTML = description;
    skillHeadingIcon.classList.remove('hidden');
    skillName.classList.remove('hidden');
    skillDescription.classList.remove('hidden');
    defaultSkill.classList.add('hidden');
};

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
