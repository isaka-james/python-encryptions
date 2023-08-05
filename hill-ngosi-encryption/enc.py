# author: masterplan

class Alg:
    def __init__(self,plain_text,key):
        self.key,self.plain_text= key,plain_text
        self.lsplain,self.lskey = list(plain_text),list(key)
        self.plen = len(self.plain_text)
        self.klen = len(self.key)
        
    def render_en(self):
        remains = self.plen - self.klen
        rsv = remains
        add = 0
        while remains > 0:
            self.lskey.append(self.key[add])
            add+=1
            if add == self.klen:
                add = 0
            remains -= 1
            
        if remains == 0:
            pass
        elif remains < 0:
            self.lskey = self.lskey[:(remains+self.klen)]
            
        new = []
        for i in range(self.plen): # plen == klen
            new.append((i,self.lsplain[i]))
        return Alg.calc_enc(self,self.lskey,new)
        
    def calc_enc(self,k,n):
            encrypted_text = []
            for i,j in n:
                if (ord(j)>=97 and ord(j)<=122):
                       # 97 - 122
                       data = ((ord(j)+ ord(k[i])))%26
                       data+=97
                       encrypted_text.append(chr(data))
                elif (ord(j)>=65 and ord(j)<=90):
                    # 65 - 90
                    data = ((ord(j)+ ord(k[i])))%26
                    data+=65
                    encrypted_text.append(chr(data))
                elif (ord(j)>=32 and ord(j)<=64):
                    # 40 - 64
                    data = ((ord(j) + ord(k[i])))%32
                    data+=32
                    encrypted_text.append(chr(data))
                else:
                    encrypted_text.append(chr(0))
            return encrypted_text

     
    
# Take Inputs
plain_text = input("Enter a text: ")
key = input("Enter key: ")

# Create Object Class
encrypt = Alg(plain_text,key)

# make encryption
en = encrypt.render_en()

# Output Encryption
print(f"\n Encrypted Text(Cipher Text) : {en}")


# honest comment: written when i visited my grandpa i think it was like 02:00 , written with no internet hence no chatGPT were used in any part of this.
