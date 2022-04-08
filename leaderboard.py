from this import d
from pymongo import MongoClient, DESCENDING

MESSAGE_LENGTH = 7
class LeaderBoard:

    def __init__(self):
        self.message = ""
        self.last_score = (0, "AAA", 0)
        self.client = MongoClient("mongodb+srv://teste:teste@cluster0.vpoht.mongodb.net/fliperama_db?retryWrites=true&w=majority")
        self.db = self.client.get_database('fliperama_db')
        self.scores = self.db.score

    # Obtém do BD as pontuações de determinada dificuldade
    def get(self, difficulty):
        player = []
        score_list = []
        
        # Seleciona do BD os valores da dificuldade correspondente, e os coloca em ordem decrescente
        # lista = list(self.scores.find({"difficulty": difficulty}).sort("score", DESCENDING))
        # For testing
        lista = list(self.scores.find().sort("score", DESCENDING))
        # adiciona cada pontuação daquela dificuldade no ranking
        for item in lista:
            for field in item:
                if (field == 'nick'):
                    player.append(item[field])
                if (field == 'score'):
                    player.append(item[field])
            # coloca no ranking nick+score 
            score_list.append(player)
            player = []

        return score_list

    # # Adiciona uma nova pontuação ao BD
    # def add(self, nick, score, difficulty):
    #     # id do é 1 acima do anterior
    #     doc_count = self.scores.count_documents({})
    #     id_number = doc_count + 1
    #     # insere o id, nick, score e dificuldade do jogador no BD do ranking
    #     self.scores.insert_one({"_id": id_number, "nick": nick, "score": score, "difficulty": difficulty})

    def add(self):
        self.translate_message()
        difficulty, nick, score = self.last_score
        # id do é 1 acima do anterior
        doc_count = self.scores.count_documents({})
        id_number = doc_count + 1
        # insere o id, nick, score e dificuldade do jogador no BD do ranking
        self.scores.insert_one({"_id": id_number, "nick": nick, "score": score, "difficulty": difficulty})


    def construct_message(self, char):
        if (len(self.message) < MESSAGE_LENGTH):
            self.message += char
        else:
            self.message = char

    def translate_message(self):
        print(self.message)
        difficulty = self.message[0:1]
        nick = self.message[1:4]
        score = self.tradutorHexDec(self.message[4:])
        self.last_score = (difficulty, nick, score)
        print(self.last_score)
    
    # retorna o int em decimal
    def intCorrespondente(self, charHex):
        if charHex in "0123456789":
            return int(charHex)
        elif charHex.lower() in "abcdef":
            return (ord(charHex.lower()) - ord("a") + 1) + 9

    # retorna o valor da pontuação em decimal
    def tradutorHexDec(self, numeroHex):
        aux = 1
        resultado = 0

        for i in range(len(numeroHex)): 
            resultado += aux * self.intCorrespondente(numeroHex[len(numeroHex)-1-i])
            aux *= 16
        return resultado

    def clear_all_scores(self):
        self.scores.delete_many({})


# For testing:

# leader_board = LeaderBoard()
# leader_board.clear_all_scores()
# lista = leader_board.get(1)
# lista = leader_board.get(2)
# lista = leader_board.get(3)
# print(lista)

# leader_board.add("Deg", 9000, 1)
# leader_board.add("lol", 6500, 1)
# leader_board.add("Lin", 1700, 1)
# leader_board.add("Aux", 12000, 1)
# leader_board.get(2)

#-m pip install "pymongo[srv]"