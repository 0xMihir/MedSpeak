## Inspiration

Healthcare providers spend nearly half of their time with their patients entering data into outdated, non-user-friendly software. After listening to Professor Paul Tang's talk _Medical Mind Meld for Patient Safety_, we were inspired to tackle the obvious and concerning **gap in communication** between patients and physicians.

The current Electronic Health Record (EHR) system is unnecessarily difficult to navigate. For instance, doctors must go through multiple steps (clicking, scrolling, typing) to access the necessary diagnostic information. This is **time-consuming and mentally taxing**. It negatively impacts the doctor-patient relationship because the doctor's attention is perpetually on the monitor rather than on the patient. In a nation with a somewhat disturbing track record in medical outcomes, we felt that something had to change. 

Tackling this giant of a problem one step at a time, we built a medical assistant that helps doctors efficiently filter through patient information and extract critical information for diagnoses, allowing them to focus on personalizing each patient's care. This new interface hopes to **alleviate a physician's information overload** and **maximize a patient's mental and physical well-being**. 


## What it does

Our web application consists of two main functionalities: a **conversation visualizer** and a **ranked prompt list**. 

The conversation visualizer takes in a transcript of a recording of the interaction between the patient and physician. The speech bubbles indicate which speaker each message corresponds to. Behind this interface, the words are processed to determine what topics are currently being discussed. 

The ranked prompt list pulls the most relevant past information for the patient to the forefront of the list, making it easy for the physician to ask better clarifying questions or make adjustments to their mental model, all without having to click and scroll through tens or hundreds of records.


## How we built it

Our end goal is to help doctors efficiently filter and prioritize patient data, so each aspect of our process (ML, backend, frontend) attempts to address that in some way.

We designed a **deep-learning-based recommendation system** for features within the patient’s Electronic Health Records (EHR). It decides what information should be displayed based on the patient’s description of their medical needs and symptoms. We leveraged the **OpenAI Embedding API** to embed string token representations of these key features into a high dimensional vector space and extract semantic similarity between each. Then, we employed the _k_-nearest neighbor algorithm to compute and display the top _k_ relevant features. This allowed us to cluster related keywords together, such as "COVID" with "shortness of breath". The appearance of one word/phrase in the cluster will bring EHR data containing other related words/phrases to the top of the list. 

We implemented the ML part of the backend using **Flask in Python**. The main structure and logic were done in **Node.js** within the **Svelte** framework. We designed the UI and front-end layout in Svelte to create something easy to navigate and use in time-sensitive situations. We designed the left panel to be the conversation visualizer, along with an option to record sound (see "What's next for MedSpeak"). The right panel holds the prompt list, which updates in real time as more information is fed in.


## Challenges we ran into

One challenge we encountered was understanding the medical workflow and procuring simulated medical data to work with. As none of us had much background in the medical field, it took us some time to find the right data. This also led to difficulties in settling on a final project idea, since we were not sure what kind of information we had access to. However, speaking with Professor Tang and other non-hackers to flesh out our idea was incredibly insightful and helped lead us onto the right track.


## Accomplishments that we're proud of

We are proud of generating a novel application of existing technology in a way that benefits the sector most in need of an upgrade.

Our solution has great potential in the daily medical workplace. It is able to **integrate past and ongoing patient information** to enhance and expedite the interaction for both parties. The implementation of our solution would result in a considerable reduction in the number of physical steps and the level of attention required to record pertinent data.

Our product's effects are twofold. It decreases the **mental and physical attention** needed for doctors to retrieve medical information. It allows doctors to spend **quality time communicating** with patients, fostering relationships built on trust and mutual understanding.


## What we learned

Over the course of this hackathon, each of us on the team became more familiar with technologies like machine learning and general full-stack development. Coming in individually with our separate skill sets, we needed to share our respective knowledge with the others in order to stay on the same page throughout. Thus we each picked up some important tidbits of the others’ expertise, enabling us to become better developers and engineers.

To build on that, we learned the importance of keeping everyone up to speed about the general direction of the project. Since we did not confirm our group until very late on the first day, we were delayed in settling on an idea and executing our tasks. More communication throughout the early stages could potentially have saved us time and confusion, allowing us to achieve more of our reach goals.

## Product Risk

Accuracy and ethics should always be a cornerstone of consideration when it comes to human health and well-being. Our product is no exception.

The medical metric recommendations may not function effectively when dealing with the latest medical metrics or conditions, as the pre-trained model is employed. This can potentially be mitigated by connecting our platform with the most up-to-date medical websites or journals. Even so, the model would require retraining every so often.

There is a possibility that doctors may become overly reliant on AI-generated prompts. While designing our solution, we purposefully stayed clear of having the prompt list return information that could be misinterpreted as diagnoses. It is incredibly dangerous to have a machine make official diagnoses, so there would have to be regulations in place to prevent abuse of the technology.

The voice transcription may not be (and likely is not) 100% accurate, which may lead to some inaccuracies in the vital signs or vital result recommendations. However, with enough training, we can hopefully make those occurrences a rarity. Even when they happen, the recording can ensure that we have a reference when verifying data.

It is imperative that physicians who use this product obtain the proper consent from their patients. Since our current product involves the transcription of a patient's words and our end goal involves an audio recording feature, sensitive information could be at risk. We should consult with legal professionals before making the product available.


## What's next for MedSpeak

Algorithmically, we aim to fine-tune the current embedding model on **clinical and biological datasets**, allowing the model to extract even more well-informed correlations based on a broader context pool. 

We also hope to extend this project to incorporate **real-time speech-to-text processing** into the visualizer. The recording would also act as a safety net in case the patient or physician wishes to revisit that conversation. 

A further extension would be the option to **autofill patient information** as the conversation goes on, as well as a **chatbot function** to quickly make changes to the record. The NLP aspect allows physicians to use abbreviations or more casual language, which saves mental resources in the long run.

Another feature could be an integration of hardware, by having **sensors that detect vital signs** transmit the data directly to the app. This would save time and energy for the nurse or doctor, enabling them to spend more time with their patient.
