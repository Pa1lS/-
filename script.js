document.addEventListener("DOMContentLoaded", function () {
  if (
    !document.getElementById("rhyme") ||
    !document.getElementById("structure") ||
    !document.getElementById("style") ||
    !document.getElementById("charisma") ||
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
    let rhyme =
      parseFloat(document.getElementById("rhyme").value) ||
      0;
    let structure =
      parseFloat(
        document.getElementById("structure").value
      ) || 0;
    let style =
      parseFloat(document.getElementById("style").value) ||
      0;
    let charisma =
      parseFloat(
        document.getElementById("charisma").value
      ) || 0;
    let vibe =
      parseFloat(document.getElementById("vibe").value) ||
      1.0;

    let baseScore =
      (rhyme + structure + style + charisma) * 1.4;
    let vibeMultiplier = 1.0558 ** (vibe - 1);
    let weightedScore = baseScore * vibeMultiplier;

    weightedScore = Math.min(weightedScore, 90);

    document.getElementById("finalScore").textContent =
      Math.round(weightedScore);
  }

  calculateFinalScore();
});
