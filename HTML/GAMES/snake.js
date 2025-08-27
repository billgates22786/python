const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const box = 20;
const canvasSize = 400;
const rows = canvasSize / box;
const cols = canvasSize / box;

let snake;
let direction;
let food;
let score;
let gameLoop;
let isGameOver = false;

function init() {
  snake = [
    { x: 8, y: 10 },
    { x: 7, y: 10 },
    { x: 6, y: 10 }
  ];
  direction = 'RIGHT';
  score = 0;
  isGameOver = false;
  placeFood();
  document.getElementById('score').textContent = score;
}

function placeFood() {
  let valid = false;
  while (!valid) {
    food = {
      x: Math.floor(Math.random() * cols),
      y: Math.floor(Math.random() * rows)
    };
    valid = !snake.some(s => s.x === food.x && s.y === food.y);
  }
}

function drawSnake() {
  for (let i = 0; i < snake.length; i++) {
    // Gradient for body
    let gradient = ctx.createLinearGradient(
      snake[i].x*box, snake[i].y*box, (snake[i].x+1)*box, (snake[i].y+1)*box
    );
    gradient.addColorStop(0, i === 0 ? "#19e3a5" : "#3a8ee6");
    gradient.addColorStop(1, "#1e3c72");
    ctx.fillStyle = gradient;
    ctx.fillRect(snake[i].x*box, snake[i].y*box, box, box);

    // Border
    ctx.strokeStyle = "#fff";
    ctx.lineWidth = 2;
    ctx.strokeRect(snake[i].x*box, snake[i].y*box, box, box);
  }
}

function drawFood() {
  ctx.save();
  ctx.shadowColor = "#e94e77";
  ctx.shadowBlur = 16;
  ctx.fillStyle = "#e94e77";
  ctx.beginPath();
  ctx.arc(food.x*box + box/2, food.y*box + box/2, box/2.1, 0, 2 * Math.PI);
  ctx.fill();
  ctx.restore();
}

function moveSnake() {
  let head = { ...snake[0] };
  if (direction === 'LEFT') head.x--;
  else if (direction === 'RIGHT') head.x++;
  else if (direction === 'UP') head.y--;
  else if (direction === 'DOWN') head.y++;

  // Wall collision
  if (
    head.x < 0 || head.x >= cols ||
    head.y < 0 || head.y >= rows ||
    snake.some(s => s.x === head.x && s.y === head.y)
  ) {
    gameOver();
    return;
  }

  snake.unshift(head);

  // Food collision
  if (head.x === food.x && head.y === food.y) {
    score++;
    document.getElementById('score').textContent = score;
    placeFood();
  } else {
    snake.pop();
  }
}

function draw() {
  ctx.clearRect(0, 0, canvasSize, canvasSize);

  // Board background
  ctx.fillStyle = "#e0eafc";
  ctx.fillRect(0, 0, canvasSize, canvasSize);

  // Grid lines
  ctx.strokeStyle = "#cfdef3";
  ctx.lineWidth = 1;
  for (let i = 1; i < cols; i++) {
    ctx.beginPath();
    ctx.moveTo(i * box, 0);
    ctx.lineTo(i * box, canvasSize);
    ctx.stroke();
  }
  for (let i = 1; i < rows; i++) {
    ctx.beginPath();
    ctx.moveTo(0, i * box);
    ctx.lineTo(canvasSize, i * box);
    ctx.stroke();
  }

  drawFood();
  drawSnake();
}

function loop() {
  if (!isGameOver) {
    moveSnake();
    draw();
  }
}

function gameOver() {
  isGameOver = true;
  clearInterval(gameLoop);
  ctx.save();
  ctx.globalAlpha = 0.75;
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvasSize, canvasSize);
  ctx.globalAlpha = 1;
  ctx.font = "36px Segoe UI";
  ctx.fillStyle = "#fff";
  ctx.textAlign = "center";
  ctx.fillText("Game Over!", canvasSize/2, canvasSize/2 - 10);
  ctx.font = "20px Segoe UI";
  ctx.fillText("Score: " + score, canvasSize/2, canvasSize/2 + 30);
  ctx.restore();
}

document.addEventListener('keydown', e => {
  if (isGameOver) return;
  if (e.key === 'ArrowLeft' && direction !== 'RIGHT') direction = 'LEFT';
  if (e.key === 'ArrowUp' && direction !== 'DOWN') direction = 'UP';
  if (e.key === 'ArrowRight' && direction !== 'LEFT') direction = 'RIGHT';
  if (e.key === 'ArrowDown' && direction !== 'UP') direction = 'DOWN';
});

function restartGame() {
  clearInterval(gameLoop);
  init();
  draw();
  gameLoop = setInterval(loop, 100);
}

window.onload = function() {
  restartGame();
};