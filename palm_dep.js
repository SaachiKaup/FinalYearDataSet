var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "prompt": {
    "text": "eval(\' Enter a some equation \')  \nGive a recommendation for making this code more secure: Give me the most important 3 points to secure this code. Answer in three sentences only, and be specific"
  }
});
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};
fetch("https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key=AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA", requestOptions)
  .then(response => response.text())
  .then(result => {
    console.log(result)
  })