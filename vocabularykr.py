import json
class vocabularyclass:
        def __init__(self): # 이거 태초에서 하는거임
            with open("vocabulary.json","r",encoding="UTF8") as vocajson:
                self.voca = json.load(vocajson)
        def save(self):
            with open("vocabulary.json", "w", encoding="UTF8") as jvocajson:
                json.dump(self.voca,jvocajson,ensure_ascii=False,indent=4)

        def add(self,word,mean): # 이거 단어 넣는거임
            self.jvoca = self.voca["jvocabulary"]
            self.jvoca[word]=mean
            self.save()

        def modify(self,word,mean): # 이거 단어 수정하는 거임
            self.mjvoca = self.voca["jvocabulary"]
            if word in self.mjvoca:
                self.mjvoca[word]=mean # 수정하는 곳임
                self.save()
            else:
                print(f"해당 \'{word}\' 단어가 단어장에 등록되어 있지 않습니다. 그래서 해당 \'{word}\' 단어를 수정하지 못했습니다")

        def delete(self,word): # 이거 단어 삭제하는 거임
            self.djvoca = self.voca["jvocabulary"]
            if word in self.djvoca:
                del self.djvoca[word] # 여기가 삭제하는 거임
                self.save()
            else:
                print(f"해당 \'{word}\' 단어가 단어장에 등록되어 있지 않습니다. 그래서 해당 \'{word}\' 단어를 삭제하지 못했습니다")