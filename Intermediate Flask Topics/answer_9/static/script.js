document.addEventListener('DOMContentLoaded', function () {
    const createForm = document.getElementById('create-book-form');
    if (createForm) {
        createForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const data = {
                title: createForm.title.value,
                author: createForm.author.value,
                published_date: createForm.published_date.value,
                isbn: createForm.isbn.value
            };
            fetch('/api/books', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(book => {
                alert(`Book created: ${book.title}`);
                window.location.href = '/view';
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const updateForm = document.getElementById('update-book-form');
    if (updateForm) {
        updateForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const bookId = updateForm.getAttribute('data-book-id');
            const data = {
                title: updateForm.title.value,
                author: updateForm.author.value,
                published_date: updateForm.published_date.value,
                isbn: updateForm.isbn.value
            };
            fetch(`/api/books/${bookId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(book => {
                alert(`Book updated: ${book.title}`);
                window.location.href = '/view';
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const booksList = document.getElementById('books-list');
    if (booksList) {
        fetch('/api/books')
        .then(response => response.json())
        .then(books => {
            books.forEach(book => {
                const listItem = document.createElement('li');
                listItem.textContent = `${book.title} by ${book.author}`;
                booksList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error:', error));
    }
});
