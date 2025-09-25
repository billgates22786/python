import streamlit as st
import random

# Inject CSS for square buttons
st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlock"] > div:first-child .element-container {
        width: 100%;
        padding-top: 100%;
        position: relative;
    }
    div[data-testid="stVerticalBlock"] > div:first-child .stButton {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3em;
        font-weight: bold;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .score-container {
        display: flex;
        justify-content: space-around;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        margin-bottom: 20px;
        background-color: #f0f2f6;
    }
    .score-box {
        text-align: center;
    }
    .score-label {
        font-size: 1.2em;
        font-weight: bold;
    }
    .score-value {
        font-size: 1.5em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def reset_game(full_reset=False):
    """
    Resets the game state.
    Args:
        full_reset (bool): If True, resets scores and player name.
    """
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None
    if full_reset:
        st.session_state.scores = {"X": 0, "O": 0}
        st.session_state.player_name = ""

def check_winner(board):
    """Checks for a winner on the board."""
    # Check rows, columns, and diagonals
    lines = (
        board[0], board[1], board[2],
        [board[i][0] for i in range(3)],
        [board[i][1] for i in range(3)],
        [board[i][2] for i in range(3)],
        [board[i][i] for i in range(3)],
        [board[i][2-i] for i in range(3)],
    )
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != "":
            return line[0]
    # Check for a draw
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    return None

def ai_move(board):
    """Implements a simple AI for the computer opponent."""
    # 1. Check if AI can win in the next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                if check_winner(board) == "O":
                    return
                board[i][j] = ""

    # 2. Block the human player if they can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                if check_winner(board) == "X":
                    board[i][j] = "O"
                    return
                board[i][j] = ""

    # 3. Take the center square
    if board[1][1] == "":
        board[1][1] = "O"
        return

    # 4. Take a corner square
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for r, c in corners:
        if board[r][c] == "":
            board[r][c] = "O"
            return

    # 5. Take any available side square
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(sides)
    for r, c in sides:
        if board[r][c] == "":
            board[r][c] = "O"
            return

def handle_click(row, col):
    """Handles a player's move and the AI's response."""
    if not st.session_state.game_over and st.session_state.board[row][col] == "":
        st.session_state.board[row][col] = st.session_state.current_player
        
        # Check for a winner after the human player's move
        winner = check_winner(st.session_state.board)
        if winner:
            if winner != "Draw":
                st.session_state.scores[winner] += 1
            st.session_state.game_over = True
            st.session_state.winner = winner
        else:
            st.session_state.current_player = "O"
            # If AI mode is enabled, let the AI make a move
            if st.session_state.game_mode == "AI" and not st.session_state.game_over:
                ai_move(st.session_state.board)
                ai_winner = check_winner(st.session_state.board)
                if ai_winner:
                    if ai_winner != "Draw":
                        st.session_state.scores[ai_winner] += 1
                    st.session_state.game_over = True
                    st.session_state.winner = ai_winner
                st.session_state.current_player = "X"


def main():
    st.title("Tic-Tac-Toe")
    st.markdown('<p class="main-header">Welcome to Tic-Tac-Toe!</p>', unsafe_allow_html=True)
    
    # Initialize session state variables if they don't exist
    if 'player_name' not in st.session_state:
        st.session_state.player_name = ""
    if 'scores' not in st.session_state:
        st.session_state.scores = {"X": 0, "O": 0}
    if 'game_mode' not in st.session_state:
        st.session_state.game_mode = "Human vs Human"
        
    # Get user's name
    if st.session_state.player_name == "":
        name = st.text_input("Please enter your name:", key="name_input")
        if name:
            st.session_state.player_name = name
    else:
        st.write(f"Hello, {st.session_state.player_name}!")
        
        # Game Mode selection
        st.session_state.game_mode = st.selectbox(
            "Select Game Mode:",
            ("Human vs Human", "Human vs AI"),
            on_change=reset_game
        )
        
        # Display score dashboard
        st.markdown('<div class="score-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="score-box"><p class="score-label">{st.session_state.player_name} (X)</p><p class="score-value">{st.session_state.scores["X"]}</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="score-box"><p class="score-label">Draws</p><p class="score-value">{st.session_state.scores["Draws"] if "Draws" in st.session_state.scores else 0}</p></div>', unsafe_allow_html=True)
        with col3:
            opponent_name = "Computer" if st.session_state.game_mode == "Human vs AI" else "Player 2"
            st.markdown(f'<div class="score-box"><p class="score-label">{opponent_name} (O)</p><p class="score-value">{st.session_state.scores["O"]}</p></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if 'board' not in st.session_state:
            reset_game()
        
        # Display game status
        if st.session_state.game_over:
            if st.session_state.winner == "Draw":
                st.subheader("It's a draw!")
            else:
                winner_name = st.session_state.player_name if st.session_state.winner == "X" else opponent_name
                st.subheader(f"Player '{winner_name}' wins!")
                st.balloons()
        else:
            current_player_name = st.session_state.player_name if st.session_state.current_player == "X" else opponent_name
            st.subheader(f"Current Player: '{current_player_name}'")

        # Display the board using columns
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                button_label = st.session_state.board[i][j] if st.session_state.board[i][j] else " "
                cols[j].button(
                    button_label,
                    key=f"cell_{i}_{j}",
                    on_click=handle_click,
                    args=(i, j),
                    disabled=st.session_state.board[i][j] != "" or st.session_state.game_over,
                    use_container_width=False
                )

        # Play again button
        if st.session_state.game_over:
            if st.button("Play Again?"):
                reset_game()
        
        # Reset scores button
        if st.button("Reset Scores"):
            st.session_state.scores = {"X": 0, "O": 0}
            reset_game()

if __name__ == "__main__":
    main()
