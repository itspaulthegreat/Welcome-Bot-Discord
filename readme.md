# Melodies bot

## To run locally

Just uncomment  the below lines in main.py
and use your own config.jsons

```
    # with open('config.json') as fh:
    # bot.config = json.load(fh)
    # bot.run(bot.config['token'])
```

## To host

Use Heroku and use the follwing build packs in order

```
1) https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest

2) heroku/python

3) https://github.com/Crazycatz00/heroku-buildpack-libopus

```
## To use

Use ```|play or |p``` to play and make the bot join ur voice channel
Use ```|leave``` to leave the bot from voice channel
Use ```|np``` to see whats playing
Use ```|skip``` to voteskip