# Copyright (C) 2021 By Team UltraX 

# ~ LegendX
# ~ ProBoyX
# ~ MadBoy

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by LegendX
# Mobile me back option he uspe click karde madhachod kang kiya to dekh
import ULTRA.plugins.sql_helper.pmpermit_sql as ULTRA_X
from .import *
from ..data.alive_db import *
import os, re, sys
from ULTRAX import id, ID, devs
from telethon.tl.functions.contacts import BlockRequest as block
from telethon import Button, custom, events, functions
import asyncio
# back button click kr madarchod
from ULTRAX import NAME
ULTRA_USER = NAME

BOT_MAD = f"Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ UʟᴛʀᴀX, ғᴏʀ {ULTRA_USER}'s Pʀᴏᴛᴇᴄᴛɪᴏɴ\n\n"

WARN = (
  f'''
**{BOT_MAD}**
__Hᴇʏ ᴛʜᴇʀᴇ!! I'ᴍ__ **υℓтяα χ** __ᴀɴᴅ I'ᴍ ʜᴇʀᴇ ᴛᴏ Pʀᴏᴛᴇᴄᴛ **{ULTRA_USER}**..\nDᴏɴ'ᴛ Uɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ 😈😈__**
__Mʏ Mᴀsᴛᴇʀ **{ULTRA_USER}**  ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ !!__ \n"
Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM, Aɴᴅ ɪ'ʟʟ ᴅᴏ ɪᴛ ғᴀɪᴛʜғᴜʟʟʏ..Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ..
**Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ...**
**Bᴇᴛᴛᴇʀ ʙᴇ ᴄᴀʀᴇғᴜʟ..**
**Cʜᴏᴏsᴇ ᴀɴʏ Rᴇᴀsᴏɴ & GTFO**
''')

back = [[Button.inline("«« Bᴀᴄᴋ", data="pm_back")]]
@xbot.on(events.InlineQuery())
async def inline_legend(event):
  piro = event.text
  pm_text = await get_pm_text()
  if pm_text:
    WARN = pm_text
  else:
    pass
  ULTRA_PIC = await get_pm_img()
  if event.sender_id == bot.me.id and piro == 'pmsecurity' or event.sender_id==id and piro=='pmpermit':
    LEGENDX = event.builder
    LEGEND = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
    LEGEND += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
    LEGEND += [[Button.inline("Aᴘᴘʀᴏᴠᴇ ᴍᴇ",data='approve_piro')]]
    PROBOYX = LEGENDX.photo(file=ULTRA_PIC, text=WARN, buttons=LEGEND)
    await event.answer([PROBOYX])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chutia')))
async def chutia_aayaa(event):
  global back
  if event.sender_id !=bot.me.id or event.sender_id != id:
     CONFIRM = [[Button.inline("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", data='confirm_chutia')]]
     CONFIRM += back
     await event.edit("**Aʀᴇ ʏᴏᴜ sᴘᴀᴍᴍᴇʀ?**", buttons=CONFIRM)
  else:
     No = "**Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ**"
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'confirm_chutia')))
async def confirmed(event):
  pro=event.sender_id
  global block
  if pro != bot.me.id or pro != ID:
    await event.edit("**Oʜᴋ sᴏ ɢᴏ ᴛᴏ ʜᴇʟʟ ᴅᴜᴅᴇ 😁**")
    await bot(block(pro))
  else:
     No = "**Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ**"
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'frnd_bsdk')))
async def Inline_legendx(event):
  piro = event.sender_id
  global back
  if piro != bot.me.id or piro != id:
    await event.edit("**Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!**", buttons=back)
  else:
    await event.answer("**Mᴀsᴛᴇʀ, ᴜsᴇ** `.approve` **ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʜɪᴍ**")
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'noobda')))
async def noobda (event):
  global back
  Piro = [[Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/UltraXchaT"), Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/UltraXoT")]]
  Piro += [[Button.url("Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X")]]
  Piro += back
  await event.edit("**CʜᴇᴄᴋOᴜᴛ ᴛʜᴇsᴇ ʟɪɴᴋs**", buttons=Piro)
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'pm_back')))
async def inline_legend(event):
  acha = event.sender.first_name
  jnl = bot.me.first_name
  LEGENDX = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
  LEGENDX += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
  await event.edit(f"Hᴇʟʟᴏ **{acha}**, ᴍʏ sᴇʟғ UʟᴛʀᴀX, ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ **{jnl}**!", buttons=LEGENDX)
  
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'nino')))
async def _(event):
  global back
  await event.edit("**Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!**", buttons=back)
  
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'hmmmmm')))
async def _(event):
  kk = [[Button.inline("Yᴇs", data='confirm_chutia')]]
  kk += [[Button.inline("Nᴏ", data='nino')]]
  await event.edit("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", buttons=kk)
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'approve_piro')))
async def approve(event):
  if event.sender_id != ID or event.sender_id != bot.me.id:
    return await event.answer("you can't use nibba", alert=True)
  if ULTRA_X.is_approved(event.chat_id):
    try:
      ULTRA_X.approve(event.chat_id, f"inline approve {event.chat.username or 'no username'}")
      k = await event.edit('ʏᴏᴜ ᴀʀᴇ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴍʏ ᴍᴀsᴛᴇʀ ɴɪʙʙᴀ')
    except Exception as e:
      await event.answer(str(e), alert=True)
      sys.exit()
    await asyncio.sleep(2)
    async for x in bot.iter_messages(event.chat_id, from_user="me", limit=8):
      if x.id == k.id:
        pass
      else:
        try:
          await bot.delete_message(event.chat_id, x.id)
        except:
          pass
  else:
    await event.answer("This user approved", alert=False)


  

# Copyright (C) 2021 By Team UltraX 

# ~ LegendX
# ~ ProBoyX
# ~ MadBoy

# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
# Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by LegendX
# Mobile me back option he uspe click karde madhachod kang kiya to dekh
