// Функция для получения CSRF токена из cookie
function getCSRFToken() {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Ищем cookie с именем 'csrftoken'
      if (cookie.substring(0, 10) === "csrftoken=") {
        cookieValue = decodeURIComponent(
          cookie.substring(10)
        );
        break;
      }
    }
  }
  return cookieValue;
}

document
  .getElementById("post-Score")
  .addEventListener("click", () => {
    const csrftoken = getCSRFToken(); // Получаем токен

    const rating = {
      category: "final-score",
      value: document
        .getElementById("finalScore")
        .textContent.trim(),
    };

    fetch("/submit_rating/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken, // Используем полученный токен
      },
      body: JSON.stringify(rating),
    })
      .then((res) => {
        if (res.status === 403) {
          alert("Ошибка: отсутствует CSRF токен");
          throw new Error("CSRF token error");
        }
        return res.json();
      })
      .then((data) => {
        if (data.status != "success")
          alert(
            "Ошибка: " +
              (data.error || "Неизвестная ошибка")
          );
      });
    //.catch(() => alert("Ошибка сети"));
  });
