# import os

from pymongo import MongoClient, DESCENDING


class LeaderBoard:

    # client = MongoClient("mongodb+srv://teste:teste@cluster0.vpoht.mongodb.net/fliperama_db?retryWrites=true&w=majority")
    # db = client.get_database('fliperama_db')
    # scores =  db.score


    #ou
    # db = client['fliperama_db']
    # collection = db['score']


    # uri = "mongodb://test1:test1@ds051990.mongolab.com:51990/joran1"
    # my_db_cli = MongoClient(uri)
    # db = my_db_cli.joran1  # select the database ... 

    # my_scores = db.scores  # this will be created if it doesn't exist!
    # # add a new score
    # my_scores.insert({"user_name": "Leeeeroy Jenkins", "score": 124, "time": "11/24/2014 13:43:22"})
    # my_scores.insert({"user_name": "bob smith", "score": 88, "time": "11/24/2014 13:43:22"})

    # # get a list of high scores (from best to worst)
    # print(list(scores.find().sort("score", DESCENDING)))


    # def create_leaderboard():
    #     return True


    def __init__(self):
        self.client = MongoClient("mongodb+srv://teste:teste@cluster0.vpoht.mongodb.net/fliperama_db?retryWrites=true&w=majority")
        self.db = self.client.get_database('fliperama_db')
        self.scores = self.db.score

    def get(self, difficult):
        # here = os.path.dirname(os.path.abspath(__file__))
        # filename = os.path.join(here, "map.txt")
        # file = open(filename)

        # file = open("teste.lb",'w')
        # file.close()

        # names = []
        # score = []

        # with open('teste.txt', 'r') as file:
        #     content = file.readlines()
        #     for line in content:
        #         for char in line:
        player = []
        score_list = []

        # lista = list(self.scores.find({"difficult": difficult}).sort("score", DESCENDING))
        lista = list(self.scores.find().sort("score", DESCENDING))
        # print(lista[0])
        for item in lista:
            # print(item)
            for field in item:
                if (field == 'nick'):
                    player.append(item[field])
                if (field == 'score'):
                    player.append(item[field])
                # print("player: ", player)
            score_list.append(player)
            # print("score_list: ", score_list)
            player = []
            # print("score_list: ", score_list)
        # print(lista)

        # print("score_list: ", score_list)
        return score_list
        #

        # return True


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