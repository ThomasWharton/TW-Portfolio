//Skill Description Box

const skillDescriptionBox = document.querySelector('#skill-description-box');
const skillIcons = Array.from(document.querySelectorAll('.skill-icon'));

const updateInfo = () => {
    skillDescriptionBox.innerHTML = "<h3>{{ skill.name }} {{ skill.skill_icon }}</h3>"
};

const initialise = async() => {
    skillIcons.forEach(skillIcon => {
        skillIcon.addEventListener('click', updateInfo)
    });
}

window.addEventListener("DOMContentLoaded", (event) => {
    initialise();
});
