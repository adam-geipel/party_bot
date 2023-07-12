# Party Bot for Discord

## NOTE: THIS IS A CRUDE WORK IN PROGRESS


### What it does

Party Bot is a bot that assists in telling users when there is an opening in a party. It's designed with Battle Royale games (e.g. Call of Duty Warzone) in mind, where trios and quads are most desirable.

-----
## Setup


### The Bot

This requires an existing bot. Users can then get their own auth tokens and add the bot to their own Discord servers as they desire.

### The deployment environment
Create a `.env` file and set the `DISCORD_TOKEN` environment variable to the bot's auth token. For example:
```text
DISCORD_TOKEN="your_token_here"
```

-----
## Deployment

Just run the docker container using the provided dockerfile.

---

## Project Roadmap

Here's where I want to take this bot:
- Add a database to the environment so the `/subscribe` command can store subscribers
    - I'll probably switch  to docker-compose to do this
- Hook in the database so the bot can check on subscribers and notify them (rather than sending notifications to `@everyone`)
- Add support for subscribing to specific voice channels
- Clean up the codebase. Doing everythin in one file, for starters, is gross.
