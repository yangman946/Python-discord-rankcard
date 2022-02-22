
from Rankcard import Main
  
rankcard = Main.RANKCARD()
card = rankcard.rank_card(
		    username="user", # user name
		    avatar= "https://external-preview.redd.it/4PE-nlL_PdMD5PrFNLnjurHQ1QKPnCvg368LTDnfM-M.png?auto=webp&s=ff4c3fbc1cce1a1856cff36b5d2a40a6d02cc1c3", 
		    level=1, # user level
		    rank=1, # user rank
		    current_xp=0, # user xp
		    custom_background= "#000000", # background colour
		    xp_color="#FF7A7A", # Foreground colour
		    next_level_xp=100) # Next level xp

