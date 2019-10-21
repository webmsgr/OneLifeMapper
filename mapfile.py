
def test_mapfile():
    fl = open("OneLifeData/tutorialMaps/tutorial1.txt")
    data = fl.read().split("/n")
    fl.close()
    cache = {}
    print(data)
    
    
