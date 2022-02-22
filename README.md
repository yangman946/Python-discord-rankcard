# Python-discord-rankcard

![img](https://github.com/yangman946/Python-discord-rankcard/blob/main/Rankcard/pics/out.jpg)

## Installation

`pip install Python-discord-rankcard`

## Usage
```
  import discord
  from discord.ext import commands
  from Rankcard import Main
  
  class Rank(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.rankcard = Main.RANKCARD()
      
	@commands.command()
	async def rank(self, ctx):
		card = self.rankcard.rank_card(
				    username=ctx.author.name, # user name
				    avatar= ctx.author.avatar_url, 
				    level=1, # user level
				    rank=1, # user rank
				    current_xp=0, # user xp
				    custom_background= "#000000", # background colour
				    xp_color="#FF7A7A", # Foreground colour
				    next_level_xp=100) # Next level xp
		file = discord.File(card)
		await ctx.send(file=file)
        
  def setup(bot):
    	bot.add_cog(Rank(bot))
          


```



