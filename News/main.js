let url =
  "https://newsapi.org/v2/everything?q=apple&apiKey=dbc8a478776349d38e84e14244524b68";
let data = null;
let x = 0;
let lastClick = null;
function createNewsCards() {
  let containerDiv = document.getElementById("container");
  containerDiv.innerHTML = "";

  let card = document.createElement("div");
  card.classList.add("card");

  let heading = document.createElement("h1");
  var headingText = document.createTextNode(data[x].title);
  heading.appendChild(headingText);
  heading.classList.add("heading");

  let image = document.createElement("IMG");
  image.src = data[x].urlToImage;
  image.classList.add("image");
  image.align = "center";

  let description = document.createElement("p");
  var descriptionText = document.createTextNode(data[x].description);
  description.appendChild(descriptionText);
  description.classList.add("description");

  let readMoreButton = document.createElement("button");
  readMoreButton.innerHTML = "Read More";
  readMoreButton.classList.add("pure-material-button-contained");
  readMoreButton.onclick = function() {
    location.href = data[x].url;
  };

  card.appendChild(heading);
  card.appendChild(image);
  card.appendChild(description);
  card.appendChild(readMoreButton);

  containerDiv.appendChild(card);
}

var req = new XMLHttpRequest();
req.overrideMimeType("application/json");
req.open("GET", url, true);
req.onload = function() {
  var jsonResponse = JSON.parse(req.responseText);
  data = jsonResponse.articles;
  lastClick = new Date().getTime();
  createNewsCards();
};
req.send(null);

let timeDiff = {};
function addTimeToDict(x) {
    if(x in timeDiff)
        timeDiff[x] += (new Date().getTime() - lastClick);
    else
        timeDiff[x]=new Date().getTime() - lastClick;
    lastClick = new Date().getTime();
    console.log(timeDiff);
}

function keyTrigger(evt) {
  let keyCode = evt.keyCode;

  if (keyCode == 37) {
    if (x > 0) {
      addTimeToDict(x);
      --x;
      createNewsCards();
    }
  } else if (keyCode == 39) {
    if (x < data.length - 1) {
        addTimeToDict(x);
      x++;
      createNewsCards();
    }
  }
}

function touchAction(el, type) {

    if (type == "l")
      {
        if (x > 0) {
            addTimeToDict(x);
            --x;
            createNewsCards();
        }
      }
    else if (type == "r")
    {
        if (x < data.length - 1) {
            addTimeToDict(x);
          x++;
          createNewsCards();
        }
      }
  }
  
detectswipe("container",touchAction);