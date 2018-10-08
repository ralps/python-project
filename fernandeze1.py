message = "I am {Maurice Ralph  Fernandez}.\n" + \
          "My Spirit animal is {Dragon},\n" + \
          "because{I like to sleep}.\n" +\
          "When not in school, I love to {Play online games}.\n" + \
          "I dream of being a/an {Programmer} in the future."

         

data = {"name" : "Maurice Ralph Fernandez",
         "spirit_animal" : "Dragon",
         "reason": "i like to sleep",
         "hobby": "playing online games",
         "proffession": "dae ko aram"}

print (message.format(                                         
         data["name"], \
         data["spirit_animal"],  \
         data["reason"], \
         data["hobby"], \
         data["proffession"] 
         ))
