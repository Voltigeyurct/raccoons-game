import random
from random_word import RandomWords

class WordGame:
    def __init__(self):
        self.r = RandomWords()
        self.current_word = ""
        self.attempts_left = 5
        self.score = 0
        self.game_over = False
        self.word_list = [
            # Original NFT Project Words
            "raccoon", "forest", "crypto", "blockchain", "digital",
            "nature", "animal", "token", "wallet", "smart",
            "future", "gaming", "player", "winner", "reward",
            "artist", "unique", "market", "secure", "invest",
            "mining", "minter", "holder", "profit", "trade",
            "launch", "rarity", "design", "create", "stake",
            
            # NFT and Crypto Terms
            "metaverse", "opensea", "ethereum", "solana", "polygon",
            "discord", "twitter", "roadmap", "utility", "community",
            "presale", "public", "private", "airdrop", "whitelist",
            "genesis", "avatar", "artwork", "auction", "bidding",
            "collect", "creator", "diamond", "edition", "emerald",
            "gallery", "hybrid", "legacy", "limited", "master",
            "mystery", "network", "premium", "project", "quality",
            "ranking", "sapphire", "special", "status", "system",
            "virtual", "volume", "bridge", "bundle", "burning",
            "custody", "delist", "deposit", "royalty", "scarcity",
            "staking", "supply", "trading", "transfer", "upgrade",
            "verify", "version", "vintage", "visible", "wrapped",
            "yielding", "zkproof", "address", "balance", "connect",
            "contract", "decrypt", "encrypt", "gasless", "history"
        ]

    def start_new_game(self):
        self.current_word = random.choice(self.word_list)
        self.attempts_left = 5
        self.score = 0
        self.game_over = False
        return self._mask_word()

    def _mask_word(self):
        masked = list('_' * len(self.current_word))
        # Show first and last letter as hints
        masked[0] = self.current_word[0]
        masked[-1] = self.current_word[-1]
        return ' '.join(masked)

    def make_guess(self, guess):
        if self.game_over:
            return {"message": "Game is over!", "status": "error"}

        if len(guess) != len(self.current_word):
            return {"message": f"Word must be {len(self.current_word)} letters long!", "status": "error"}

        if guess.lower() == self.current_word.lower():
            self.score += 1
            if self.score >= 3:
                self.game_over = True
                return {"message": "Congratulations! You've completed the Racoon Word Game! 🎉", "status": "win"}
            else:
                old_word = self.current_word
                self.current_word = random.choice(self.word_list)
                while old_word == self.current_word:
                    self.current_word = random.choice(self.word_list)
                return {
                    "message": f"Correct! Score: {self.score}/3. Next word:",
                    "status": "correct",
                    "masked_word": self._mask_word()
                }
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                self.game_over = True
                return {"message": "Game Over! You ran out of attempts.", "status": "lose"}
            return {
                "message": f"Wrong guess! {self.attempts_left} attempts left.",
                "status": "wrong",
                "masked_word": self._mask_word()
            }
