document.addEventListener('DOMContentLoaded', function() {
    const cursor = document.createElement('div');
    cursor.classList.add('cursor');
    
    const cursorDot = document.createElement('div');
    cursorDot.classList.add('cursor-dot');
    
    document.body.appendChild(cursor);
    document.body.appendChild(cursorDot);
    
    let mouseX = 0;
    let mouseY = 0;
    
    let cursorX = 0;
    let cursorY = 0;
    
    document.addEventListener('mousemove', function(e) {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        cursorDot.style.left = mouseX + 'px';
        cursorDot.style.top = mouseY + 'px';
    });
    
    function animateCursor() {
        cursorX += (mouseX - cursorX) * 0.1;
        cursorY += (mouseY - cursorY) * 0.1;
        
        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';
        
        requestAnimationFrame(animateCursor);
    }
    
    animateCursor();
    
    const links = document.querySelectorAll('a');
    
    links.forEach(link => {
        link.addEventListener('mouseenter', () => {
            cursor.style.width = '30px';
            cursor.style.height = '30px';
            cursor.style.backgroundColor = 'rgba(142, 255, 142, 0.1)';
        });
        
        link.addEventListener('mouseleave', () => {
            cursor.style.width = '20px';
            cursor.style.height = '20px';
            cursor.style.backgroundColor = 'transparent';
        });
    });
    
    const headings = document.querySelectorAll('h1, h2, p, li');
    headings.forEach(heading => {
        heading.classList.add('terminal-text');
    });
    
    document.addEventListener('click', createGlitchEffect);
});

function createGlitchEffect() {
    const glitch = document.createElement('div');
    glitch.classList.add('glitch-effect');
    glitch.style.position = 'fixed';
    glitch.style.top = '0';
    glitch.style.left = '0';
    glitch.style.width = '100%';
    glitch.style.height = '100%';
    glitch.style.backgroundColor = 'rgba(142, 255, 142, 0.05)';
    glitch.style.pointerEvents = 'none';
    glitch.style.zIndex = '9';
    glitch.style.mixBlendMode = 'overlay';
    
    document.body.appendChild(glitch);
    
    for (let i = 0; i < 3; i++) {
        const line = document.createElement('div');
        line.style.position = 'absolute';
        line.style.left = '0';
        line.style.top = Math.random() * 100 + '%';
        line.style.width = '100%';
        line.style.height = (Math.random() * 3 + 1) + 'px';
        line.style.backgroundColor = '#8eff8e';
        line.style.opacity = Math.random() * 0.3 + 0.2;
	
        glitch.appendChild(line);
    }
    
    setTimeout(() => {
        glitch.style.opacity = '0';
        glitch.style.transition = 'opacity 0.3s';
        
        setTimeout(() => {
            document.body.removeChild(glitch);
        }, 300);
    }, 150);
}
