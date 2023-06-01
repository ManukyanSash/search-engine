const textArea = document.getElementById('search-input')
const sendButton = document.getElementById('submit-button');

sendButton.addEventListener('click', function(event) {
  event.preventDefault();

  const text = textArea.value;
  const data = { content: text };
  const jsonData = JSON.stringify(data);
  
  fetch('http://localhost:8080/admin', {
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
    console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});

});