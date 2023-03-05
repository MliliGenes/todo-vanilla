const container = document.querySelector(".container");

const personas = document.querySelectorAll(".persona");

const articles = document.querySelectorAll(".article");

personas.forEach((persona) => {
  persona.addEventListener("click", (e) => {
    let key = persona.getAttribute("data-key");

    articles.forEach((art) => {
      art.classList.remove("active");
    });

    let targetArticle = document.querySelector(`.article[data-key="${key}"]`);

    targetArticle.classList.add("active");
    container.classList.add("deactive");
  });
});

articles.forEach((art) => {
  let btn = art.querySelector("i");
  btn.addEventListener("click", (e) => {
    let targetArticle = btn.parentElement;
    targetArticle.classList.remove("active");
    container.classList.remove("deactive");
  });
});

window.addEventListener("keydown", (e) => {
  let currentArticle = document.querySelector(".active");
  if (e.key == "Escape") {
    currentArticle.classList.remove("active");
    container.classList.remove("deactive");
  }
});
