const boardElem = document.getElementById('board');
const statusElem = document.getElementById('status');
let board, currentPlayer, gameOver;

function init() {
  board = ['', '', '', '', '', '', '', '', ''];
  currentPlayer = 'X';
  gameOver = false;
  render();
  statusElem.textContent = "Current Turn: " + currentPlayer;
}

function render() {
  boardElem.innerHTML = '';
  board.forEach((cell, i) => {
    const cellElem = document.createElement('div');
    cellElem.className = 'cell';
    cellElem.textContent = cell;
    cellElem.onclick = () => makeMove(i);
    boardElem.appendChild(cellElem);
  });
}

function makeMove(i) {
  if (gameOver || board[i]) return;
  board[i] = currentPlayer;
  render();
  if (checkWin(currentPlayer)) {
    statusElem.textContent = currentPlayer + " Wins!";
    gameOver = true;
  } else if (board.every(cell => cell)) {
    statusElem.textContent = "Draw!";
    gameOver = true;
  } else {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    statusElem.textContent = "Current Turn: " + currentPlayer;
  }
}

function checkWin(player) {
  const wins = [
    [0,1,2],[3,4,5],[6,7,8], // rows
    [0,3,6],[1,4,7],[2,5,8], // cols
    [0,4,8],[2,4,6]          // diags
  ];
  return wins.some(indices =>
    indices.every(idx => board[idx] === player)
  );
}

function restartGame() {
  init();
}

window.onload = init;