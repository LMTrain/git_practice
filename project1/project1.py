songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20}

inventory["invisible knife"] = 40
inventory["mithril shield"] = 25

conference_rooms = ["executive", "hopper", "lovelace", "pod", "snooze booth"]
capacity = [7, 20, 6, 2, 1]
room_dict = {key:value for key, value in zip(conference_rooms, capacity)}

print(room_dict)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])
