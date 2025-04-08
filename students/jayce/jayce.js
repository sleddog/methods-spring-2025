window.onload = function () {
    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");

    const numBalls = 4;
    const balls = [];

    for (let i = 0; i < numBalls; i++) {
        balls.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            dx: (Math.random() - 0.5) * 4,
            dy: (Math.random() - 0.5) * 4,
            radius: 20,
            color: `hsl(${Math.random() * 360}, 70%, 60%)`
        });
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (let i = 0; i < balls.length; i++) {
            let b = balls[i];

            if (b.x + b.radius > canvas.width || b.x - b.radius < 0) b.dx = -b.dx;
            if (b.y + b.radius > canvas.height || b.y - b.radius < 0) b.dy = -b.dy;

            b.x += b.dx;
            b.y += b.dy;

            ctx.beginPath();
            ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
            ctx.fillStyle = b.color;
            ctx.fill();
            ctx.closePath();

            for (let j = i + 1; j < balls.length; j++) {
                let b2 = balls[j];
                let dx = b2.x - b.x;
                let dy = b2.y - b.y;
                let dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < b.radius + b2.radius) {
                    let tempDx = b.dx;
                    let tempDy = b.dy;
                    b.dx = b2.dx;
                    b.dy = b2.dy;
                    b2.dx = tempDx;
                    b2.dy = tempDy;

                    // Overlapping 

                    let overlap = (b.radius + b2.radius - dist) / 2;
                    let angle = Math.atan2(dy, dx);
                    b.x -= overlap * Math.cos(angle);
                    b.y -= overlap * Math.sin(angle);
                    b2.x += overlap * Math.cos(angle);
                    b2.y += overlap * Math.sin(angle);
                }
            }
        }

        requestAnimationFrame(draw);
    }

    draw();
};
