from telegram import Update
from telegram.ext import ContextTypes
from config import OWNER_ID, SUDO_USERS
import state

from vc.player import join_vc, leave_vc, stop_play
from vc.controls import toggle_bass
from vc.user import user

def sudo(uid):
    return uid == OWNER_ID or uid in SUDO_USERS

async def addsession(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not sudo(update.effective_user.id):
        return await update.message.reply_text("❌ YOU MUST BE SUDO")
    await update.message.reply_text("✅ SESSION ACTIVE")

async def delsession(update, context):
    if not sudo(update.effective_user.id):
        return
    await user.stop()
    await update.message.reply_text("♻️ SESSION RESET")

async def setrecordgroup(update, context):
    if not sudo(update.effective_user.id):
        return
    state.record_group = update.effective_chat.id
    await update.message.reply_text("🎙 RECORD GROUP SET")

async def join(update, context):
    if not sudo(update.effective_user.id):
        return
    await join_vc(update.effective_chat.id)
    await update.message.reply_text("🔊 JOINED VC")

async def leave(update, context):
    if not sudo(update.effective_user.id):
        return
    await leave_vc(update.effective_chat.id)
    await update.message.reply_text("👋 LEFT VC")

async def bass(update, context):
    if not sudo(update.effective_user.id):
        return
    await toggle_bass()
    await update.message.reply_text("🎵 BASS TOGGLED")

async def mute(update, context):
    if not sudo(update.effective_user.id):
        return
    await user.mute_chat(update.effective_chat.id)
    await update.message.reply_text("🔇 MUTED")

async def unmute(update, context):
    if not sudo(update.effective_user.id):
        return
    await user.unmute_chat(update.effective_chat.id)
    await update.message.reply_text("🔊 UNMUTED")

async def leaverecord(update, context):
    state.record_group = None
    await update.message.reply_text("❌ RECORD GROUP DISCONNECTED")

async def leaveplay(update, context):
    await stop_play()
    await update.message.reply_text("⏹ PLAY STOPPED")
