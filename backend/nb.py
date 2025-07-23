from collections import Counter, defaultdict
import pandas as pd
import numpy as np
import re

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
        self.alpha = 0.01
        self.class_probs = {}
        self.word_probs = defaultdict(Counter)
        for proj in self.projs:
            self.word_probs[proj] = Counter()
        self.denom = 0

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

        vocab_size = len(self.all_words)

        # Calculate class priors with inverse frequency weighting and normalization
        class_weights = {proj: 1.0 / self.num_projs[proj] for proj in self.projs}
        total_weight = sum(class_weights.values())
        proj_probs = []
        for proj in self.projs:
            weighted_prob = class_weights[proj] / total_weight  # Normalize so sum=1
            proj_probs.append(weighted_prob)

        # Calculate likelihoods with Laplace smoothing
        for proj in self.projs:
            focus_dict = self.word_counts[proj]
            denom = self.total_words[proj] + self.alpha * self.total_instances
            self.denom = denom  # Save for smoothing unknown words
            for word in self.all_words:
                if word not in focus_dict:
                    self.word_probs[proj][word] = self.alpha / denom
                else:
                    self.word_probs[proj][word] = (focus_dict[word] + self.alpha) / denom

        # Log of class prior probabilities
        temp = np.log(proj_probs)
        # self.class_probs = {self.projs[i]: temp[i] for i in range(len(temp))}
        self.class_probs = {self.projs[i] : 0 for i in range(len(temp))}

    def preprocess(self, text):
        # Lowercase and keep only words, excluding stop words and short words
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return [w for w in words if w not in self.stop_words and len(w) > 2]

    def predict(self, desc):
        pp_desc = self.preprocess(desc)
        cur_class_probs = self.class_probs.copy()

        for proj in self.projs:
            for word in pp_desc:
                # Use smoothed probability or fallback
                cur_class_probs[proj] += np.log(self.word_probs[proj].get(word, self.alpha / self.denom))

        # Return class with highest log-probability
        preds = {'A': "Artificial Intelligence", "S" : "Security", "G" : "Game Development", "W": "Web Development"}
        
        # Show the score for each class in terminal
        for prob in sorted(cur_class_probs, key=cur_class_probs.get, reverse=True):
            print(prob+": "+str(-1*round(cur_class_probs[prob], 2)))

        return preds[max(cur_class_probs, key=cur_class_probs.get)]


classy = Classifier()
classy.retrain()
