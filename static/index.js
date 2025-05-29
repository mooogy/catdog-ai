const uploadBox = document.getElementById("upload-box")
const fileInput = document.getElementById("file-upload")
const submitButton = document.getElementById("submit-button")
const resetButton = document.getElementById("reset-button")
const previewImage = document.getElementById("preview-image")
const addPhotoIcon = document.getElementById("add-photo-icon")
const section1Text = document.getElementById("section-1-text")
const results = document.getElementById("results")
const resultsLink = document.getElementById("results-link")

const prediction = document.getElementById("prediction")
const probCat = document.getElementById("probs-cat")
const probDog = document.getElementById("probs-dog")

var resultsReady = false

function toggleResults() {
  if (resultsReady) {
    results.style.display = "block";
    submitButton.setAttribute("disabled", "disabled")
    resetButton.removeAttribute("disabled")

    uploadBox.style.pointerEvents = "none";
    uploadBox.style.opacity = "0.5";
    resultsLink.click()
  } else {
    results.style.display = "none";
  }
}

function loadResults(label, probs, plot) {

  const catProb = (probs.cat * 100).toFixed(2);
  const dogProb = (probs.dog * 100).toFixed(2);

  prediction.textContent = label;
  probCat.textContent = `Cat: ${catProb}%`;
  probDog.textContent = `Dog: ${dogProb}%`;


  const plotData = JSON.parse(plot)
  const config = {
    responsive: true,
    staticPlot: true
  }

  Plotly.react("plot-container", plotData.data, plotData.layout, config);
  resultsReady = true
}

window.addEventListener("DOMContentLoaded", () => {
  fileInput.value = ""
  submitButton.setAttribute("disabled", "disabled");
})

uploadBox.addEventListener("click", () => {
  fileInput.click()
})

const observer = new MutationObserver(function (mutations) {
  window.dispatchEvent(new Event('resize'));
});

const child = document.getElementById('plot-container');
observer.observe(child, {
  attributes: true
})

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  document.getElementById("upload-error").style.visibility = "hidden";
  if (!file) {
    submitButton.setAttribute("disabled", "disabled")
    return
  };

  const reader = new FileReader();

  reader.onload = () => {
    console.log(addPhotoIcon)
    addPhotoIcon.style.display = "none"
    previewImage.src = reader.result;
    previewImage.style.display = "block"; // In case it was hidden by default
  };

  reader.readAsDataURL(file); // Convert file to base64 for preview
  submitButton.removeAttribute("disabled")

})

async function getModelResponse() {
  const file = fileInput.files[0]
  if (!file) {
    console.log("No file to upload")
    return
  }

  const formData = new FormData()
  formData.append("file", file)

  try {
    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData
    })

    const data = await res.json()
    console.log(data)
    loadResults(data.label, data.probs, data.plot)
    toggleResults()
  } catch (e) {
    const errorText = document.getElementById("upload-error");
    errorText.textContent = "Error: Could not read image. Please upload a valid JPG or PNG.";
    errorText.style.visibility = "visible";
    console.error(e)
  }



}

function resetApp() {

  results.style.display = "none";
  uploadBox.style.pointerEvents = "auto";
  uploadBox.style.opacity = "1";

  previewImage.src = "";
  previewImage.style.display = "none";
  addPhotoIcon.style.display = "block";

  fileInput.value = "";


  submitButton.setAttribute("disabled", "disabled");
  resetButton.setAttribute("disabled", "disabled");


  prediction.textContent = "Label";
  probCat.textContent = "Cat: --%";
  probDog.textContent = "Dog: --%";


  resultsReady = false;
}

submitButton.addEventListener("click", getModelResponse)
resetButton.addEventListener("click", resetApp)