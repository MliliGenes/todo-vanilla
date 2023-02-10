window.addEventListener("load", () => {
  const root = document.querySelector(":root");
  const toggle = document.querySelector(".toggle");
  const dot = document.querySelector(".dot");
  const theme = document.querySelector(".theme");
  const vars = [
    "--bg-color",
    "--bg2-color",
    "--bg3-color",
    "--text-color",
    "--text2-color",
    "--textchecked-color",
  ];
  const lightColors = [
    "#d3d3d3",
    "#444343",
    "#858585",
    "#3a3a3a",
    "#ededed",
    "#ededed80",
  ];
  const darkColors = [
    "#1f1f1f",
    "#d5d5d5",
    "#a8a8a8",
    "#dbdbdb",
    "#272727",
    "#21212180",
  ];
  var themes = JSON.parse(localStorage.getItem("themes")) || {};
  function renderTheme() {
    if (themes["theme"] == "light") {
      dot.classList.remove("togglechecked");
      dot.classList.remove("bi-moon-stars-fill");
      dot.classList.add("bi-sun-fill");
      theme.innerText = "light";
      let index = 0;
      for (let v of vars) {
        let color = lightColors[index];
        root.style.setProperty(v, color);
        index++;
      }
    } else {
      dot.classList.add("togglechecked");
      dot.classList.add("bi-moon-stars-fill");
      dot.classList.remove("bi-sun-fill");
      theme.innerText = "dark";
      for (let v of vars) {
        let index = 0;
        for (let v of vars) {
          let color = darkColors[index];
          root.style.setProperty(v, color);
          index++;
        }
      }
    }
  }
  renderTheme();
  toggle.addEventListener("click", (e) => {
    if (themes["theme"] == "light") {
      themes["theme"] = "dark";
      localStorage.setItem("themes", JSON.stringify(themes));
      renderTheme();
    } else {
      themes["theme"] = "light";
      localStorage.setItem("themes", JSON.stringify(themes));
      renderTheme();
    }
  });
});
