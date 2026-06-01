# Words for hangman game
easy_words = (
    "apple", "banana", "cherry", "orange", "grape", "mango", "peach", "pear", "plum", "kiwi",
    "computer", "laptop", "keyboard", "mouse", "monitor", "printer", "router", "internet", "server", "network",
    "python", "java", "ruby", "swift", "kotlin", "html", "css", "javascript", "react", "django",
    "school", "teacher", "student", "library", "classroom", "notebook", "pencil", "chalk", "exam", "homework",
    "elephant", "giraffe", "tiger", "lion", "zebra", "monkey", "panda", "kangaroo", "rabbit", "fox",
    "river", "mountain", "forest", "desert", "ocean", "island", "valley", "hill", "waterfall", "volcano",
    "chair", "table", "window", "door", "lamp", "bed", "mirror", "sofa", "shelf", "carpet",
    "doctor", "nurse", "police", "fireman", "driver", "chef", "pilot", "engineer", "farmer", "artist",
    "music", "guitar", "piano", "violin", "drums", "flute", "trumpet", "song", "dance", "melody",
    "planet", "galaxy", "asteroid", "comet", "rocket", "satellite", "space", "orbit", "gravity", "eclipse"
)

hard_words = (
    # Fruits
    "apple", "banana", "cherry", "orange", "grape", "mango", "peach", "pear", "plum", "kiwi",
    "lemon", "lime", "papaya", "guava", "pineapple", "apricot", "fig", "coconut", "date", "berry",
    "watermelon", "strawberry", "blueberry", "blackberry", "raspberry", "pomegranate", "tangerine", "cantaloupe", "avocado", "grapefruit",

    # Animals
    "dog", "cat", "lion", "tiger", "leopard", "elephant", "zebra", "monkey", "panda", "giraffe",
    "bear", "wolf", "fox", "deer", "rabbit", "kangaroo", "koala", "crocodile", "snake", "lizard",
    "dolphin", "whale", "shark", "octopus", "crab", "fish", "eagle", "parrot", "owl", "pigeon",
    "goat", "sheep", "cow", "horse", "pig", "hen", "duck", "goose", "turkey", "camel",

    # Objects
    "chair", "table", "sofa", "bed", "lamp", "mirror", "window", "door", "carpet", "shelf",
    "television", "radio", "phone", "camera", "clock", "bottle", "cup", "plate", "bowl", "fork",
    "spoon", "knife", "book", "pen", "pencil", "notebook", "bag", "shoe", "shirt", "trouser",
    "watch", "ring", "bracelet", "necklace", "hat", "umbrella", "towel", "blanket", "pillow", "fan",

    # Professions
    "teacher", "doctor", "nurse", "engineer", "lawyer", "pilot", "driver", "police", "fireman", "chef",
    "farmer", "artist", "musician", "writer", "journalist", "actor", "architect", "scientist", "dentist", "plumber",
    "electrician", "mechanic", "carpenter", "barber", "soldier", "waiter", "tailor", "accountant", "receptionist", "cleaner",

    # Verbs
    "run", "walk", "jump", "dance", "sing", "read", "write", "eat", "drink", "sleep",
    "smile", "laugh", "cry", "think", "talk", "listen", "watch", "play", "swim", "fly",
    "drive", "cook", "clean", "draw", "paint", "climb", "sit", "stand", "open", "close",
    "throw", "catch", "cut", "build", "break", "fix", "move", "push", "pull", "carry",

    # Adjectives
    "happy", "sad", "angry", "tired", "sleepy", "hungry", "thirsty", "beautiful", "ugly", "strong",
    "weak", "fast", "slow", "big", "small", "tall", "short", "young", "old", "brave",
    "clever", "stupid", "funny", "serious", "loud", "quiet", "rich", "poor", "kind", "rude",
    "bright", "dark", "hot", "cold", "warm", "cool", "wet", "dry", "soft", "hard",

    # Countries & Places
    "nigeria", "ghana", "kenya", "southafrica", "egypt", "morocco", "ethiopia", "canada", "brazil", "argentina",
    "mexico", "usa", "france", "germany", "italy", "spain", "portugal", "england", "china", "japan",
    "india", "australia", "newzealand", "russia", "ukraine", "poland", "sweden", "norway", "finland", "switzerland",
    "turkey", "saudiarabia", "israel", "qatar", "uae", "iran", "iraq", "pakistan", "bangladesh", "philippines",

    # Food
    "rice", "beans", "bread", "butter", "cheese", "egg", "meat", "fish", "chicken", "soup",
    "stew", "yam", "noodles", "spaghetti", "potato", "pizza", "burger", "sandwich", "salad", "cake",
    "chocolate", "biscuit", "icecream", "tea", "coffee", "milk", "juice", "water", "sugar", "salt",

    # Nature
    "tree", "flower", "grass", "leaf", "branch", "root", "river", "mountain", "valley", "hill",
    "forest", "desert", "ocean", "sea", "beach", "island", "lake", "sky", "rain", "cloud",
    "storm", "lightning", "thunder", "snow", "ice", "fire", "wind", "sand", "rock", "sun",

    # Technology
    "computer", "laptop", "keyboard", "mouse", "monitor", "printer", "scanner", "router", "internet", "server",
    "network", "email", "software", "hardware", "database", "program", "website", "browser", "password", "screen",
    "phone", "tablet", "charger", "battery", "camera", "speaker", "microphone", "headphone", "video", "signal",

    # Random nouns
    "ball", "game", "sport", "goal", "team", "match", "stadium", "coach", "referee", "score",
    "bookstore", "market", "shop", "office", "school", "library", "church", "mosque", "bank", "hospital",
    "garden", "park", "museum", "bridge", "road", "car", "bus", "train", "ship", "plane",
    "airport", "station", "city", "village", "house", "building", "street", "avenue", "corner", "square",

    # Emotions / abstract
    "love", "hate", "joy", "anger", "fear", "peace", "hope", "dream", "trust", "faith",
    "truth", "lie", "honor", "shame", "pride", "guilt", "patience", "courage", "wisdom", "power",
    "freedom", "justice", "friendship", "kindness", "luck", "destiny", "memory", "future", "past", "present",

    # Science
    "atom", "molecule", "cell", "energy", "force", "gravity", "planet", "star", "galaxy", "universe",
    "comet", "asteroid", "rocket", "space", "satellite", "telescope", "microscope", "experiment", "theory", "scientist",
    "oxygen", "hydrogen", "carbon", "nitrogen", "helium", "iron", "gold", "silver", "copper", "zinc",

    # Miscellaneous
    "music", "song", "melody", "rhythm", "sound", "voice", "drum", "guitar", "piano", "violin",
    "dance", "art", "painting", "drawing", "color", "film", "movie", "actor", "director", "camera",
    "holiday", "vacation", "travel", "journey", "adventure", "discovery", "island", "desert", "temple", "castle",
    "bridge", "tower", "palace", "garden", "riverbank", "harbor", "mountain", "cave", "forest", "volcano",

    # Random fillers to reach 500
    "gate", "fence", "ladder", "bucket", "rope", "nail", "hammer", "spanner", "drill", "brush",
    "paint", "wall", "floor", "roof", "ceiling", "tile", "pipe", "wire", "switch", "socket",
    "coin", "money", "wallet", "purse", "ticket", "passport", "key", "lock", "bell", "alarm",
    "medicine", "tablet", "injection", "needle", "bandage", "mask", "soap", "toothpaste", "brush", "comb",
    "broom", "dustbin", "bucket", "mop", "vacuum", "tissue", "sponge", "detergent", "rag", "cleaner"
)

