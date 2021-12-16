import json
class vocabularyclass:
        def __init__(self):
            with open("vocabulary.json","r",encoding="UTF8") as vocajson:
                self.voca = json.load(vocajson)
        def save(self):
            with open("vocabulary.json", "w", encoding="UTF8") as jvocajson:
                json.dump(self.voca,jvocajson,ensure_ascii=False,indent=4)

        def add(self,word,mean):
            self.jvoca = self.voca["jvocabulary"]
            self.jvoca[word]=mean
            self.save()

        def modify(self,word,mean):
            self.mjvoca = self.voca["jvocabulary"]
            if word in self.mjvoca:
                self.mjvoca[word]=mean
                self.save()
            else:
                print(f"The corresponding \'{word}\' word is not registered in the vocabulary. So progran couldn't modify that \'{word}\' word")

        def delete(self,word):
            self.djvoca = self.voca["jvocabulary"]
            if word in self.djvoca:
                del self.djvoca[word]
                self.save()
            else:
                print(f"The corresponding \'{word}\' word is not registered in the vocabulary. So progran couldn't delete that \'{word}\' word")