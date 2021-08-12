import discord

current_sundaymaple = """\
__**SUPERSTAR (v207)**__
> __1st Sunday: 15th August 2021__
> · Return of the Relic Hunt Daily Mission Rewards x2
> · Rune EXP Buff effect +100%
> · Combo Kill Orb EXP gain +300%
> 
> __2nd Sunday: 22nd August 2021__
> · Return of the Relic Hunt Daily Mission Rewards x2
> · Monster Park Clear EXP +50%
> 
> __3rd Sunday: 29th August 2021__
> · Monster Collection 'Mysterious Momon' x3 issued (Look for [Sunday Maple] Here's your Sunday Maple Gift! in Star notification)
> · 100% extra chance for new Monster Collection registration
> 
> __4th Sunday: 5th September 2021__
> · 30% off Star Force Enhancement Cost
> 
> __5th Sunday: 12th September 2021__
> · 50% off Spell Trace enhancement cost
> 
> __6th Sunday: 19th September 2021__
> · Polo and Frito's Bounty Hunt EXP x2
> · Defeat Flame Wolf EXP x2
> 
> __7th Sunday: 26th September 2021__
> · Selective Arcane Symbol Exchange Coupon x20 and 3X EXP Coupon (15 mins) x5 issued (Look for [Sunday Maple] Here's your Sunday Maple Gift! in Star notification)
"""


async def sundaymaple(message):
    message_to_send = current_sundaymaple
    await message.channel.send(message_to_send)