#message which sender wants to send to reciever taking from user
msg=input('enter  the message which sender wants to send:')
characters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#*@$ _+-'
key=8
encrypt=""
decrypt=""
for i in msg:
    position=characters.find(i)
    newposition=(position+8)%70
    encrypt+=characters[newposition]
print("the encrypted value is:",encrypt)
for j in encrypt:
    pos=characters.find(j)
    newpos=(pos-8)%70
    decrypt+=characters[newpos]
print("the decrypted value is:",decrypt)#the reciever recieves this message
