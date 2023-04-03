// const counterContainer = document.querySelector('#counter-section');
// let counterHasStarted = false;
// const initiateCounters = () => {
//     if(window.scrollY >= counterContainer.offsetTop - window.innerHeight + 200 && !counterHasStarted) {
//         counter("years-counter", 0, 11, 2500);
//         counter("student-counter", 100, 350, 2500);
//         counter("professor-counter", 0, 18, 2500);

//         counterHasStarted = true;
//     };
// }


const sections = document.querySelectorAll('section');
for (const section of sections) {
    section.classList.add('opacity-0');
}

let invisibleSections = Array.from(sections);

const sectionFadeIn = () => {
    for (const section of invisibleSections) {
        if (window.scrollY >= section.offsetTop - window.innerHeight + 300) {
            section.classList.remove('opacity-0');
            invisibleSections.splice(invisibleSections.indexOf(section), 1)
        }
    }
}

window.addEventListener('load', sectionFadeIn);
window.addEventListener('scroll', sectionFadeIn);