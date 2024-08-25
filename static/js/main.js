document.querySelectorAll('.shine-effect').forEach(element => {
    element.addEventListener('mouseenter', () => {
      element.classList.add('shine-hover');
    });
    element.addEventListener('mouseleave', () => {
      element.classList.remove('shine-hover');
    });
  });
  