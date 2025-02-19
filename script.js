document.addEventListener("DOMContentLoaded", function () {
  if (
    !document.getElementById("rhyme") ||
    !document.getElementById("rhythm") ||
    !document.getElementById("quality") ||
    !document.getElementById("style") ||
    !document.getElementById("wealth") ||
    !document.getElementById("vibe") ||
    !document.getElementById("finalScore")
  ) {
    console.error(
      "Один или несколько элементов не найдены в DOM."
    );
    return;
  }

  document.querySelectorAll(".slider").forEach((slider) => {
    slider.addEventListener("input", function () {
      let value = this.value;
      this.parentElement.querySelector(
        ".ratingValue"
      ).textContent = value;
      calculateFinalScore();
    });
  });

  const imageInput = document.getElementById("track-image");
  const imagePreview =
    document.getElementById("image-preview");

  imageInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        imagePreview.innerHTML = `<img src="${e.target.result}" alt="Загруженное изображение">`;
      };
      reader.readAsDataURL(file);
    } else {
      imagePreview.innerHTML = "";
    }
  });

  function calculateFinalScore() {
    let quality =
      parseFloat(
        document.getElementById("quality").value
      ) || 0;
    let rhyme =
      parseFloat(document.getElementById("rhyme").value) ||
      0;
    let wealth =
      parseFloat(document.getElementById("wealth").value) ||
      0;
    let style =
      parseFloat(document.getElementById("style").value) ||
      0;
    let rhythm =
      parseFloat(document.getElementById("rhythm").value) ||
      0;
    let vibe =
      parseFloat(document.getElementById("vibe").value) ||
      1.0;

    function redefiningSmallValues(id) {
      if (4 < id <= 7) {
        id *= id * 1.2;
      } else if (7 < id <= 10) {
        id *= 1.39;
      }
      return id;
    }

    function redefiningLargeValues(id) {
      if (1 <= id < 5) {
        id *= id * 1.2;
      } else if (5 <= id < 7) {
        id *= 1.4;
      } else if (7 <= id <= 10) {
        id *= 1.6;
      }
      return id;
    }

    let weightedScore =
      redefiningLargeValues(style) +
      redefiningLargeValues(vibe) +
      redefiningSmallValues(rhythm) +
      redefiningSmallValues(rhyme) +
      redefiningSmallValues(wealth) +
      redefiningSmallValues(quality);

    weightedScore = Math.min(weightedScore, 100);

    document.getElementById("finalScore").textContent =
      Math.round(weightedScore);
  }

  calculateFinalScore();
});
