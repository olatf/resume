

// function myFunction() {
//   const x = document.getElementById("myLinks");
//   const y = document.getElementById("body");
//   const z = document.getElementById("class");
  
//   if (x.style.display === "block") {
//     x.style.display = "none";
//     y.style.filter = "blur(0px)";
//     z.style.overflow = "auto";
//   } else {
//     x.style.display = "block";
//     y.style.filter = "blur(2px)";
//     z.style.overflow = "hidden";
//     x.style.filter = "blur(0px)";
//   }

// }

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


function myFunction2() {
  const x = document.getElementById("myLinked");
  const y = document.getElementById("body");
  const z = document.getElementById("class");
  
  if (x.style.display === "block") {
    x.style.display = "none";
    y.style.filter = "blur(0px)";
    z.style.overflow = "auto";
  } else {
    x.style.display = "block";
    y.style.filter = "blur(2px)";
    x.style.filter = "blur(0px)";
  }

}

function toggleDarkMode() {
  var html = document.documentElement;
  html.classList.toggle("dark");
  console.log("Am clicked")
}


function updateClock() {
  var now = new Date();

  var hours = now.getHours();
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();

  // var time = hours + ":" + minutes + ":" + seconds;

  var clockElement = document.getElementById("clock");
  var clockElements = document.getElementById("clocks");
  var clockElemented = document.getElementById("clocked");
  clockElement.textContent = hours.toString().padStart(2, "0");
  clockElements.textContent = minutes.toString().padStart(2, "0");
  clockElemented.textContent = seconds.toString().padStart(2, "0");
    
  var dateElement = document.getElementById("date");
  dateElement.textContent = now.toDateString();
}

setInterval(updateClock, 1000); // Call updateClock every second (1000ms)

