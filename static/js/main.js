const SHOWING = 'showing';
const firstSlide = document.querySelector('.slider-item:first-child');

function slide() {
    const currentSlide = document.querySelector(`.${SHOWING}`);
    if (currentSlide) {
        currentSlide.classList.remove(SHOWING);
        const nextSlide = currentSlide.nextElementSibling;
        if (nextSlide) {
            nextSlide.classList.add(SHOWING);
        } else {
            firstSlide.classList.add(SHOWING);
        }
    } else {
        firstSlide.classList.add(SHOWING);
    }
}

slide();
setInterval(slide, 1000);