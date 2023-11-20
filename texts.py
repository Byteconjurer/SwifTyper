import random

class Texts:
    easy_texts = [
        "I fear Not the man who\nhas practiced Ten thousand\nkicks once but I Fear\nthe man who has Practiced\none Kick ten thousand times",
        "here's looking at you kid\nplay it once sam For old times sake\nim shocked, shocked to find that gambling is going on in here!\nround up the usual suspects\nkiss me. kiss me as if it were the last time\nlouis, i think this is the beginning of a beautiful friendship",
        "i wandered lonely as a cloud\nthat floats on high over vales and hills\nwhen all at once I saw a crowd\na host, of golden daffodils\nfluttering and dancing in the breeze\ncontinuous as the stars that shine",
        "my dad gave me one dollar bill\ncause i'm his smartest son\nand i swapped it for two shiny quarters\n'cause two is more than one",
        "here's looking at you, kid\nmurmured rick as he gazed into ilsa's eyes\nthe air was filled with the bittersweet melody of a piano\nechoing the romance of casablanca",
        "life is like a box of chocolates\nForrest mused, reflecting on the unpredictable nature of existence\neach moment held a surprise\nmuch like the sweet variety in gump's box",
        "you can't handle the truth! \nroared Colonel jessup, a powerful moment\nin the courtroom drama of a few good men\nthe intensity of the scene lingered in the air"
    ]

    medium_texts = [
        "\"You can't handle the truth!\"\nroared Colonel Jessup, a powerful\nmoment in the courtroom drama of A Few Good Men.\nThe intensity of the scene lingered in the air.",
        "\"Here's Johnny!\" echoed through the empty halls \nof the Overlook Hotel. \nThe Shining's chilling tale unfolded, \nblending horror and suspense in Kubrick's masterpiece.",
        "\"You can't change the past, but you can learn from it,\" \nadvised Gil in Midnight in Paris. The allure of time travel \nblended with nostalgia, creating a captivating narrative.",
        "\"To infinity and beyond!\" proclaimed Buzz Lightyear, \nembarking on an intergalactic adventure. \nToy Story's animated charm resonated, \ntranscending the limits of imagination.",
        "\"I am your father,\" revealed Darth Vader. \nThe revelation echoed through the galaxy, \naltering the course of Star Wars, \na pivotal moment in cinematic history.",
        "Neutrinos, elusive particles with infinitesimal mass, \noscillate in quantum ballets. String theory's harmonious \nmelodies weave 10-dimensional symphonies. \nAstrophysicists unveil cosmic secrets: \n13.8 billion years of cosmic evolution, a celestial odyssey.",
        "Sibilant serpents swiftly slithered, shrouded in shadows. \nPeter Piper, a prolific pepper picker, piqued palates profoundly. \nSix slippery snails silently slid southward, seeking sunlit sanctuaries.",
        "Palindrome perfection: A man, a plan, a canal, Panama! \nMadam, in Eden, I'm Adam. Racecar radar, reviver of words. \nTenet palindrome, reads same forward and backward, a linguistic feat."
    ]

    hard_texts = [
        "Fuel levels at 90%, altitude 30,000 feet. \n'I feel the need... the need for speed!' \nMaverick radioed, pushing Top Gun's F-14s to Mach 2, \na rush of velocity through the skies!",
        "Quantum physics unraveled: Schrödinger's cat \ndanced between 0 and 1. Accelerating at 9.8 m/s^2, \nastronauts gazed at the cosmos. Mathematical \nelegance met celestial mysteries.",
        "Neuropl@sticity, a symphony of synapses, \nrewired cognitive landscapes 4.0. Exoplanet exploration: \na cosmic endeavor. Synchronizing datastreams, \nengineers decoded the enigma of prime numbers \nusing 0s, 1s, and %",
        "Polyrhythmic jazz echoed in the 21st-century groove. \nFibonacci sequence, 1-1-2-3-5-8, unfolded in golden spirals. \nCryptocurrency miners deciphered blockchain's \nintricate code: cRypT0!",
        "Vini, vidi, vino! Fermentation's alchemical dance, \n25C, transforms grapes into nectar. Cabernet Sauvignon, \na Bordeaux symphony, ages in oaken barrels. \nSip, swirl, savor: T@nn1n$!"
    ]

    @classmethod
    def get_random_text(cls, mode: str):
        """Returns a random text based on the mode"""

        if mode == "EASY":
            return random.choice(cls.easy_texts)
        elif mode == "MEDIUM":
            return random.choice(cls.medium_texts)
        elif mode == "HARD":
            return random.choice(cls.hard_texts)
        else:
            raise ValueError("Invalid mode")

        

        
