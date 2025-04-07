const toggle = document.getElementById('theme-toggle');
const typewriter = document.getElementById('typewriter');
const skills = ["Java", "JavaScript/TypeScript", "C#", "Python", "React", "TailwindCSS", "Git"];
const weatherApi = "https://api.open-meteo.com/v1/forecast?latitude=45.6797&longitude=-111.0386&current=temperature_2m&timezone=America%2FDenver&forecast_days=1&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch";

let i = 0;
let j = 0;

// Using an anonymous function to set the initial theme
// This function checks the local storage for the theme preference!
(function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
})();

// Theme Toggle Button
toggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

window.addEventListener("DOMContentLoaded", () => {
    const headshot = document.getElementById("headshot");
    requestAnimationFrame(() => {
        headshot.classList.remove("opacity-0", "-translate-x-10");
        headshot.classList.add("opacity-100", "translate-x-0");
    });
});


// Typewriter effect for Skills section
function type() {
    if (j < skills[i].length) {
        typewriter.textContent += skills[i][j];
        j++;
        setTimeout(type, 100);
    } else {
        setTimeout(() => {
            typewriter.textContent = '';
            i = (i + 1) % skills.length;
            j = 0;
            type();
        }, 1500);
    }
}

type();

// Fetch weather data and update the temperature display
fetch(weatherApi)
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        const temperature = data.current.temperature_2m;
        document.getElementById("temperature").textContent = `${temperature}°F`;
    })
    .catch(error => {
        console.error("Error fetching weather data:", error);
        document.getElementById("temperature").textContent = "Error loading temperature.";
    });