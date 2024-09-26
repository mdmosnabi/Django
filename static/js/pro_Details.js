document.getElementById('bar').addEventListener('click', function (event) {
    let a =event.target.classList.value
    if(a.includes('Specifications')){
        document.getElementById('speci').classList.remove('hidden');
        document.getElementById('Des').classList.add('hidden');
        document.getElementById('Review').classList.add('hidden');
        document.getElementById('Ownership').classList.add('hidden');
    }
    else if(a.includes('Description')){
        document.getElementById('Des').classList.remove('hidden');
        document.getElementById('speci').classList.add('hidden');
        document.getElementById('Review').classList.add('hidden');
        document.getElementById('Ownership').classList.add('hidden');
    }
    else if(a.includes('Review')){
        document.getElementById('Review').classList.remove('hidden');
        document.getElementById('Des').classList.add('hidden');
        document.getElementById('speci').classList.add('hidden');
        document.getElementById('Ownership').classList.add('hidden');
    }
    else if(a.includes('Ownership')){
        document.getElementById('Ownership').classList.remove('hidden');
        document.getElementById('Des').classList.add('hidden');
        document.getElementById('speci').classList.add('hidden');
        document.getElementById('Review').classList.add('hidden');
    }
    
    
});
document.getElementById('addReview').addEventListener('click',()=>{
    document.getElementById('form').classList.toggle('hidden')
})

function submitForm(formElement) {
    const formData = new FormData(formElement);
    
    // Extract the action URL and CSRF token
    const actionUrl = formElement.action;
    const csrfToken = formData.get('csrfmiddlewaretoken');
    
    // Create an XMLHttpRequest object
    const xhr = new XMLHttpRequest();
    xhr.open('POST', actionUrl, true);
    
    // Set the request header for CSRF token
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    
    // Set up a handler for when the request finishes
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            console.log(response);
            
            if (response.bool) {
                window.location.reload();
            } else {
                alert('message: ' + response.message);
            }
        } else {
            console.log('Request failed. Returned status of ' + xhr.status);
        }
    };

    // Send the request
    xhr.send(formData);
}


document.getElementById('abcd').addEventListener('submit', function(event) {
    event.preventDefault();
    submitForm(this)
});

