from heygenbot import HeygenBot

bot = HeygenBot("path", "session_cookie_value")
bot.login()
bot.verify_login()
bot.create_video("Hey there! This video was generated entirely using automation. Isn't that cool?,", video_title="Demo Clip")
bot.close(delay=60)