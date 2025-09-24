document.addEventListener("DOMContentLoaded", function () {
  const scrollContainer = document.getElementById("pacil-scroll");
  const dots = document.querySelectorAll("#paginationDots .dot");

  if (!scrollContainer || dots.length === 0) return;

  scrollContainer.addEventListener("scroll", () => {
    const scrollLeft = scrollContainer.scrollLeft;
    const width = scrollContainer.offsetWidth;
    const index = Math.round(scrollLeft / width);

    dots.forEach((dot, i) => {
      dot.classList.toggle("active", i === index);
    });
  });
});
