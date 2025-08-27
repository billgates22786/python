const boardElem = document.getElementById('memory-board');
const statusElem = document.getElementById('memory-status');

let cardValues, cards, firstCard, secondCard, lockBoard, matches;

function init() {
  let icons = ['🍎','🍌','🍇','🍑','🍉','🍋','🍒','🥝'];
  cardValues = [...icons, ...icons];
  cardValues.sort(() => Math.random() - 0.5);
  cards = [];
  lockBoard = false;
  matches = 0;
  render();
  statusElem.textContent = "Find all pairs!";
}

function render() {
  boardElem.innerHTML = '';
  for (let i = 0; i < cardValues.length; i++) {
    const cardElem = document.createElement('div');
    cardElem.className = 'memory-card';
    cardElem.dataset.index = i;
    cardElem.onclick = () => flipCard(cardElem, i);
    cards.push({elem: cardElem, value: cardValues[i], flipped: false, matched: false});
    boardElem.appendChild(cardElem);
  }
}

function flipCard(cardElem, idx) {
  if (lockBoard) return;
  let card = cards[idx];
  if (card.flipped || card.matched) return;

  card.flipped = true;
  cardElem.classList.add('flipped');
  cardElem.textContent = card.value;

  if (!firstCard) {
    firstCard = card;
    return;
  }
  secondCard = card;
  lockBoard = true;

  if (firstCard.value === secondCard.value) {
    firstCard.matched = true;
    secondCard.matched = true;
    firstCard.elem.classList.add('matched');
    secondCard.elem.classList.add('matched');
    matches++;
    statusElem.textContent = "Pairs found: " + matches;
    resetTurn();
    if (matches === cardValues.length / 2) {
      statusElem.textContent = "You Win!";
    }
  } else {
    setTimeout(() => {
      firstCard.flipped = false;
      secondCard.flipped = false;
      firstCard.elem.classList.remove('flipped');
      secondCard.elem.classList.remove('flipped');
      firstCard.elem.textContent = '';
      secondCard.elem.textContent = '';
      resetTurn();
    }, 900);
  }
}

function resetTurn() {
  [firstCard, secondCard] = [null, null];
  lockBoard = false;
}

function restartGame() {
  [firstCard, secondCard] = [null, null];
  init();
}

window.onload = init;