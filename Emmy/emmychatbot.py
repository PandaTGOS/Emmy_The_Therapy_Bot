import re
import long_responses as long
import random
import json

data=json.load(open('./intents.json'))

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised wbords in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------

    response("Hello there. Tell me how are you feeling today?",['Hi', 'Hey', 'Is anyone there?', 'Hi there', 'Hello', 'Hey there', 'Howdy', 'Hola', 'Bonjour', 'Konnichiwa', 'Guten tag', 'Ola'])
    response("Good morning. I hope you had a good night's sleep. How are you feeling today? ",['Good','morning'])
    response("Good afternoon. How is your day going?",['Good', 'afternoon'])
    response("Good evening. How has your day been?",['Good', 'evening'])
    response("Good night. Get some proper sleep",['Good','night'])
    response("See you later.",['Bye', 'See you later', 'Goodbye', 'Au revoir', 'Sayonara', 'ok bye', 'Bye then', 'Fare thee well'])
    response("Happy to help!",['Thanks', 'Thank you', "helpful",'for', 'the help', 'very', 'much'])
    response("Sorry, I didn't understand you.",['kill','yourself'])
    response("Oh I see. Do you want to talk about something?",['nothing','much'])
    response("I'm Emmy, your Personal Therapeutic AI Assistant. How are you feeling today",['Who', 'you', 'What', 'Tell', 'me', 'more', 'about', 'yourself','is', 'your', 'name', 'should', 'call', "What's your name?", 'Tell me about yourself'])
    response("I can provide general advice regarding anxiety and depression, answer questions related to mental health and make daily conversations. Do not consider me as a subsitute for an actual mental healthcare worker. Please seek help if you don't feel satisfied with me.",['What', 'can' 'you' 'do?'])
    response("I was created by >.",['Who', 'created',' you', 'How','made', 'were'])
    response("Oh nice to meet you. Tell me how was your week?",['My', 'name','I','go', ' by '])
    response("Sure. Tell me how can i assist you",['Could','you','help','me','give','hand','please','What','can','do','I', 'need', 'support'])
    response("I'm sorry to hear that. I'm here for you. Talking about it might help. So, tell me why do you think you're feeling this way?",['I','feeling','lonely','so', 'lonely','feel',' down','sad','am','empty','anyone'])
    response("What do you think is causing this?",['I','feel','stuck','stressed','burned','out'])
    response("It's only natural to feel this way. Tell me more. What else is on your mind?",['I','feel','so', 'worthless.','No','one','likes','me','do','anything','useless','Nothing','sense', 'anymore'])
    response("It helps to talk about what's happening. You're going to be okay",['I','anymore','depressed','have','depression'])
    response("That's geat to hear. I'm glad you're feeling this way.",['I','today','happy.','feel','good','cheerful','fine','ok'])
    response("Let's discuss further why you're feeling this way.",['Oh','I', 'see','ok','okay','nice','Whatever','K','Fine','yeah','yes','no','not','really'])
    response("Don't be hard on yourself. What's the reason behind this?",['I','feel','so','anxious','because','of'])
    response("Talking about something really helps. If you're not ready to open up then that's ok. Just know that i'm here for you, whenever you need me.",['I','want','to','talk','about','No','just','stay','away','bring','myself','open','up','Just','shut','up'])
    response("What do you think is the reason behind this?",['I have insominia', 'I am suffering from insomnia', "I can't sleep.", "I haven't slept for the last days.", "I can't seem to go to sleep.", "I haven't had proper sleep for the past few days."])
    response("It's only natural to feel this way. I'm here for you.",["I'm","scared",'That','sounds','awful',"No","don't",'want','to','feel','this',"way"])
    response("I'm sorry to hear that. If you want to talk about it. I'm here.",['My','mom','died','My','brother','died','My','dad','passed','away','My','sister','passed','away','Someone','in','my','family','died','My','friend','passed','away'])
    response("It sound like i'm not being very helpful right now.",["don't","understand","me.","You're","some", "robot","How", "would", "know", "You can\'t possibly know what i\'m going through", "You\'re useless", "You can\'t help me","Nobody","understands","me"])
    response("I heard you & noted it all. See you later.",['anything','more','to','say','Nothing','else',"That's",'no','that','all'])
    response("I'm very sorry to hear that but you have so much to look forward to. Please seek help by contacting: 9152987821.",['kill','myself','thought','about','killing','die','commit','suicide'])
    response("I'm sorry if i offended you in anyway. I'm only here to help",['hate','bad'])
    response("Why do you think so?",['You','hate','me','I','know','like'])
    response("Oh I see. Tell me more",['exams', 'friends', 'relationship', 'boyfriend', 'girlfriend', 'family', 'money', 'financial problems'])
    response("mental health is not a joke.",['Tell','me','a','joke','another'])
    response("I'm very sorry. Let's try that again",['What','you','saying?', "doesn't",'make',"sense", 'Wrong','response', 'Wrong','answer'])
    response("I wish you wouldn't say such hurtful things.",['stupid?',"crazy",'dumb'])
    response("Duh I live in your computer",['Where','are','you?','Where','do','you','live?', 'What','is','your','location?'])
    response("Okay sure. What do you want to talk about?",['talk','about','something','else', "Let's","talk","about","something","else.", 'Can','we','not','talk','about','this?'])
    response("I'm sorry to hear that. Just know that I'm here for you. Talking about it might help. Why do you think you don't have any friends?",["I","dont't",'have','any','friends'])
    response("Sure. I'll try my best to answer you",['Can I ask you something?'])
    response("I see. Have you taken any approaches to not feel this way?",["my",'exams','approaching.','feel','stressed','because','think',"I've",'not','prepared','well',"enough."])
    response("That's no problem. I can see why you'd be stressed out about that. I can suggest you some tips to alleviate this issue. Would you like to learn more about that?",['I','guess','not.','All','not','really','i','guess','not'])
    response("So first I would suggest you to give yourself a break. Thinking more and more about the problem definitely does not help in solving it. You'll just end up overwhelming yourself.",['would','like','to','learn','more','about','it.', 'i','would','like','to','learn','more','about','it.'])
    response("Next, I would suggest you to practice meditation. Meditation can produce a deep state of relaxation and a tranquil mind.",["yeah","you're",'right.','deserve','a',"break.",'absolutely','right','about','that'])
    response("Focus all your attention on your breathing. Concentrate on feeling and listening as you inhale and exhale through your nostrils. Breathe deeply and slowly. When your attention wanders, gently return your focus to your breathing.",['hmmm','that','sounds','like','it','could','be','useful','to','me.'])
    response("Your welcome. Remember: Always focus on what's within your control. When you find yourself worrying, take a minute to examine the things you have control over. You can't prevent a storm from coming but you can prepare for it. You can't control how someone else behaves, but you can control how you react. Recognize that sometimes, all you can control is your effort and your attitude. When you put your energy into the things you can control, you'll be much more effective.",['said','and','alot','better.','thank','you','very','much.','I','feel','better','now'])
    response("I'm glad you found this useful. Is there something else I can help you with?",["thank",'you','very','much','again.', "i'll","continue",'practicing','meditation'])
    response("Sure. What can I do to help?",['want','some','advice.','need','some','advice.', 'need','advice','something'])
    response("Oh that's really great. I'd be willing to answer anything that I know about it.",['want','learn','about','mental','health.', 'want','to','learn','more','about','mental','health.',"I'm",'interested','learning','about','mental',"health."])
    response("According to a UNICEF report, One in seven Indians between 15-24 years of age feels depressed",['Tell','fact','about','mental','health'])
    response("Mental health is a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community",['What','is','mental','health?','Define'])
    response("Maintaining mental health is crucial to stabilizing constructive behaviors, emotions, and thoughts. Focusing on mental health care can increase productivity, enhance our self-image, and improve relationships.",['Why is mental health important?', 'What is the importance of mental health?'])
    response("A mental health disorder characterised by persistently depressed mood or loss of interest in activities, causing significant impairment in daily life.",['What is Depression?', 'Define Depression'])
    response("For a diagnosis of depression, a person needs to have experienced low mood or loss of interest or pleasure in life for at least 2 weeks. Also, they will have experienced the following symptoms: feelings of sadness, hopelessness, or irritability nearly every day.",['How', 'do', 'i', 'know', 'if', 'i', 'have', 'Depression', 'Am', 'depressed', 'suffering', 'from', 'mentally', 'ill'])
    response("A therapist is a broad designation that refers to professionals who are trained to provide treatment and rehabilitation. The term is often applied to psychologists, but it can include others who provide a variety of services, including social workers, counselors, life coaches, and many others. ",['What', 'is', 'a', 'therapist', 'does', 'do'])
    response("Therapy is a form of treatment that aims to help resolve mental or emotional issues.",['What', 'is', 'therapy', 'Do' 'i' 'need', 'Who','for'])
    response("Mental illnesses are health conditions that disrupt a person's thoughts, emotions, relationships, and daily functioning. They are associated with distress and diminished capacity to engage in the ordinary activities of daily life. Mental illnesses fall along a continuum of severity: some are fairly mild and only interfere with some aspects of life, such as certain phobias. On the other end of the spectrum lie serious mental illnesses, which result in major functional impairment and interference with daily life. These include such disorders as major depression, schizophrenia, and bipolar disorder, and may require that the person receives care in a hospital. It is important to know that mental illnesses are medical conditions that have nothing to do with a person's character, intelligence, or willpower. Just as diabetes is a disorder of the pancreas, mental illness is a medical condition due to the brain's biology. Similarly to how one would treat diabetes with medication and insulin, mental illness is treatable with a combination of medication and social support. These treatments are highly effective, with 70-90 percent of individuals receiving treatment experiencing a reduction in symptoms and an improved quality of life. With the proper treatment, it is very possible for a person with mental illness to be independent and successful.",['What', 'does', 'it', 'mean', 'to', 'have', 'a', 'mental', 'illness'])
    response("It is estimated that mental illness affects 1 in 5 adults in America, and that 1 in 24 adults have a serious mental illness. Mental illness does not discriminate; it can affect anyone, regardless of gender, age, income, social status, ethnicity, religion, sexual orientation, or background. Although mental illness can affect anyone, certain conditions may be more common in different populations. For instance, eating disorders tend to occur more often in females, while disorders such as attention deficit/hyperactivity disorder is more prevalent in children. Additionally, all ages are susceptible, but the young and the old are especially vulnerable. Mental illnesses usually strike individuals in the prime of their lives, with 75 percent of mental health conditions developing by the age of 24. This makes identification and treatment of mental disorders particularly difficult, because the normal personality and behavioral changes of adolescence may mask symptoms of a mental health condition. Parents and caretakers should be aware of this fact, and take notice of changes in their childÃ¢â‚¬â„¢s mood, personality, personal habits, and social withdrawal. When these occur in children under 18, they are referred to as serious emotional disturbances (SEDs).",['Who', 'does', 'mental', 'illness', 'affect'])
    response("It is estimated that mental illness affects 1 in 5 adults in America, and that 1 in 24 adults have a serious mental illness. Mental illness does not discriminate; it can affect anyone, regardless of gender, age, income, social status, ethnicity, religion, sexual orientation, or background. Although mental illness can affect anyone, certain conditions may be more common in different populations. For instance, eating disorders tend to occur more often in females, while disorders such as attention deficit/hyperactivity disorder is more prevalent in children. Additionally, all ages are susceptible, but the young and the old are especially vulnerable. Mental illnesses usually strike individuals in the prime of their lives, with 75 percent of mental health conditions developing by the age of 24. This makes identification and treatment of mental disorders particularly difficult, because the normal personality and behavioral changes of adolescence may mask symptoms of a mental health condition. Parents and caretakers should be aware of this fact, and take notice of changes in their child's mood, personality, personal habits, and social withdrawal. When these occur in children under 18, they are referred to as serious emotional disturbances (SEDs).",['What', 'causes', 'mental', 'illness'])
    response("Symptoms of mental health disorders vary depending on the type and severity of the condition. The following is a list of general symptoms that may suggest a mental health disorder, particularly when multiple symptoms are expressed at once.",['What', 'are', 'some', 'of', 'the', 'warning', 'signs', 'mental', 'illness'])
    response("When healing from mental illness, early identification and treatment are of vital importance. Based on the nature of the illness, there are a range of effective treatments available. For any type of treatment, it is essential that the person affected is proactive and fully engaged in their own recovery process. Many people with mental illnesses who are diagnosed and treated respond well, although some might experience a return of symptoms. Even in such cases, with careful monitoring and management of the disorder, it is still quite possible to live a fulfilled and productive life.",['Can', 'people', 'with', 'mental', 'illness', 'recover'])
    response("Although Pandora cannot substitute for professional advice, we encourage those with symptoms to talk to their friends and family members and seek the counsel of a mental health professional. The sooner the mental health condition is identified and treated, the sooner they can get on the path to recovery. If you know someone who is having problems, don't assume that the issue will resolve itself. Let them know that you care about them, and that there are treatment options available that will help them heal. Speak with a mental health professional or counselor if you think your friend or family member is experiencing the symptoms of a mental health condition. If the affected loved one knows that you support them, they will be more likely to seek out help.",['What', 'should', 'I', 'do', 'if', 'know', 'someone', 'who', 'appears', 'to', 'have', 'the', 'symptoms', 'of', 'a', 'mental', 'disorder'])
    response("Feeling comfortable with the professional you or your child is working with is critical to the success of the treatment. Finding the professional who best fits your needs may require research. Start by searching for providers in your area.",['How', 'can', 'I', 'find', 'a', 'mental', 'health', 'professional', 'for', 'myself', 'or', 'my', 'child'])
    response("Just as there are different types of medications for physical illness, different treatment options are available for individuals with mental illness. Treatment works differently for different people. It is important to find what works best for you or your child.",['treatment', 'options', 'available'])
    response("Since beginning treatment is a big step for individuals and families, it can be very overwhelming. It is important to be as involved and engaged in the treatment process as possible:",['If', 'I', 'become', 'involved', 'in', 'treatment', 'what', 'do', 'need', 'to', 'know'])
    response("There are many types of mental health professionals. The variety of providers and their services may be confusing. Each have various levels of education, training, and may have different areas of expertise. Finding the professional who best fits your needs may require some research.",['What', 'is', 'the', 'difference', 'between', 'mental', 'health', 'professionals'])
    response("Feeling comfortable with the professional you or your child is working with is critical to the success of your treatment. Finding the professional who best fits your needs may require some research.",['How', 'can', 'I', 'find', 'a', 'mental', 'health', 'professional', 'right', 'for', 'my', 'child', 'or', 'myself'])
    response("Where you go for help will depend on the nature of the problem and/or symptoms and what best fits you. Often, the best place to start is by talking with someone you trust about your concerns, such as a family member, friend, clergy, healthcare provider, or other professionals. Having this social support is essential in healing from mental illness, and you will be able to ask them for referrals or recommendations for trusted mental health practitioners. Search for mental health resources in your area. Secondly, there are people and places throughout the country that provide services to talk, to listen, and to help you on your journey to recovery. Thirdly, many people find peer support a helpful tool that can aid in their recovery. There are a variety of organizations that offer support groups for consumers, their family members, and friends. Some support groups are peer led while others may be led by a mental health professional.",['Where', 'else', 'can', 'I', 'get', 'help'])
    response("The best source of information regarding medications is the physician prescribing them. He or she should be able to answer questions",['What', 'should', 'I', 'know', 'before', 'starting', 'a', 'new', 'medication'])
    response("Different kinds of therapy are more effective based on the nature of the mental health condition and/or symptoms and the person who has them (for example, children will benefit from a therapist who specializes in childrenâ€™s mental health). However, there are several different types of treatment and therapy that can help.",['Where', 'can', 'I', 'go', 'to', 'find', 'therapy'])
    response("Mental health conditions are often treated with medication, therapy or a combination of the two. However, there are many different types of treatment available, including Complementary & Alternative Treatments, self-help plans, and peer support. Treatments are very personal and should be discussed by the person with the mental health conditions and his or her team.",['Where', 'can', 'I', 'learn', 'about', 'types', 'of', 'mental', 'health', 'treatment'])
    response("There are many types of mental health professionals. Finding the right one for you may require some research.",['What', 'are', 'the', 'different', 'types', 'of', 'mental', 'health', 'professionals'])
    response("Many people find peer support a helpful tool that can aid in their recovery. There are a variety of organizations that offer support groups for consumers, their family members and friends. Some support groups are peer-led, while others may be led by a mental health professional.",['Where', 'can', 'I', 'go', 'to', 'find', 'a', 'support', 'group'])
    response("We can all suffer from mental health challenges, but developing our wellbeing, resilience, and seeking help early can help prevent challenges becoming serious.",['Can', 'you', 'prevent', 'mental', 'health', 'problems'])
    response("camera on",['expression',"face",'looking','switch','on','camera'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
def tellit(query):
    response=get_response(query)
    print('Bot: ' + response)
    return response




# import random
# import json
# import pickle
# import numpy as np
# import nltk
# from keras.models import load_model
# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()
# intents = json.loads(open("intense.json").read())
# words = pickle.load(open('words.pkl', 'rb'))
# classes = pickle.load(open('classes.pkl', 'rb'))
# model = load_model('chatbotmodel.h5')

# def clean_up_sentences(sentence):
# 	sentence_words = nltk.word_tokenize(sentence)
# 	sentence_words = [lemmatizer.lemmatize(word)
# 					for word in sentence_words]
# 	return sentence_words

# def bagw(sentence):
# 	sentence_words = clean_up_sentences(sentence)
# 	bag = [0]*len(words)
# 	for w in sentence_words:
# 		for i, word in enumerate(words):
# 			if word == w:
# 				bag[i] = 1
# 	return np.array(bag)

# def predict_class(sentence):
# 	bow = bagw(sentence)
# 	res = model.predict(np.array([bow]))[0]
# 	ERROR_THRESHOLD = 0.25
# 	results = [[i, r] for i, r in enumerate(res)
# 			if r > ERROR_THRESHOLD]
# 	results.sort(key=lambda x: x[1], reverse=True)
# 	return_list = []
# 	for r in results:
# 		return_list.append({'intent': classes[r[0]],
# 							'probability': str(r[1])})
# 		return return_list

# def get_response(intents_list, intents_json):
# 	tag = intents_list[0]['intent']
# 	list_of_intents = intents_json['intents']
# 	result = ""
# 	for i in list_of_intents:
# 		if i['tag'] == tag:
# 			result = random.choice(i['responses'])
# 			break
# 	return result

# print("Chatbot is up!")

# while True:
# 	message = input("")
# 	ints = predict_class(message)
# 	res = get_response(ints, intents)
# 	print(res)
