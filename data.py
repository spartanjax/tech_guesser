s = [
    "A tool that scans web applications for common vulnerabilities like SQL injection, XSS, and insecure cookies. It uses both static code analysis and live testing to identify risks, then outputs a prioritized mitigation report.",
    
    "A browser extension that detects phishing attempts in real-time by analyzing URLs, webpage layout, and SSL certificate details. It uses a trained Naive Bayes model to flag suspicious pages before users interact with them.",
    
    "A custom personal firewall with a graphical interface that lets users monitor, allow, or deny individual processes from making outbound connections. It groups traffic by domain and shows real-time usage patterns.",
    
    "A ransomware simulation lab where a safe 'ransomware' app encrypts dummy files, and students must identify the behavior and reverse the process using logs, decryption keys, or backups.",
    
    "A file integrity monitoring system that hashes system-critical files and periodically verifies their checksums, alerting the user if unauthorized changes occur.",
    
    "A network intrusion detection system using machine learning to detect abnormal traffic. It is trained on packet metadata (e.g., size, frequency, source/destination) and flags brute force, scanning, and spoofing attempts.",
    
    "A honeytoken deployment framework that generates fake credentials and monitors whether they are used, helping to detect credential theft or insider threats in an enterprise network.",
    
    "A password entropy evaluator that provides real-time strength feedback to users and gives guidance on improving password security using length, character variety, and unpredictability.",
    
    "An API security testing suite that simulates common attacks such as header injection, JWT manipulation, and insecure direct object references (IDOR), then reports back with fixes.",
    
    "A simple malware sandbox environment that logs system calls, file writes, and registry edits made by unknown executables in a virtual machine, helping classify potential threats.",
]

w = [
    "Developed a full-stack e-commerce platform that supports user authentication, product browsing, real-time inventory tracking, secure checkout via Stripe, and a custom admin dashboard for managing orders and analytics. Built using React, Node.js, Express, and MongoDB, the application also integrates Cloudinary for product image storage and uses JWT for session management. SEO optimization and responsive mobile-first design principles were implemented to ensure accessibility and performance across all devices. The project included automated email confirmation, password recovery, and dark/light theme toggling via CSS variables.",
    
    "Built a personal portfolio website using React and TailwindCSS to showcase software engineering projects, resume, and a blog section backed by Markdown files. The site uses Framer Motion for animations and is deployed on Netlify with CI/CD enabled via GitHub Actions. Custom hooks and components were used for theme toggling, lazy image loading, and smooth scroll navigation. The blog supports syntax-highlighted code blocks and image embeds, making it a powerful technical documentation tool as well.",
    
    "Created a job-board web app that allows companies to post openings and applicants to apply directly through a dynamic, responsive frontend. Used Vue.js with Vuex for frontend state management and Firebase as the backend and authentication layer. The admin panel includes CSV export features, spam filter controls, and posting approval workflows. Real-time updates ensure that job listings appear immediately across all devices. Deployed using Vercel, and includes basic analytics tracking with Google Analytics.",
    
    "Designed a collaborative real-time whiteboard app using WebSockets and Canvas API. Users can join rooms via invite links and draw together on a shared canvas with tools like pen, eraser, color picker, and shape drawers. The backend was built using Node.js and Socket.IO, while the frontend was made with vanilla JavaScript and CSS Grid. Persistent storage is handled via MongoDB to store snapshots of the canvas and user sessions. This project highlights how synchronous collaboration tools work under the hood.",
    
    "Developed a Progressive Web App (PWA) for recipe tracking that works offline and supports saving recipes to the home screen. Built using React and IndexedDB via localForage, the app syncs with a backend API when a connection is available. Service workers ensure offline availability and caching. Users can add custom recipes, categorize them, and search via tags or ingredients. A nutritional breakdown is calculated using the Edamam API integration. The UI is accessible and optimized for one-handed use on mobile devices.",
    
    "Created a browser-based markdown editor that previews content in real time, supports saving/loading drafts, and exports clean HTML. Built with React and CodeMirror, it features a side-by-side editing interface and collapsible toolbars. Themes are toggleable (light/dark/sepia), and shortcut keys enhance usability. The app includes live previewing with custom components for tables, links, and code blocks. Backend integration allows users to save their content via an Express and PostgreSQL API.",
    
    "Built a social networking site similar to Twitter, featuring a timeline, likes, retweets, and a follow system. Authentication uses OAuth 2.0 with Google and GitHub. The backend API, built with Django REST Framework, supports pagination and rate limiting. Redis is used for caching trending posts, and Celery is used for handling background jobs like email notifications. Users can upload avatars, edit bios, and set privacy settings. The frontend is powered by React and Redux Toolkit.",
    
    "Designed an event ticketing web app that allows event organizers to list, promote, and sell tickets. Used Next.js with server-side rendering for optimal SEO and dynamic routes for event pages. Stripe was used for payments, and tickets are issued as scannable QR codes. The dashboard includes analytics for views, sales, and attendance. Users receive digital receipts and tickets via email, and the platform supports refunds and discount codes. Integrated calendar syncing for attendees.",
    
    "Created a multi-language blog engine with Django, supporting dynamic translation of posts, tags, and UI elements. The CMS backend includes rich text editing with TinyMCE, post scheduling, and versioning. Frontend was built using Alpine.js and HTMX for dynamic updates without full page reloads. Used PostgreSQL with JSONB fields to store translation data. SEO features include sitemap generation and meta tag customization. Integrated Algolia for instant search across all articles.",
    
    "Developed a web-based kanban board app inspired by Trello. Users can create boards, lists, and draggable task cards with deadlines, file attachments, and markdown-enabled descriptions. Real-time updates are handled using Firebase. Offline support was implemented via service workers and local caching. The app is styled with TailwindCSS and includes accessibility features such as keyboard navigation and screen reader support. Authentication supports Google and email-based login."
]

g = [
    "Built a 2D platformer game using Unity and C#, featuring hand-drawn sprites and custom animations. The game includes multiple levels with increasing difficulty, enemy AI, power-ups, checkpoints, and a scoring system. Implemented parallax scrolling for dynamic backgrounds, sound effects with spatial audio, and save/load functionality using JSON serialization. A level editor was created using Unity’s UI system, allowing for custom map creation. Physics interactions use Unity’s Rigidbody2D and BoxCollider components to enable smooth character movement and interactions with the environment.",

    "Developed a multiplayer online battle arena (MOBA) prototype using Unreal Engine and Blueprints. Players choose unique heroes with abilities and compete in teams. The networked multiplayer is powered by Unreal’s replication system, with client-side prediction and server reconciliation. The game features a top-down camera, minimap, in-game chat, and skill cooldown system. Matchmaking and lobby systems were built using Photon. Environment assets were created using Quixel Megascans and custom shaders. An Elo-based ranking system tracks competitive performance.",

    "Created a roguelike dungeon crawler using Godot Engine and GDScript. Each playthrough features procedurally generated levels, randomized enemies, and item loot tables. The game supports keyboard/controller input and features a turn-based combat system. Health, armor, status effects, and inventory systems were modularized using Godot’s node-based scene architecture. Integrated tilemap-based level design and visual effects using shaders for darkness and fog of war. Saves progress using binary serialization to enable mid-run continuation.",

    "Designed a rhythm-based action game using JavaScript and the HTML5 Canvas API. Players must hit keys in time with the music to defeat enemies. Game state includes timing windows, scoring multipliers, and high score storage via `localStorage`. Audio was managed using the Web Audio API, with beat detection logic implemented for dynamic syncing. The game supports custom user-added songs through drag-and-drop file handling and dynamic beatmap generation. Responsive layout enables both desktop and mobile play.",

    "Built a text-based interactive fiction game in Python using the Ren'Py engine. The game features branching storylines, multiple endings, character stats that evolve based on decisions, and dynamic dialogue trees. Included custom GUI for choices, inventory system, and embedded puzzles to progress through the story. Integrated background music and animated scene transitions for immersion. Data-driven structure with external JSON for story progression, allowing easy content updates without touching source code.",

    "Developed a VR escape room experience using Unity and Oculus SDK. The game includes interactive puzzles using physics-based interactions, hand tracking, and spatial audio cues to guide players. Players can pick up, rotate, and combine objects to unlock secrets and exit the room. Voiceover hints were included for accessibility, and a timer tracks player progress. The environment was modeled using Blender and textured in Substance Painter. Experience was tested and refined with playtest feedback loops.",

    "Created a mobile idle/incremental game for Android using Kotlin and Android Studio. The game features a system of upgrades, achievements, and offline progress tracking. UI was built with Jetpack Compose, and game logic was separated via MVVM architecture. Data is persisted using Room (SQLite), and remote analytics are tracked using Firebase. Monetization was added through rewarded video ads and in-app purchases. Daily rewards, prestige system, and dynamic difficulty scaling keep users engaged long-term.",

    "Built a 3D flight simulator game using OpenGL and C++. Implemented real-time physics for flight dynamics, including lift, drag, thrust, and stall conditions. The game includes a heads-up display (HUD), multiple camera angles, and procedurally generated terrain using Perlin noise. Audio effects and weather simulation (wind, fog, day-night cycle) were added for immersion. Controls support both keyboard and joystick. Used SDL2 for input handling and windowing. Frame rate optimizations ensure smooth rendering across GPUs.",

    "Designed an educational game to teach kids math using Phaser.js. The game includes mini-games like arithmetic puzzles, time challenges, and memory tests with gamified rewards such as character skins and badges. Difficulty adjusts dynamically based on performance. Parental analytics dashboard shows progress trends and engagement. Backend is powered by Firebase, storing user profiles and progress. Used Google Text-to-Speech for accessibility, and responsive design ensures compatibility with tablets and smartphones.",

    "Created a puzzle-platformer game in Lua using the LÖVE framework. Gameplay involves manipulating the environment with time and gravity switches to solve puzzles. Designed over 40 hand-crafted levels with increasing complexity and hidden collectibles. Implemented a level selection menu, save/load system, and keyboard remapping. Used Tiled for level design and custom shaders for lighting and visual effects. Audio was handled with love.audio, and sprite animations were done frame-by-frame for smooth transitions."
]


a = [
    "Built a sentiment analysis system using Python and PyTorch to classify customer reviews as positive, neutral, or negative. The model was trained on a large corpus of labeled text using an LSTM architecture with pretrained GloVe embeddings. Data preprocessing included tokenization, stopword removal, and padding. Achieved over 90% accuracy on the test set. Deployed as a RESTful API with Flask and Docker, and integrated into a web dashboard using React. Also added visualization of word-level attention weights to explain model decisions for end users.",

    "Developed a computer vision model to detect plant diseases in crops from leaf images using TensorFlow and transfer learning with a pretrained EfficientNet model. The dataset consisted of over 50,000 annotated images across 30+ classes. Implemented data augmentation and class balancing to improve generalization. The system achieved high accuracy and was deployed on mobile using TensorFlow Lite for real-time farm usage. A dashboard tracks infection trends and provides early alerts for high-risk zones.",

    "Created a reinforcement learning agent using OpenAI Gym and Stable Baselines3 to teach an autonomous drone to navigate through an obstacle course. The agent used the Proximal Policy Optimization (PPO) algorithm and learned from simulated LIDAR input and positional feedback. Training was conducted in a custom Unity environment with communication via ML-Agents. Added curriculum learning to gradually increase difficulty. The project culminated in real-time simulation of drone path planning and obstacle avoidance.",

    "Designed a recommendation engine for an e-commerce platform using collaborative filtering and matrix factorization. Implemented user-based and item-based models in Python using Scikit-learn and Surprise libraries. Conducted A/B testing on real customer traffic to evaluate impact on engagement and conversion. Integrated hybrid features from product metadata and user profiles. The final system improved user retention and boosted click-through rates by over 20%. Recommendations were explained with similarity scores for transparency.",

    "Implemented a facial recognition and emotion detection system using OpenCV and deep learning. Used dlib for facial landmark detection and trained a CNN using the FER2013 dataset to classify emotions like happiness, anger, surprise, etc. The system was integrated into a real-time webcam application with live overlay of detected emotions. Added face identification using face embeddings from FaceNet and cosine similarity. Deployed with a Streamlit interface for user testing and data collection.",

    "Built an AI-powered chatbot for a university website using Rasa and spaCy. The bot could handle over 200 intents and respond with dynamic answers based on student queries. Integrated with backend services to fetch schedules, grades, and course details. Included fallback mechanisms and escalation to live chat. Training data was augmented using synthetic data generation. User satisfaction metrics were tracked using feedback forms and integrated analytics, helping improve intent classification over time.",

    "Trained a generative adversarial network (GAN) to create original artworks in the style of Monet and Van Gogh. Used CycleGAN to learn style transfer from photos to paintings. The model was trained on thousands of artwork images and tuned using perceptual loss. Generated images were evaluated with FID scores and curated via a web app gallery. Included a real-time style transfer demo where users could upload their own photos and receive stylized results.",

    "Developed a fraud detection system using an ensemble of tree-based models including XGBoost, LightGBM, and Random Forest. Trained on highly imbalanced financial transaction data with synthetic oversampling (SMOTE) and undersampling techniques. Evaluated models using precision-recall and ROC AUC metrics. The final pipeline included feature engineering with transaction metadata and behavioral patterns. Deployed the model with FastAPI and monitored false positive rates via a custom dashboard built with Plotly and Dash.",

    "Created an NLP summarization tool that generates concise summaries of research papers. Used a combination of extractive and abstractive techniques, leveraging BERT for extractive sentence scoring and a transformer-based seq2seq model for abstractive generation. Fine-tuned on the arXiv dataset. The tool includes a web interface with PDF upload and highlight features. Summaries are automatically tagged with relevant keywords using TF-IDF and RAKE. Hosted on Heroku with MongoDB for storing user queries and summaries.",

    "Built a traffic prediction model using LSTM networks to forecast congestion levels in urban areas. Historical traffic data was collected from city APIs and enriched with weather and event data. The time-series model accounted for daily and weekly patterns and predicted vehicle density and average speed. Incorporated spatial features using road network graphs. Results were visualized using heatmaps and integrated into a route-planning tool for city commuters. The model updated every hour with new data using a cron-based pipeline."
]
s_large = [
    "A tool that scans web applications for common vulnerabilities like SQL injection, XSS, and insecure cookies. It uses both static code analysis and live testing to identify risks, then outputs a prioritized mitigation report.",
    
    "A browser extension that detects phishing attempts in real-time by analyzing URLs, webpage layout, and SSL certificate details. It uses a trained Naive Bayes model to flag suspicious pages before users interact with them.",
    
    "A custom personal firewall with a graphical interface that lets users monitor, allow, or deny individual processes from making outbound connections. It groups traffic by domain and shows real-time usage patterns.",
    
    "A ransomware simulation lab where a safe 'ransomware' app encrypts dummy files, and students must identify the behavior and reverse the process using logs, decryption keys, or backups.",
    
    "A file integrity monitoring system that hashes system-critical files and periodically verifies their checksums, alerting the user if unauthorized changes occur.",
    
    "A network intrusion detection system using machine learning to detect abnormal traffic. It is trained on packet metadata (e.g., size, frequency, source/destination) and flags brute force, scanning, and spoofing attempts.",
    
    "A honeytoken deployment framework that generates fake credentials and monitors whether they are used, helping to detect credential theft or insider threats in an enterprise network.",
    
    "A password entropy evaluator that provides real-time strength feedback to users and gives guidance on improving password security using length, character variety, and unpredictability.",
    
    "An API security testing suite that simulates common attacks such as header injection, JWT manipulation, and insecure direct object references (IDOR), then reports back with fixes.",
    
    "A simple malware sandbox environment that logs system calls, file writes, and registry edits made by unknown executables in a virtual machine, helping classify potential threats.",
    
    "A browser-based clickjacking detector that overlays iframes and displays visual alerts when content is being loaded invisibly or manipulated via CSS/JS.",
    
    "A forensic disk imaging tool that copies bit-for-bit contents of a drive and maintains a cryptographic hash for evidence integrity, often used in digital investigations.",
    
    "A Bluetooth security analyzer that scans nearby devices for known vulnerabilities, like default PINs, open ports, or misconfigured profiles, and provides mitigation suggestions.",
    
    "An IoT device vulnerability scanner that audits common consumer hardware (like smart bulbs or cameras) on a local network for weak credentials or outdated firmware.",
    
    "A phishing simulation service that sends fake phishing emails to test employee awareness. The backend tracks who clicks and provides personalized training afterward.",
    
    "A secure file transfer protocol built on top of HTTPS with multi-factor authentication and automatic file encryption at rest and in transit.",
    
    "A cryptographic visualization tool that demonstrates how symmetric and asymmetric encryption works, complete with live encryption/decryption using AES and RSA in-browser.",
    
    "A rootkit detection tool that scans for hidden processes and kernel-level anomalies in Linux systems, comparing known good states to current behavior.",
    
    "A steganography detector that analyzes image and audio files for hidden messages using pixel deviation, byte analysis, and LSB analysis techniques.",
    
    "A log analyzer for detecting brute-force login attempts on web servers, correlating repeated failed logins by IP address and generating alerts.",
    
    "A port scanner that maps an entire subnet, identifies open ports, and categorizes them based on known vulnerabilities or default services.",
    
    "A zero-trust model demo environment showing how network segmentation and identity-aware proxies can prevent lateral movement even after an initial breach.",
    
    "A browser fingerprinting project that shows users how uniquely identifiable their browser is based on font support, resolution, extensions, and other metadata.",
    
    "A secure chat app using end-to-end encryption with forward secrecy, ephemeral keys, and tamper detection built-in.",
    
    "A secure code audit tool that scans Python or JavaScript projects for hardcoded credentials, unsafe function calls, or insecure libraries.",
    
    "A reverse engineering challenge platform that lets users analyze obfuscated binaries to extract strings, decode logic, and uncover functionality.",
    
    "A CVE tracker that regularly pulls the latest critical vulnerabilities in used dependencies and emails alerts for known issues in deployed systems.",
    
    "A virtual private network (VPN) setup guide and demo using WireGuard, teaching users about tunneling, encryption, and DNS leaks.",
    
    "A dark web crawler (ethical and restricted) that gathers breach data on specified keywords or email addresses to alert users of data exposure.",
    
    "A USB intrusion detector that alerts or locks the system when unauthorized USB devices are connected, optionally logging VID/PID for analysis.",
    
    "A biometric login system using facial recognition and voice print as a multi-factor method, tested against spoofing techniques and noise.",
    
    "A public-key infrastructure (PKI) simulator where users generate their own certs, simulate revocations, and explore how HTTPS validation really works.",
    
    "A wireless attack detection tool that monitors for deauthentication attacks, fake access points, and rogue DHCP servers in a given environment.",
    
    "A project that demonstrates DNS poisoning, then teaches how to defend against it using DNSSEC and network configuration best practices.",
    
    "A role-based access control (RBAC) demo platform that lets admins assign user permissions visually and enforces rules at the API level.",
    
    "A captive portal testing project that demonstrates how attackers can create rogue WiFi hotspots with fake login pages to steal credentials.",
    
    "A simulated CTF (capture the flag) challenge with real-world vulnerability exploits in web, binary, crypto, and reverse engineering domains.",
    
    "A browser exploit lab that demonstrates how XSS, CSRF, and CSP bypasses can be executed and prevented in modern browsers.",
    
    "A forensic timeline builder that organizes user activity (file access, browser history, USB insertions) from system logs into a readable timeline.",
    
    "A project comparing different password hashing algorithms (MD5, SHA256, bcrypt, Argon2) and demonstrating how fast each can be cracked with dictionary attacks.",
    
    "A DDoS mitigation simulation that uses rate-limiting, CAPTCHA gating, and IP blacklisting on a sample web server under simulated attack.",
    
    "An email spoofing detector that checks SPF, DKIM, and DMARC configurations for a domain and flags possible spoofing vulnerabilities.",
    
    "A secure mobile app prototype that protects against screen capture, clipboard sniffing, and unauthorized background activity on Android.",
    
    "A vulnerability scanner for Docker containers that checks image base layers for known exploits and outdated packages.",
    
    "A QR code phishing prevention tool that scans QR codes for redirection and validates destination domains before opening them.",
    
    "A digital evidence chain-of-custody tracker using blockchain to store evidence transactions, ensuring tamper-proof logs.",
    
    "A keystroke dynamics authentication system that learns the rhythm and speed of typing to verify identity beyond passwords.",
    
    "A browser-based social engineering game that teaches users how to identify manipulative messages, fake login prompts, and too-good-to-be-true offers.",
    
    "A self-destructing file sharing app where files are encrypted and hosted temporarily with an expiration timer and download limit.",
    
    "A tool to audit open-source packages for malicious dependencies, typosquatting, and post-install scripts that could pose threats.",
    
    "A smart home security audit tool that connects to IoT hubs and analyzes devices for open ports, weak authentication, or misconfiguration."
]