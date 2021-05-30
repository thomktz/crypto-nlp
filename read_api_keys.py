"""
Create a file named API_keys.txt and format it as such, using the twitter API credentials :

consumer_key
consumer_secret_key
access_key
access_secret

"""
# %%
keys_file = open("API_keys.txt", "r")
keys = keys_file.read()
keys = keys.split("\n")

consumer_key, consumer_secret, access_key, access_secret = keys
