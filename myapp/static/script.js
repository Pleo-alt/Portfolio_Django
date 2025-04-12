// Ensure the modal is hidden when the page loads
const modal = document.getElementById('modal');
modal.style.display = 'none';

// Add event listeners to "View More" buttons
const openModalButtons = document.querySelectorAll('.view-more-btn');
openModalButtons.forEach((button) => {
    button.addEventListener('click', () => {
        // Hide all modal-skill elements first
        document.querySelectorAll('.modal-skill').forEach((modalSkill) => {
            modalSkill.style.display = 'none';
        });

        // Get the skill name from the button's parent span
        const skillName = button.parentElement.textContent.trim().split(' ')[0].toLowerCase();
        const modalSkill = document.getElementById(`${skillName}-modal`);

        // Show the modal and the corresponding modal-skill
        if (modalSkill) {
            modal.style.display = 'flex';
            modalSkill.style.display = 'block';
        }
    });
});

// Close the modal when the "Close" button is clicked
document.addEventListener('click', (event) => {
    if (event.target.classList.contains('closeModal')) {
        modal.style.display = 'none';
        document.querySelectorAll('.modal-skill').forEach((modalSkill) => {
            modalSkill.style.display = 'none';
        });
    }
});

// Close the modal when clicking outside the modal content
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
        document.querySelectorAll('.modal-skill').forEach((modalSkill) => {
            modalSkill.style.display = 'none';
        });
    }
});

//progress bar
document.addEventListener('DOMContentLoaded', function () {
    // Get all the progress bars
    const progressBars = document.querySelectorAll('.bars');
    
    progressBars.forEach(function(bar) {
        // Get the percentage value from the data-percentage attribute
        const percentage = bar.getAttribute('data-percentage');
        
        // Set the width of the progress bar's colored section
        setTimeout(function() {
            const colorBar = bar.querySelector('::before');
            bar.style.setProperty('--progress-width', percentage + '%'); // Use custom property to set width
        }, 100);  // Small delay to allow the page to render first
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const successMessage = document.getElementById('contactSuccessMessage');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const formData = new FormData(contactForm);

        fetch(contactForm.action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json()) // Assume response is JSON with success status
        .then(data => {
            if (data.success) {
                successMessage.style.display = 'block'; // Show success message
                contactForm.reset(); // Optionally reset the form
            } else {
                alert('There was an error sending your message.');
            }
        })
        .catch(error => {
            alert('There was an error sending your message.');
        });
    });
});

function toggleMenu() {
    const navList = document.querySelector('.nav_list');
    const isVisible = navList.getAttribute('data-visible') === 'true';
    navList.setAttribute('data-visible', !isVisible);
}