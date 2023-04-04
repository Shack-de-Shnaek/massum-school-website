const sections = document.querySelectorAll('section');

let invisibleSections = [];

const sectionFadeIn = () => {
    for (const section of invisibleSections) {
        if (window.scrollY >= section.offsetTop - window.innerHeight + 300) {
            section.classList.remove('opacity-0');
            invisibleSections.splice(invisibleSections.indexOf(section), 1)
        }
    }
}

window.addEventListener('load', () => {
    if (window.innerWidth >= 576) {
        for (const section of sections) {
            section.classList.add('opacity-0');
        }
        invisibleSections = Array.from(sections);
        sectionFadeIn();
    }
});
window.addEventListener('scroll', sectionFadeIn);