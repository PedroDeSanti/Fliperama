from pymongo import MongoClient, DESCENDING
class LeaderBoard:

    def __init__(self):
        self.client = MongoClient("mongodb+srv://teste:teste@cluster0.vpoht.mongodb.net/fliperama_db?retryWrites=true&w=majority")
        self.db = self.client.get_database('fliperama_db')
        self.scores = self.db.score

    # Obtém do BD as pontuações de determinada dificuldade
    def get(self, difficult):
        player = []
        score_list = []
        
        # Seleciona do BD os valores da dificuldade correspondente, e os coloca em ordem decrescente
        lista = list(self.scores.find({"difficult": difficult}).sort("score", DESCENDING))
        # For testing
        # lista = list(self.scores.find().sort("score", DESCENDING))
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

    # Adiciona uma nova pontuação ao BD
    def add(self, nick, score, difficult):
        # id do é 1 acima do anterior
        doc_count = self.scores.count_documents({})
        id_number = doc_count + 1
        # insere o id, nick, score e dificuldade do jogador no BD do ranking
        self.scores.insert_one({"_id": id_number, "nick": nick, "score": score, "difficult": difficult})

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