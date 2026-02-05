import state
from vc.player import stop_play, join_vc

async def toggle_bass():
    state.bass_enabled = not state.bass_enabled
    if state.playing_group:
        await stop_play()
        await join_vc(state.playing_group)

async def mute_self(client, chat_id):
    await client.mute_chat(chat_id)

async def unmute_self(client, chat_id):
    await client.unmute_chat(chat_id)
