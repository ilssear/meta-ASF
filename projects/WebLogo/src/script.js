document.addEventListener('DOMContentLoaded', () => {
    const logoCode = document.getElementById('logoCode');
    const logoCanvas = document.getElementById('logoCanvas');
    const ctx = logoCanvas.getContext('2d');
    const runButton = document.getElementById('run');
    const resetButton = document.getElementById('reset');
    const loadButton = document.getElementById('load');
    const saveButton = document.getElementById('save');
    const clearCanvasButton = document.getElementById('clearCanvas');

    // Set canvas dimensions
    logoCanvas.width = 400;
    logoCanvas.height = 400;

    let turtle = { x: 0, y: 0, angle: 0, penDown: true, visible: true };

    function resetTurtle() {
        ctx.clearRect(0, 0, logoCanvas.width, logoCanvas.height);
        ctx.beginPath();
        turtle = { x: logoCanvas.width / 2, y: logoCanvas.height / 2, angle: 0, penDown: true, visible: true };
        ctx.moveTo(turtle.x, turtle.y);
    }

    function executeLogoCode() {
        const code = logoCode.value;
        const commands = code.split('\n');
        let i = 0;
        while (i < commands.length) {
            const command = commands[i].trim();
            const parts = command.split(' ');
            const cmd = parts[0].toLowerCase();
            const value = parseFloat(parts[1]);

            switch (cmd) {
                case 'fd':
                    turtle.x += value * Math.cos(turtle.angle);
                    turtle.y += value * Math.sin(turtle.angle);
                    if (turtle.penDown) {
                        ctx.lineTo(turtle.x, turtle.y);
                        ctx.stroke();
                    }
                    break;
                case 'bk':
                    turtle.x -= value * Math.cos(turtle.angle);
                    turtle.y -= value * Math.sin(turtle.angle);
                    if (turtle.penDown) {
                        ctx.lineTo(turtle.x, turtle.y);
                        ctx.stroke();
                    }
                    break;
                case 'rt':
                    turtle.angle += value * Math.PI / 180;
                    break;
                case 'lt':
                    turtle.angle -= value * Math.PI / 180;
                    break;
                case 'pu':
                    turtle.penDown = false;
                    break;
                case 'pd':
                    turtle.penDown = true;
                    break;
                case 'ht':
                    turtle.visible = false;
                    break;
                case 'st':
                    turtle.visible = true;
                    break;
                case 'home':
                    turtle.x = logoCanvas.width / 2;
                    turtle.y = logoCanvas.height / 2;
                    turtle.angle = 0;
                    break;
                case 'repeat':
                    const repeatCount = parseInt(value);
                    const repeatCommands = [];
                    i++;
                    while (i < commands.length && commands[i].trim() !== 'end') {
                        repeatCommands.push(commands[i]);
                        i++;
                    }
                    for (let j = 0; j < repeatCount; j++) {
                        repeatCommands.forEach(repeatCmd => {
                            const repeatParts = repeatCmd.trim().split(' ');
                            const repeatCmdName = repeatParts[0].toLowerCase();
                            const repeatValue = parseFloat(repeatParts[1]);
                            switch (repeatCmdName) {
                                case 'fd':
                                    turtle.x += repeatValue * Math.cos(turtle.angle);
                                    turtle.y += repeatValue * Math.sin(turtle.angle);
                                    if (turtle.penDown) {
                                        ctx.lineTo(turtle.x, turtle.y);
                                        ctx.stroke();
                                    }
                                    break;
                                case 'bk':
                                    turtle.x -= repeatValue * Math.cos(turtle.angle);
                                    turtle.y -= repeatValue * Math.sin(turtle.angle);
                                    if (turtle.penDown) {
                                        ctx.lineTo(turtle.x, turtle.y);
                                        ctx.stroke();
                                    }
                                    break;
                                case 'rt':
                                    turtle.angle += repeatValue * Math.PI / 180;
                                    break;
                                case 'lt':
                                    turtle.angle -= repeatValue * Math.PI / 180;
                                    break;
                                case 'pu':
                                    turtle.penDown = false;
                                    break;
                                case 'pd':
                                    turtle.penDown = true;
                                    break;
                                case 'ht':
                                    turtle.visible = false;
                                    break;
                                case 'st':
                                    turtle.visible = true;
                                    break;
                                case 'home':
                                    turtle.x = logoCanvas.width / 2;
                                    turtle.y = logoCanvas.height / 2;
                                    turtle.angle = 0;
                                    break;
                            }
                        });
                    }
                    break;
            }
            i++;
        }
    }

    runButton.addEventListener('click', () => {
        resetTurtle();
        executeLogoCode();
    });

    resetButton.addEventListener('click', () => {
        logoCode.value = '';
        resetTurtle();
    });

    loadButton.addEventListener('click', () => {
        const savedCode = localStorage.getItem('logoCode');
        if (savedCode) {
            logoCode.value = savedCode;
        }
    });

    saveButton.addEventListener('click', () => {
        localStorage.setItem('logoCode', logoCode.value);
    });

    clearCanvasButton.addEventListener('click', () => {
        resetTurtle();
    });
}); 