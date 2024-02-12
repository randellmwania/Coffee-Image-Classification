document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    fetch("/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        const imageContainer = document.getElementById("imageContainer");
        const predictionDiv = document.getElementById("prediction");
        const recommendationDiv = document.getElementById("recommendation");

        // Clear previous results
        imageContainer.innerHTML = "";
        predictionDiv.innerHTML = "";
        recommendationDiv.innerHTML = "";

        // Display uploaded image
        const img = document.createElement("img");
        img.src = URL.createObjectURL(file);
        img.alt = "Uploaded Image";
        imageContainer.appendChild(img);

        // Display prediction result
        predictionDiv.textContent = "Prediction: " + data.prediction;

        // Display recommendation
        if (data.recommendation) {
          recommendationDiv.textContent = "Recommendation:";
          const causeParagraph = document.createElement("p");
          causeParagraph.textContent = "Cause: " + data.recommendation.cause;
          recommendationDiv.appendChild(causeParagraph);

          const cureParagraph = document.createElement("p");
          cureParagraph.textContent = "Cure: " + data.recommendation.cure;
          recommendationDiv.appendChild(cureParagraph);

          if (data.recommendation["Learn More"]) {
            const learnMoreButton = document.createElement("button");
            learnMoreButton.textContent = "Learn More";
            learnMoreButton.classList.add("learn-more-button"); // Add button style
            learnMoreButton.addEventListener("click", function () {
              window.open(data.recommendation["Learn More"], "_blank");
            });
            recommendationDiv.appendChild(learnMoreButton);
          } else {
            recommendationDiv.textContent = "No recommendation available.";
          }

          // Add additional spacing for better readability
          recommendationDiv.appendChild(document.createElement("br"));
          recommendationDiv.appendChild(document.createElement("hr"));
        } else {
          recommendationDiv.textContent = "No recommendation available.";
        }
      })
      .catch((error) => console.error("Error:", error));
  });
