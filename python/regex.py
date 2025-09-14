import re

sample_text = """
Hello World!  
Email: example123@test-mail.com  
Phone: +1-202-555-0173  
Date: 2025-08-13 
d=2025-13-13 
Price: $199.99  
ID: A1B2C3  
URL: https://www.example.com/path?query=regex  
"""
answer = " , i'm jckawin Yes"

text=" im kawin , im kawin , im kawin"

pattern = r"https://\w+\.?\w+\.\w+" 
finder = re.findall(pattern,sample_text)
substitution = re.sub(r'kawin' , "nisarg", text , 2)
print(substitution)
print(finder) 