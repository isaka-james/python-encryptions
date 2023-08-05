# author: masterplan

import random,sys,os,time

key = []
limit = 0
speed = 0.02

def text_out(text: str) -> None:
    for character in text:
        sys.stdout.write(character)y 
        sys.stdout.flush()
        time.sleep(speed)
 
while limit < 257:
    x = random.randint(0,3)
    
    if x == 0:
         key.append(chr(random.randint(97, 123)))
    if x == 1:
        key.append(chr(random.randint(65, 91)))
    if x == 2:    
        key.append(chr(random.randint(40,65)))
        
    limit = limit + 1
        
text_out(key)

# honest  note: written the following day after writting hill-ngosi-encryption, hence no chatGPT or internet was used,
# only i think was the notes from 'pydroid3' - my favourite compiler
