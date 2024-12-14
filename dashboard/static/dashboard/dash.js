const hamburgerMenu = document.querySelector('.hamburger-menu');
const sidebar = document.querySelector('.sidebar');

// Initially hide the sidebar
sidebar.style.display = '';

// Toggle the sidebar when the hamburger menu is clicked
hamburgerMenu.addEventListener('click', (event) => {
    // Prevent the click from propagating to the document
    event.stopPropagation();

    // Toggle the sidebar display
    if (sidebar.style.display === 'none') {
        sidebar.style.display = 'block';
    } else {
        sidebar.style.display = 'none';
    }
});

// Add a global click listener to close the sidebar
document.addEventListener('click', () => {
    if (sidebar.style.display === 'block') {
        sidebar.style.display = 'none';
    }
});

// Prevent the sidebar from closing when clicked
sidebar.addEventListener('click', (event) => {
    event.stopPropagation();
});

//darkmode
document.addEventListener('DOMContentLoaded', () => {
    const settingsIcon = document.getElementById('settings-icon');
    const allIcons = document.querySelectorAll('.bx');
    const sidebarLinks = document.querySelectorAll('.sidebar-link a, .sidebar-link i');
    const mainLinks = document.querySelectorAll('.main-links');
    const headers = document.querySelectorAll('.header');

    const savedTheme = localStorage.getItem('theme') || 'light';

    if (savedTheme === 'dark') {
        applyDarkMode(settingsIcon, allIcons, sidebarLinks, mainLinks, headers);
    } else {
        applyLightMode(settingsIcon, allIcons, sidebarLinks, mainLinks, headers);
    }
});

function myFunction() {
    const settingsIcon = document.getElementById('settings-icon');
    const allIcons = document.querySelectorAll('.bx');
    const sidebarLinks = document.querySelectorAll('.sidebar-link a, .sidebar-link i');
    const mainLinks = document.querySelectorAll('.main-links');
    const headers = document.querySelectorAll('.header');
    const currentTheme = localStorage.getItem('theme') || 'light';

    if (currentTheme === 'light') {
        applyDarkMode(settingsIcon, allIcons, sidebarLinks, mainLinks, headers);
        localStorage.setItem('theme', 'dark');
    } else {
        applyLightMode(settingsIcon, allIcons, sidebarLinks, mainLinks, headers);
        localStorage.setItem('theme', 'light');
    }
}

function applyDarkMode(settingsIcon, allIcons, sidebarLinks, mainLinks, headers) {
    settingsIcon.style.color = 'white';
    document.body.style.backgroundColor = 'black';
    document.body.style.color = 'white';

    allIcons.forEach(icon => {
        icon.style.color = 'white';
    });

    sidebarLinks.forEach(link => {
        link.style.color = 'white';
    });

    mainLinks.forEach(link => {
        link.style.color = 'white';
    });

    headers.forEach(header => {
        header.style.color = 'white';
        header.style.backgroundColor = 'black';
    });
}

function applyLightMode(settingsIcon, allIcons, sidebarLinks, mainLinks, headers) {
    settingsIcon.style.color = 'black';
    document.body.style.backgroundColor = 'white';
    document.body.style.color = 'black';

    allIcons.forEach(icon => {
        icon.style.color = 'black';
    });

    sidebarLinks.forEach(link => {
        link.style.color = 'black';
    });

    mainLinks.forEach(link => {
        link.style.color = 'black';
    });

    headers.forEach(header => {
        header.style.color = 'black';
        header.style.backgroundColor = 'white';
    });
}
