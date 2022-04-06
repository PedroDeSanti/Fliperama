from pymongo import MongoClient, DESCENDING
class LeaderBoard:

    def __init__(self):
        self.client = MongoClient("mongodb+srv://teste:teste@cluster0.vpoht.mongodb.net/fliperama_db?retryWrites=true&w=majority")
        self.db = self.client.get_database('fliperama_db')
        self.scores = self.db.score

    def get(self, difficult):
        player = []
        score_list = []

        lista = list(self.scores.find({"difficult": difficult}).sort("score", DESCENDING))
        # For testing
        # lista = list(self.scores.find().sort("score", DESCENDING))
        for item in lista:
            for field in item:
                if (field == 'nick'):
                    player.append(item[field])
                if (field == 'score'):
                    player.append(item[field])
            score_list.append(player)
            player = []

        return score_list

    def add(self, nick, score, difficult):
        doc_count = self.scores.count_documents({})
        id_number = doc_count + 1
        self.scores.insert_one({"_id": id_number, "nick": nick, "score": score, "difficult": difficult})

# For testing:

# leader_board = LeaderBoard()
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