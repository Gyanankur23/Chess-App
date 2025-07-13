# pages/Interactive_Board.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="♟️ Interactive Chess Board", layout="centered")
st.title("♟️ ChessMaster Interactive Board")

# Embed chessboard.js via HTML
components.html("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ChessMaster Board</title>
  <style>
    body {
      background-color: #f0f0f0;
      text-align: center;
    }
    #board {
      width: 400px;
      margin: auto;
    }
  </style>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/css/chessboard.min.css" />
</head>
<body>
  <div id="board"></div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/js/chessboard.min.js"></script>
  <script>
    var board = null;
    var game = new Chess();

    function onDragStart (source, piece, position, orientation) {
      if (game.game_over()) return false;
      if (piece.search(/^b/) !== -1) return false; // Only allow white to move
    }

    function onDrop (source, target) {
      var move = game.move({
        from: source,
        to: target,
        promotion: 'q'
      });

      if (move === null) return 'snapback';

      window.setTimeout(makeRandomMove, 250);
    }

    function makeRandomMove () {
      var possibleMoves = game.moves();
      if (game.game_over()) return;

      var randomIdx = Math.floor(Math.random() * possibleMoves.length);
      game.move(possibleMoves[randomIdx]);
      board.position(game.fen());
    }

    function onSnapEnd () {
      board.position(game.fen());
    }

    var config = {
      draggable: true,
      position: 'start',
      onDragStart: onDragStart,
      onDrop: onDrop,
      onSnapEnd: onSnapEnd
    };
    board = Chessboard('board', config);
  </script>
</body>
</html>
""", height=500)
