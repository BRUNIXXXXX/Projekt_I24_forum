// Fetch and display comments from the server
document.addEventListener('DOMContentLoaded', loadComments);

const postForm = document.getElementById('postForm');
const postContainer = document.getElementById('postContainer');

// Load comments
function loadComments() {
    fetch('/api/comments/')
        .then(response => response.json())
        .then(data => {
            postContainer.innerHTML = '';
            data.comments.forEach(addCommentToDOM);
        });
}

// Add a comment to the DOM
function addCommentToDOM(comment) {
    const postElement = document.createElement('div');
    postElement.classList.add('post');
    postElement.innerHTML = `
        <h3>${comment.topic}</h3>
        <p class="meta">By ${comment.username} on ${comment.date}</p>
        <p>${comment.message}</p>
    `;
    postContainer.prepend(postElement);
}

// Submit a new comment
postForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const topic = document.getElementById('topic').value.trim();
    const message = document.getElementById('message').value.trim();

    if (username && topic && message) {
        fetch('/api/comments/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ username, topic, message }),
        })
        .then(response => response.json())
        .then(data => {
            loadComments(); // Reload comments
            postForm.reset();
        });
    }
});

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
