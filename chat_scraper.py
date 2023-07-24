import re

chat_file = 'Russ_chat.txt'

clean_lines = []
lower_clean_lines = []
start_date = ''
word_list = []
senders = []
sight_words = ['a','i','to', 'and', 'the', 'is', 'it', 'in', 'you', 'ya', 
                           'that','for', 'was', 'like', 'of', 'on', 'he', 'be', 'but',
                           'if', 'so', 'have']
senders_lower = []

#Remove Unicode
with open(chat_file, "r") as f:
    content = f.read()

    # Remove all unicode characters from the text.
    clean_content = re.sub(r"[^\x00-\x7F]", "", content)

    with open(chat_file, "w") as f:
        f.write(clean_content)

#creating Start Date
with open(chat_file, "r") as those_guys:
    start_date = ''
    lines = 0
    for line in those_guys:
        if lines == 6:
            start_date += line[1:11]
            break
        lines += 1
    
        

#Removing Date and Time 
def remove_beginning(line):
    i = 0
    while i < len(line) and not line[i] == ']':
        i += 1
    return line[i+2:]

with open(chat_file, "r") as those_guys:
    clean_lines = []
    for line in those_guys.readlines():
        clean_lines.append(remove_beginning(line))

        
#Cleaning up the lines
clean_lines = [line for line in clean_lines if "omitted" not in line]
clean_lines = [line for line in clean_lines if "State Major" not in line]
clean_lines = [line for line in clean_lines if not line.startswith("Those Guys")]
clean_lines = [line for line in clean_lines if ":" in line]

#Writing cleaned up chat to a new .txt file 
with open("clean_tg.txt", "w") as clean_tg:
    clean_tg.writelines(clean_lines)

#Create Sender  
with open("clean_tg.txt", "r") as clean_tg:
    for line in clean_tg:
        i = 0
        if not line:
            continue
        while i < len(line):
            if line[i] == ':':
                break
            i += 1
        sender = line[:i]
        if len(senders) >= 7:
            break
        if sender not in senders:
            senders.append(sender)        
                
                

#Splitting Each word
def split_to_words(list):
    for string in list:
        words = string.split()
        word_list.extend(words)

#Making Everything Lowercase    
def make_all_lowercase(list_of_items):
  for item in list_of_items:
    new_item = item.lower()
    lower_clean_lines.append(new_item)
  return lower_clean_lines
make_all_lowercase(clean_lines)

#Each person sent how many messages 
def count_messages(sender = sender, list = clean_lines):
    count = 0
    for line in list:
        if sender in line:
            count+= 1
    print("{} has sent: '{}' messages since {}.".format(sender.title(), 
                                                        count, start_date))

def each_sent():
    for sender in senders:
        count_messages(sender)

#what was said how many times total
def phrase_count(phrase):
    count = 0
    for line in lower_clean_lines:
        if phrase in line:
            count+= 1
    print(f"The phrase: '{phrase}' has been said: '{count}' times since {start_date}.")

#One person sent what 
def sent_by(phrase, sender = sender, list = lower_clean_lines):
    count = 0
    for line in list:
        if sender.lower() in line and phrase in line:
            count += 1
    print("The phrase: '{}' has been sent: {} times by {} since {}."
          .format(phrase, count, sender, start_date))

#Top 10 Words
def get_top_ten(list = lower_clean_lines):
    word_count = {}
    for word in list:
        if word in excluded_words:
            pass
        else:
            word_count[word] = word_count.get(word, 0) + 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse = True)

    for word, count in sorted_words[:10]:
        print(f"'{word}' has been sent '{count}' times since {start_date}.")

def print_top_ten():
    print("The following are the top 10 uncommon words:")
    get_top_ten()

#Creating Excluded words list for top 10
excluded_words = []
for word in sight_words:
    excluded_words.append(word)

for sender in senders:
    excluded_words.append(sender)

for sender in senders:
    senders_lower.append(sender.lower())

for sender in senders_lower:
    excluded_words.append(sender)

sender_colon = []
for sender in senders_lower:
    sender_colon.append(sender + ':')

for sender in sender_colon:
    excluded_words.append(sender)    

#All User Function
def all_senders(phrase):
    for sender in senders:
        sent_by(phrase, sender, lower_clean_lines)

#Calls
each_sent()
all_senders('haha')
phrase_count('lol')
print_top_ten()








