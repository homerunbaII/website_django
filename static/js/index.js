// navbar 스크롤 애니메이션

const navbar = document.querySelector('nav');
const navbarHeight = navbar.getBoundingClientRect().height;

document.addEventListener('scroll', () => {
    if(window.scrollY > navbarHeight) {
        navbar.classList.add('navbar--dark');
    } else {
        navbar.classList.remove('navbar--dark');
    }
});

window.addEventListener('scroll', () => {
	const bwLeft = window.scrollX;
	document.querySelector('nav').style.transform = `translateX(-${bwLeft}px)`;
  });