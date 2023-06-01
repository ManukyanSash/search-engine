const textArea = document.getElementById('search-input')
const sendButton = document.getElementById('submit-button');
const list = document.getElementById('auto');
let res = document.getElementById('search-results');

sendButton.addEventListener('click', function(event) {
  event.preventDefault();

  const text = textArea.value;
  const data = { content: text };
  const jsonData = JSON.stringify(data);
  
  fetch('http://localhost:8080/templates', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: jsonData
})
.then(response => {
  if (response.status === 200) {
    return response.json();
  } else {
    throw new Error('Invalid response');
  }
})
.then(data => {
  const myDiv = document.getElementById('search-results-div');
  for(let i = 0; i < data.length; ++i){
    const newP = document.createElement('p');
    const newA = document.createElement('a');
    newA.textContent = data[i];
    newA.href = data[i];
    newP.appendChild(newA)
    myDiv.appendChild(newP);
  }
})
.catch(error => {
  console.error('Error:', error);
});
});

textArea.addEventListener('input', function(event) {
  var typedValue = event.target.value;
  const data = { content: typedValue };
  const jsonData = JSON.stringify(data);

  fetch('http://localhost:8080/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: jsonData
  })
  .then(response => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error('Invalid response');
    }
  })
  .then(data => {
    const opt = document.createElement('option');
    opt.value = data[1];
    auto.appendChild(opt);
  })
});