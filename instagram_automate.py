from instabot import Bot
bot=Bot()
bot.login(username="id",pasword="xyz")
bot.follow("wscubetechindia i.e. to whom we have to follow")
bot.upload_photo("photo_address",caption="I love python")
bot.unfollow("wscubetechindia i.e. to whom we have to follow")
bot.send_message("I love python",["username1"],["username2"],["username3"])
followers=bot.get_user_followers("username, of whom we have to check the followers")
for follower in followers:
    print(bot.get_user_followers(follower))
following=bot.get_user_followers("username, of which we have to check the followings")
for Following in following:
    print(bot.get_user_info(Following))

