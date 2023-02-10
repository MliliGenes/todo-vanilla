window.addEventListener("load", () => {
  const input = document.querySelector("#input");
  const submit = document.querySelector("#submit");
  const taskslist = document.querySelector("#taskslist");
  const title = document.querySelector("h1");
  const clear = document.querySelector(".clear");

  ischecked = true;
  var isdit = false;

  var database = JSON.parse(localStorage.getItem("tasks")) || {};

  submit.addEventListener("click", (e) => {
    e.preventDefault();
    let newtask = input.value.trim();
    if (!newtask) {
      alert("please fill up the input!");
      return;
    }
    let id = new Date();
    database[id.getTime()] = { task: newtask, state: false };
    input.value = "";
    localStorage.setItem("tasks", JSON.stringify(database));

    renderTasks();
    mainExist();
    taskCount();
    cleardata();
  });
  renderTasks();
  mainExist();
  taskCount();
  cleardata();

  function mainExist() {
    if (Object.keys(database).length !== 0) {
      taskslist.classList.add("dn");
    } else if (Object.keys(database).length === 0) {
      taskslist.classList.remove("dn");
      clear.classList.remove("dn");
    }
  }
  function cleardata() {
    if (Object.keys(database).length > 1) {
      clear.classList.add("showclear");
    } else {
      clear.classList.remove("showclear");
    }
  }
  function taskCount() {
    if (Object.keys(database).length > 0) {
      title.setAttribute("data-count", Object.keys(database).length);
    } else {
      title.setAttribute("data-count", 0);
    }
  }

  function renderTasks() {
    console.log;
    taskslist.innerHTML = "";
    for (let item of Object.entries(database)) {
      let date = new Date(item[0] * 1);
      let humanForm = date.toLocaleString().replace(", ", " ");
      let template = `
        <div class="checkbox"></div>
        <input type="text" value="${item[1].task}" id="${item[0]}" data-set="${item[1].state}" readonly class="task-text" />
        <i class="bi bi-pencil-square"></i>
        <i class="bi bi-trash-fill"></i>
      `;
      const div = document.createElement("div");
      div.classList.add("task");
      div.setAttribute("data-date", humanForm);
      div.innerHTML = template;
      taskslist.appendChild(div);
    }
    const allTasks = document.querySelectorAll(".task-text");
    allTasks.forEach((oneTask) => {
      if (oneTask.getAttribute("data-set") == "true") {
        oneTask.previousElementSibling.classList.add("checked");
        oneTask.classList.add("checkedtask");
        ischecked = false;
      } else {
        oneTask.previousElementSibling.classList.remove("checked");
        oneTask.classList.remove("checkedtask");
        ischecked = true;
      }
    });
  }
  clear.addEventListener("click", (e) => {
    if (isdit) {
      return;
    }
    if (
      e.target.classList.contains("cleartxt") ||
      e.target.classList.contains("clear")
    ) {
      const clearTasks = document.querySelectorAll(".task");
      for (let task of clearTasks) {
        let id = task.firstElementChild.nextElementSibling.getAttribute("id");
        task.classList.add("delet");
        setTimeout(function () {
          taskslist.removeChild(task);
          let newdatabase = {};
          database = newdatabase;
          localStorage.setItem("tasks", JSON.stringify(database));
          cleardata();
          mainExist();
          taskCount();
        }, 300);
      }
    }
  });
  taskslist.addEventListener("click", (e) => {
    let target = e.target;
    if (target.classList.contains("bi-pencil-square")) {
      if (!ischecked) {
        return;
      }
      target.classList.remove("bi-pencil-square");
      target.classList.add("bi-check-lg");
      target.classList.add("edit");
      let task = target.previousElementSibling;
      tmp = task.value;
      task.removeAttribute("readonly");
      task.classList.add("edit");
      task.focus();
      task.setSelectionRange(task.value.length, task.value.length);
      isdit = true;
    } else if (target.classList.contains("bi-check-lg") || e.keyCode == 13) {
      target.classList.add("bi-pencil-square");
      target.classList.remove("bi-check-lg");
      target.classList.remove("edit");
      let task = target.previousElementSibling;
      if (!task.value) {
        task.value = tmp;
      }
      task.setAttribute("readonly", "readonly");
      task.classList.remove("edit");
      task.value = task.value.trim();
      isdit = false;
      if (task.value != tmp) {
        let id = target.previousElementSibling.getAttribute("id");
        let newdatabase = {};
        for (let item of Object.entries(database)) {
          if (item[0] == id) {
            let newid = new Date();
            newdatabase[newid.getTime()] = {
              task: task.value,
              state: item[1].state,
            };
          } else {
            newdatabase[item[0]] = { task: item[1].task, state: item[1].state };
          }
        }
        database = newdatabase;
        localStorage.setItem("tasks", JSON.stringify(database));
        renderTasks();
        cleardata();
      }
    }

    if (target.classList.contains("bi-trash-fill")) {
      let task = target.parentElement;
      let id =
        target.previousElementSibling.previousElementSibling.getAttribute("id");
      task.classList.add("delet");
      setTimeout(function () {
        taskslist.removeChild(task);
        let newdatabase = {};
        for (let item of Object.entries(database)) {
          if (item[0] == id) {
            continue;
          }
          newdatabase[item[0]] = { task: item[1].task, state: item[1].state };
        }
        database = newdatabase;
        localStorage.setItem("tasks", JSON.stringify(database));
        taskCount();
        mainExist();
        cleardata();
      }, 250);
    }

    if (target.classList.contains("checkbox")) {
      if (isdit) {
        return;
      }
      if (!target.classList.contains("checked")) {
        let id = target.nextElementSibling.getAttribute("id");
        let newdatabase = {};
        for (let item of Object.entries(database)) {
          if (item[0] == id) {
            newdatabase[item[0]] = { task: item[1].task, state: true };
          } else {
            newdatabase[item[0]] = { task: item[1].task, state: item[1].state };
          }
        }
        database = newdatabase;
        localStorage.setItem("tasks", JSON.stringify(database));
        renderTasks();
      } else {
        let id = target.nextElementSibling.getAttribute("id");
        let newdatabase = {};
        for (let item of Object.entries(database)) {
          if (item[0] == id) {
            newdatabase[item[0]] = { task: item[1].task, state: false };
          } else {
            newdatabase[item[0]] = { task: item[1].task, state: item[1].state };
          }
        }
        database = newdatabase;
        localStorage.setItem("tasks", JSON.stringify(database));
        renderTasks();
      }
    }
  });
});
