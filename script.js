document.addEventListener("DOMContentLoaded", function () {
  if (
    !document.getElementById("rhythm") ||
    !document.getElementById("rhyme") ||
    !document.getElementById("wealth") ||
    !document.getElementById("imagery") ||
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
    let rhythm = parseFloat(document.getElementById("rhythm").value) || 0;
    let rhyme = parseFloat(document.getElementById("rhyme").value) || 0;
    let wealth = parseFloat(document.getElementById("wealth").value) || 0;
    let imagery = parseFloat(document.getElementById("imagery").value) || 0;
    let charisma = parseFloat(document.getElementById("charisma").value) || 0;
    let vibe = parseFloat(document.getElementById("vibe").value) || 0;

    function getBaseCoefficient(value) {
      if (value >= 1 && value < 4) return 1;
      if (value >= 4 && value < 7) return 1.2;
      if (value >= 7 && value <= 10) return 1.39;
      return 1;
    }

    function getAdditionalCoefficient(value) {
      if (value >= 1 && value <= 5) return 1.2;
      if (value >= 5 && value <= 8) return 1.4;
      if (value >= 8 && value <= 10) return 1.6;
      return 1;
    }

    rhythm *= getBaseCoefficient(rhythm);
    rhyme *= getBaseCoefficient(rhyme);
    wealth *= getBaseCoefficient(wealth);
    imagery *= getBaseCoefficient(imagery);
    charisma *= getBaseCoefficient(charisma) * getAdditionalCoefficient(charisma);
    vibe *= getBaseCoefficient(vibe) * getAdditionalCoefficient(vibe);

    let weightedScore = rhythm + rhyme + wealth + imagery + charisma + vibe;

    let maxPossibleScore = (10 * getBaseCoefficient(10)) * 4 +
                           (10 * getBaseCoefficient(10) * getAdditionalCoefficient(10)) * 2;

    weightedScore = (weightedScore / maxPossibleScore) * 100;
    weightedScore = Math.min(weightedScore, 100);

    const finalScoreElement = document.getElementById("finalScore");
    finalScoreElement.textContent = Math.round(weightedScore);

    // Изменяем цвет текста на золотой, если оценка 100
    if (weightedScore === 100) {
      finalScoreElement.style.color = "#FFD700"; // Золотой
    } else {
      finalScoreElement.style.color = "#007BFF"; // Синий
    }
  }

  calculateFinalScore();
});
