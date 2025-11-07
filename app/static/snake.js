const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const TILE = 20;
let dir = [1, 0];

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowUp" && dir[1] !== 1) dir = [0, -1];
  if (e.key === "ArrowDown" && dir[1] !== -1) dir = [0, 1];
  if (e.key === "ArrowLeft" && dir[0] !== 1) dir = [-1, 0];
  if (e.key === "ArrowRight" && dir[0] !== -1) dir = [1, 0];
});

async function tick() {
  await fetch("/move", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ dir }),
  });

  const state = await fetch("/state").then((r) => r.json());
  draw(state);
}

function draw(state) {
  ctx.fillStyle = "#111";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "red";
  ctx.fillRect(state.food[0] * TILE, state.food[1] * TILE, TILE, TILE);

  ctx.fillStyle = "#4caf50";
  for (const [x, y] of state.snake) {
    ctx.fillRect(x * TILE, y * TILE, TILE, TILE);
  }

  ctx.fillStyle = "white";
  ctx.fillText(`Score: ${state.score}`, 10, 20);
}

setInterval(tick, 150);
