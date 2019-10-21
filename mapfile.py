
def test_mapfile():
    biomes = open("biomes.txt")
    biomes = biomes.read().split("\n")
    fl = open("OneLifeData/tutorialMaps/tutorial1.txt")
    data = fl.read().split("\n")
    fl.close()
    cache = {}
    for line,loc in enumerate(data):
        if loc.strip() == "":
            continue
        x,y,biome,floor,ontop = loc.split(" ")
        print("location : ({},{}) ".format(x,y))
        print("biome: {} ({})".format(biomes[int(biome)],biome))
        if "," in ontop:
            things = ontop.split(",")
            print("container: {}".format(things.pop(0)))
            for item in things:
                if ";" in item:
                    items = item.split(";")
                    print("    container: {}".format(items.pop(0)))
                    for citem in items:
                        print("        has: {}".format(citem))
                else:
                    print("    has: {}".format(item))
        else:
            print("item:{}".format(ontop))


test_mapfile()
