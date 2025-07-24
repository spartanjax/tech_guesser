from collections import Counter, defaultdict
import pandas as pd
import numpy as np
import re
import data
import boost_words

class Classifier:
    def __init__(self):
        # Stop words set
        self.stop_words = {
            'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't",
            'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by',
            'can', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing',
            "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't",
            'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself',
            'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is',
            "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no',
            'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves',
            'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so',
            'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then',
            'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those',
            'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're",
            "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while',
            'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll",
            "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'
        }

        # Initialize variables needed for training and prediction
        self.X = None
        self.y = None
        self.projs = ["A", "S", "G", "W"]

        self.total_words = {proj: 0 for proj in self.projs}
        self.num_projs = {proj: 0 for proj in self.projs}
        self.word_counts = defaultdict(Counter)
        for proj in self.projs:
            self.word_counts[proj] = Counter()
        self.all_words = Counter()
        self.total_instances = 0
        self.alpha = 0.01 #Laplace constant
        self.beta = 50 #Boost constant
        self.max_length = 200
        self.class_probs = {}
        self.word_probs = defaultdict(Counter)
        for proj in self.projs:
            self.word_probs[proj] = Counter()
        self.denoms = {}
        
    def adjust_beta(self, new_val):
        self.beta = new_val


    def retrain(self, csv_file="train.csv"):
        # Load data from CSV
        df = pd.read_csv(csv_file)
        self.X = df["Description"].values
        self.y = df["Class"].values

        self.total_instances = len(self.X)

        # Reset counts
        self.total_words = {proj: 0 for proj in self.projs}
        self.num_projs = {proj: 0 for proj in self.projs}
        self.word_counts = defaultdict(Counter)
        for proj in self.projs:
            self.word_counts[proj] = Counter()
        self.all_words = Counter()

        # Count words per class
        for i in range(self.total_instances):
            pred, desc = self.y[i], self.X[i]
            pp_desc = self.preprocess(desc)

            self.word_counts[pred].update(pp_desc)
            self.total_words[pred] += len(pp_desc)
            self.all_words.update(pp_desc)
            self.num_projs[pred] += 1


        temp = Counter()
        for word, count in self.all_words.items():
            if "_" in word:
                if count >= 3:
                    temp[word] = count
            else:
                temp[word] = count
        self.all_words = temp
        # Calculate class priors with inverse frequency weighting and normalization
        # class_weights = {proj: 1.0 / self.num_projs[proj] for proj in self.projs}
        # class_weights = {proj: self.num_projs[proj] / self.total_instances for proj in self.projs}
        # total_weight = sum(class_weights.values())

        # proj_probs = []
        # for proj in self.projs:
        #     weighted_prob = class_weights[proj] / total_weight  # Normalize so sum=1
        #     proj_probs.append(weighted_prob)

        # Calculate likelihoods with Laplace smoothing
        self.vocab_size = len(self.all_words)
        for proj in self.projs:
            focus_dict = self.word_counts[proj]
            self.denoms[proj] = self.total_words[proj] + self.alpha * self.vocab_size
            for word in self.all_words:
                if word not in focus_dict:
                    self.word_probs[proj][word] = self.alpha / self.denoms[proj]
                else:
                    self.word_probs[proj][word] = (focus_dict[word] + self.alpha) / self.denoms[proj]
        
        # Log of class prior probabilities
        # proj_probs = [self.num_projs[proj] / self.total_instances for proj in self.projs]
        proj_probs = [1/len(self.projs)] * len(self.projs)
        temp = np.log(proj_probs)
        self.class_probs = {self.projs[i]: temp[i] for i in range(len(temp))}

    def preprocess(self, text):
        text = text.lower()
        words = [w for w in re.findall(r'\b\w+\b', text) if w not in self.stop_words]
        bigrams = []
        bigrams = [f"{words[i-1]}_{words[i]}" for i in range(1, len(words))]
        return words + bigrams

    def additional_training(self, pred, desc):
        pp_desc = self.preprocess(desc)
        self.word_counts[pred].update(pp_desc)
        self.total_words[pred] += len(pp_desc)
        self.all_words.update(pp_desc)
        self.num_projs[pred] += 1

        # Recalculate word probabilities for affected class (or all classes if you prefer)
        for proj in self.projs:
            focus_dict = self.word_counts[proj]
            self.denoms[proj] = self.total_words[proj] + self.alpha * self.total_instances
            for word in self.all_words:
                if word not in focus_dict:
                    self.word_probs[proj][word] = self.alpha / self.denoms[proj]
                else:
                    self.word_probs[proj][word] = (focus_dict[word] + self.alpha) / self.denoms[proj]

    def predict(self, desc):
        # print(desc)
        if len(desc.split(" ")) < 1:
            print("Word requirement not met.")
            return "Please describe the project in more depth!"
        
        pp_desc = self.preprocess(desc)
        cur_class_probs = self.class_probs.copy()
        desc_length = max(len(pp_desc), 1) 
        scaling_factor = np.sqrt(desc_length) 

        # print(pp_desc)
        
        for proj in self.projs:
            for word in pp_desc:
                # Use smoothed probability or fallback
                # cur_class_probs[proj] += np.log(self.word_probs[proj].get(word, self.alpha / self.denoms[proj]))
                prob = self.word_probs[proj].get(word, self.alpha / (self.total_words[proj] + self.alpha*self.vocab_size))
                log_boost = boost_words.log_boosts.get(proj, {}).get(word, 0.0)
                cur_class_probs[proj] += np.log(prob) + (log_boost * self.beta * scaling_factor / np.sqrt(self.max_length))

        # Return class with highest log-probability
        preds = {'A': "Artificial Intelligence", "S" : "Security", "G" : "Game Development", "W": "Web Development"}
        
        # Show the score for each class in terminal
        # print("Description: "+desc)
        for prob in sorted(cur_class_probs, key=cur_class_probs.get, reverse=True):
            print(prob+": "+str(round(cur_class_probs[prob], 2)))

        
        if len(Counter(cur_class_probs.values())) == 1:
            prediction =  "Please describe the project in more depth!"
        else:
            prediction = preds[max(cur_class_probs, key=cur_class_probs.get)]
        print(prediction)
        return prediction


classy = Classifier()
classy.retrain()
# for key in sorted(classy.all_words, key=classy.all_words.get, reverse=True):
#     print(key, classy.all_words[key])

# print(classy.predict('the ragebait ai has a 1/50 chance of responding to a message sent to a discord channel. it either glazes the message (with responses like: "facts 👏", "this is exactly why i joined this server 🔥", "keep talking and imma have to make out with you") or it ragebaits the message (with responses like: "interesting way to say absolutely nothing", "tf did i just read?", "i respect your confidence. not your point though"). theres other functionality in place to prevent it from being a harassment bot and to make it adhere to strict ethical guidelines, but thats extra for experts.'))
# classy.predict('web development')
# classy.predict('artificial intelligence')
# classy.predict('security')
# classy.predict('game development')
# print(classy.class_probs)
# print("Class instance counts:", classy.num_projs)


projects = [
    # AI Project
    "Developed an AI-powered recommendation system for an e-learning platform that personalized course suggestions based on user behavior and historical performance. The model combined collaborative filtering with natural language processing (NLP) to analyze user reviews and course descriptions. TensorFlow was used to build and train the deep learning model, which achieved a significant improvement in engagement metrics. The system was integrated into a React frontend via a Flask API and featured real-time updates as users interacted with content. It also included a feedback loop to retrain the model based on new user actions.",

    # Web Project
    "Built a full-stack job board web application designed for remote tech roles. The frontend was built in React with Tailwind CSS for a clean UI, and the backend used Node.js with Express and MongoDB for data storage. Key features included user authentication, job filtering by location/skills, and a real-time chat feature for employers and applicants using WebSockets. Admin users could approve or reject postings, and analytics dashboards showed application trends over time. The platform supported over 1,000 active users and implemented SEO optimization for public job listings.",

    # Cybersecurity Project
    "Designed and implemented a network intrusion detection system (NIDS) that analyzed live packet data to detect potential threats in real-time. Using Scapy and Python, the tool parsed and classified traffic into protocols, flagged anomalies using predefined signatures, and applied a machine learning model to identify novel attack patterns. A web dashboard built with Flask displayed visualized traffic data, including suspicious IPs and ports. The tool was deployed in a test environment simulating a corporate network, where it successfully identified simulated port scans, DDoS traffic, and credential stuffing attacks.",

    # Game Development Project
    "Created a 2D platformer game using Unity and C# inspired by classic retro mechanics. The game featured multiple levels, enemy AI with pathfinding, collectible items, and boss fights. A custom level editor was built into the game, allowing players to design and share their own levels. The game supported controller input and was exported for WebGL and Windows platforms. A leaderboard system tracked high scores using Firebase integration. Emphasis was placed on smooth animation transitions, responsive controls, and polished pixel art for a nostalgic experience."
]

for proj in projects:
    classy.predict(proj)


#Beta Testing
# betas = [0.1, 0.5, 1, 2, 5, 10, 20]
# for b in betas:
#     count = 0
#     classy.adjust_beta(b)
#     for proj in data.s:
#         if classy.predict(proj) == "Security":
#             count += 1

#     print(b, count/len(data.s))

