### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# def __init__(self,value):
# self.value = value


# The assignment operator is incorrect. Should be a comparison operator == . Currently would always return True.  
# Also a colon beyond the word else
  def check_for_ace(self, card):
    if card.value = 1: 
      return True
    else 
      return False
   
# Def not dif in addition to missing comma between card1 and card2.  Also first return card should be card1.  card is not a variable.  
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# line 37. Total cards not initialized before its use. total = 0 
# In the cards total method the return statement has a string concatination error.  Should return "You have a total of" + str(total)
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
