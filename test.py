from heygenbot import HeygenBot

bot = HeygenBot("path", "sessionid")
bot.login()
#bot.create_video("I want to take a moment to commend VAAGDHARA for your remarkable commitment to uplifting tribal communities, especially your focus on True Childhood, True Farming, and True Governance. It's amazing to see how you have impacted over 130,000 families across more than a thousand villages. I’m Karma, a fundraising strategist who has successfully helped nonprofits raise over $10 million to further their missions. I’d like to introduce you to an innovative tool that could enhance your efforts—a Donor Stewardship AI Agent that creates personalized three-part email sequences for your donors. This tool can specifically address challenges like sustaining child protection programs and raising awareness about sustainable practices among farmers. Let me know if I can send you more information or if you’d like to set up a quick 15-minute call to discuss how this can benefit VAAGDHARA.", video_title="Demo Clip")
bot.save_video()
bot.close(delay=60)