const state = {
    keydown: false,
    mouseX: 0,
    mouseY: 0,
    clickPostions: [],
    clickCount: 0,
}

const clickContainer = document.querySelector('.click-container');

document.addEventListener('keydown', keydownHandler);
function keydownHandler(event) {
    if (state.keydown) return;
    state.keydown = true
}

document.addEventListener('keyup', keyupHandler);
function keyupHandler(event) {
    state.keydown = false;
}

document.addEventListener('click', clickHandler);
function clickHandler(event) {
    const x = event.clientX;
    const y = event.clientY;
    state.clickPostions.push({ x, y });
    state.clickCount++;
}

document.onmousemove = function(event) {
    const x = event.clientX;
    const y = event.clientY;
    state.mouseX = x;
    state.mouseY = y;
    if (state.keydown) {
        state.clickPostions.push({ x, y });
        state.clickCount++;
        renderClicks();
    }
}

document.addEventListener('click', clickHandler);
function clickHandler(event) {
    const x = event.clientX;
    const y = event.clientY;
    state.clickPostions.push({ x, y });
    state.clickCount++;
    renderClicks();
}

function renderClicks() {
    clickContainer.innerHTML = '';
    state.clickPostions.forEach((pos, index) => {
        const clickElement = document.createElement('div');
        clickElement.className = 'click';
        clickElement.style.left = `${pos.x -10}px`;
        clickElement.style.top = `${pos.y - 10}px`;
        clickElement.style.backgroundColor = indexToColor(index);
        clickContainer.appendChild(clickElement);
    });
}

function indexToColor(num) {
    const colors = [
        '#f0a940', '#e1be31', '#d2d322', '#b6ec39', '#aaef60', '#9ef287', '#91f5ad', '#addd96', '#c8c47e', '#ff934f','#f0a940','#e19165','#d1798a','#c161af','#b149d4','#c55cb3','#d86e92','#ec8171'
    ];
    return colors[num % colors.length];
}