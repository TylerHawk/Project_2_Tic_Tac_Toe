# Tic Tac Toe 
## Let's play in the terminal
### Project requirements
+ Create the game board
    * Create the 'true' slots in memory
    * Create a display board that updates itself
    * Determine slot accessibility method
+ Determine player turn cycle
  + Access player data, turn dependent
  + Turn must continue until valid entry is entered
+ Validate player input
  + Must be formated correctly
    + correct length and order
  + Can only include 1, 2, 3, and a, b, c
  + Board location must be free
  + Feedback must be provided to player
+ Record player slot locations
+ Catch winning play
  + Define all winning possibilities
  + Check if a winning pattern is in player slot locations
+ Determine game life cycle
  + What will end the game while loop
    + Draw event
    + Winning event

### Challenges during development

1. Game board did not update when printed.
   + Placed it in a function that returns the updated print.
2. Implementing turns.
   + Accessed appropriate player data by taking moduler of turn count.
3. Validating input format did not work as originally expected.
   + Using an 'OR AND OR' statement took trial and error and had to be dropped. 
   + By placing validators in lists and comparing player input with an 'IN AND IN' statement, successful validation was implemented.
4. While storing player inputs for winning validation, turn relationship between row and column was lost. 
   + Stored value example [ "1", "a", "2", "b", "3", "c" ]
   + Desired format to maintain relationships was a list of tuples.
   + Final outcome example [ ("1", "a"), ("2", "b"), ("3", "c") ]
5. When winning the game using the last available slot declared a winner while a draw. 
   + Since it was last turn, the draw statement was called.
   + By checking if end_game had already been toggled, the draw statement is skipped when a win occurs on the last turn.

### Game Example: Win
Here is an example of a win. Player input errors are also recorded.
  
          A | B | C
        1   |   |  
          ----------
        2   |   |  
          ----------
        3   |   |  
        
    Player 1: 'X'; Player 2: '0'
    To select the location on your turn, type its address as 'row''column'; for example: '1a' or '2b'
    Player 1, make your selection: 4b
    Choice is not valid.
    Player 1, make your selection: 1a
    
          A | B | C
        1 X |   |  
          ----------
        2   |   |  
          ----------
        3   |   |  
        
    Player 2, make your selection: b2
    Choice is not valid.
    Player 2, make your selection: 2b
    
          A | B | C
        1 X |   |  
          ----------
        2   | 0 |  
          ----------
        3   |   |  
        
    Player 1, make your selection: 2a
    
          A | B | C
        1 X |   |  
          ----------
        2 X | 0 |  
          ----------
        3   |   |  
        
    Player 2, make your selection: 3b
    
          A | B | C
        1 X |   |  
          ----------
        2 X | 0 |  
          ----------
        3   | 0 |  
        
    Player 1, make your selection: 3a
    
          A | B | C
        1 X |   |  
          ----------
        2 X | 0 |  
          ----------
        3 X | 0 |  
        
    Player 1, you are the winner!

### Game Example: Draw
Here game ends with a draw. Player input errors are also recorded.

          A | B | C
        1   |   |  
          ----------
        2   |   |  
          ----------
        3   |   |  
        
    Player 1: 'X'; Player 2: '0'
    To select the location on your turn, type its address as 'row''column'; for example: '1a' or '2b'
    Player 1, make your selection: 1a
    
          A | B | C
        1 X |   |  
          ----------
        2   |   |  
          ----------
        3   |   |  
        
    Player 2, make your selection: 2a
    
          A | B | C
        1 X |   |  
          ----------
        2 0 |   |  
          ----------
        3   |   |  
        
    Player 1, make your selection: 3a
    
          A | B | C
        1 X |   |  
          ----------
        2 0 |   |  
          ----------
        3 X |   |  
        
    Player 2, make your selection: 2a
    That slot has been taken.
    Player 2, make your selection: 2b
    
          A | B | C
        1 X |   |  
          ----------
        2 0 | 0 |  
          ----------
        3 X |   |  
        
    Player 1, make your selection: 2c
    
          A | B | C
        1 X |   |  
          ----------
        2 0 | 0 | X
          ----------
        3 X |   |  
        
    Player 2, make your selection: ba
    Choice is not valid.
    Player 2, make your selection: b2
    Choice is not valid.
    Player 2, make your selection: ab
    Choice is not valid.
    Player 2, make your selection: 1b
    
          A | B | C
        1 X | 0 |  
          ----------
        2 0 | 0 | X
          ----------
        3 X |   |  
        
    Player 1, make your selection: 3b
    
          A | B | C
        1 X | 0 |  
          ----------
        2 0 | 0 | X
          ----------
        3 X | X |  
        
    Player 2, make your selection: 3c
    
          A | B | C
        1 X | 0 |  
          ----------
        2 0 | 0 | X
          ----------
        3 X | X | 0
        
    Player 1, make your selection: 1c
    
          A | B | C
        1 X | 0 | X
          ----------
        2 0 | 0 | X
          ----------
        3 X | X | 0
        
    Game tied!
